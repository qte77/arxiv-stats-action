import utils
import csv
from os import getenv, makedirs
from os.path import exists, dirname
import urllib.request

CSV_FILE = getenv("CSV_FILE")
TOPICS = getenv("TOPICS")
START_RESULT = getenv("START_RESULT")
END_RESULT = getenv("END_RESULT")
ADD_URL = getenv("ADD_URL")
BASE_URL = getenv("BASE_URL")
MAX_RESULTS_PER_QUERY = getenv("MAX_RESULTS_PER_QUERY")

TOPICS_REPL_STR = "#TOPICS#"
MAXRES_REPL_STR = "#MAXRES#"
STARTRES_REPL_STR = "#STARTRES#"

if not exists(CSV_FILE):
  # folder needs to exist before open() context
  makedirs(dirname(CSV_FILE), exist_ok=True)
  header = ["published", "updated", "id", "version", "title"]
  print(f"{header}")
  with open(CSV_FILE, 'w+', newline='', encoding='UTF8') as f:
    csv.writer(f).writerow(header)

# https://github.com/karpathy/arxiv-sanity-lite/blob/d7a303b410b0246fbd19087e37f1885f7ca8a9dc/aslite/arxiv.py#L15
# https://info.arxiv.org/help/api/user-manual.html
# sortOrder=descending
add_url = ADD_URL.replace(TOPICS_REPL_STR, TOPICS).replace(MAXRES_REPL_STR, MAX_RESULTS_PER_QUERY)
search_query = BASE_URL + add_url

for k in range(START_RESULT, START_RESULT + END_RESULT, MAX_RESULTS_PER_QUERY):
  search_query_k = search_query.replace(STARTRES_REPL_STR, str(k))
  with urllib.request.urlopen(search_query_k) as url:
      response = url.read()
  if url.status != 200:
      print(f"arxiv did not return status 200 response")
  out = []
  parse = feedparser.parse(response)
  for e in parse.entries:
      j = encode_feedparser_dict(e)
      # extract / parse id information
      idv, rawid, version = parse_arxiv_url(j['id'])
      # TODO simplify title prep
      title = str(j['title'])
      for s in '\n\r\"\'':
          title = title.translate({ ord(s): None })
      title = f"'{title}'"
      out.append([
        j['published'], j['updated'],
        rawid, version, title                  
      ])
  with open(CSV_FILE, 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    for o in out:
      writer.writerow(o)
