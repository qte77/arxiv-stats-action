'''
TODO short description

arxiv API output
  'id': 'http://arxiv.org/abs/2406.04221v1',
  'guidislink': True,
  'link': 'http://arxiv.org/abs/2406.04221v1',
  'updated': '2024-06-06T16:20:07Z',
  'updated_parsed': time.struct_time(tm_year=2024, tm_mon=6, tm_mday=6, tm_hour=16, tm_min=20, tm_sec=7, tm_wday=3, tm_yday=158, tm_isdst=0),
  'published': '2024-06-06T16:20:07Z',
  'published_parsed': time.struct_time(tm_year=2024, tm_mon=6, tm_mday=6, tm_hour=16, tm_min=20, tm_sec=7, tm_wday=3, tm_yday=158, tm_isdst=0),
  'title': 'Matching Anything by Segmenting Anything',
  'title_detail': {'type': 'text/plain', 'language': None, 'base': '', 'value': 'Matching Anything by Segmenting Anything'},
  'summary': 'The robust association of the same'
'''

# fetch and parse
import time
import feedparser
import urllib.request
# write to csv
from os import makedirs
from os.path import exists, dirname
import csv

def encode_feedparser_dict(d):
  """ helper function to strip feedparser objects using a deep copy """
  if isinstance(d, feedparser.FeedParserDict) or isinstance(d, dict):
      return {k: encode_feedparser_dict(d[k]) for k in d.keys()}
  elif isinstance(d, list):
      return [encode_feedparser_dict(k) for k in d]
  else:
      return d

def parse_arxiv_url(url):
  """
  example is http://arxiv.org/abs/1512.08756v2
  we want to extract the raw id (1512.08756) and the version (2)
  """
  ix = url.rfind('/')
  assert ix >= 0, 'bad url: ' + url
  idv = url[ix+1:] # extract just the id (and the version)
  rawid, version = idv.split('v')
  assert rawid is not None and version is not None, \
    f"error splitting id and version in idv string: {idv}"
  return idv, rawid, int(version)
