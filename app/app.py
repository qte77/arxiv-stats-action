import csv
from os import getenv, makedirs
from os.path import exists, dirname
from utils import get_api_response, get_parsed_output

OUT_DIR = getenv("OUT_DIR", './data')
TOPICS = getenv("TOPICS", 'cat:cs.CV+OR+cat:cs.LG+OR+cat:cs.CL+OR+cat:cs.AI+OR+cat:cs.NE+OR+cat:cs.RO')
BASE_URL = getenv("BASE_URL", 'https://export.arxiv.org/api/query?')
ADD_URL = getenv("ADD_URL", 'search_query=#TOPICS#&start=#STARTRES#&max_results=#MAXRES#&sortBy=submittedDate')
START_RESULT = getenv("START_RESULT", 0)
END_RESULT = getenv("END_RESULT", 19)
MAX_RESULTS_PER_QUERY = getenv("MAX_RESULTS_PER_QUERY", 10)

TOPICS_REPL_STR = "#TOPICS#"
MAXRES_REPL_STR = "#MAXRES#"
STARTRES_REPL_STR = "#STARTRES#"

HEADER = ["Published", "Weekday(Monday==0)", "Updated", "ID", "Version", "Title"]

# https://github.com/karpathy/arxiv-sanity-lite/blob/d7a303b410b0246fbd19087e37f1885f7ca8a9dc/aslite/arxiv.py#L15
# https://info.arxiv.org/help/api/user-manual.html
# sortOrder=descending
add_url_dyn = ADD_URL.replace(TOPICS_REPL_STR, TOPICS).replace(MAXRES_REPL_STR, str(MAX_RESULTS_PER_QUERY))
api_url = BASE_URL + add_url_dyn

for k in range(START_RESULT, START_RESULT + END_RESULT, MAX_RESULTS_PER_QUERY):
  api_url_k = api_url.replace(STARTRES_REPL_STR, str(k))
  response = get_api_response(api_url_k)
  out = get_parsed_output(response)
  for k in out.keys():
    out_file = f"{OUT_DIR}/{k}.csv"
    if not exists(out_file):
      # folder needs to exist before open() context
      makedirs(dirname(out_file), exist_ok=True)
      with open(out_file, 'w+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)
    with open(out_file, 'a+', newline='', encoding='UTF8') as f:
      writer = csv.writer(f)
      for o in out[k]:
        writer.writerow(o)
