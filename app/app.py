import csv
from os import getenv, makedirs
from os.path import exists, dirname
from utils import get_api_response, get_parsed_output

OUT_FILE = getenv("OUT_FILE", 'data/data.csv')
TOPICS = getenv("TOPICS", 'cat:cs.CV+OR+cat:cs.LG+OR+cat:cs.CL+OR+cat:cs.AI+OR+cat:cs.NE+OR+cat:cs.RO')
BASE_URL = getenv("BASE_URL", 'http://export.arxiv.org/api/query?')
ADD_URL = getenv("ADD_URL", 'search_query=#TOPICS#&start=#STARTRES#&max_results=#MAXRES#&sortBy=submittedDate')
START_RESULT = getenv("START_RESULT", 0)
END_RESULT = getenv("END_RESULT", 19)
MAX_RESULTS_PER_QUERY = getenv("MAX_RESULTS_PER_QUERY", 10)

TOPICS_REPL_STR = "#TOPICS#"
MAXRES_REPL_STR = "#MAXRES#"
STARTRES_REPL_STR = "#STARTRES#"

HEADER = ["published", "updated", "id", "version", "title"]

# https://github.com/karpathy/arxiv-sanity-lite/blob/d7a303b410b0246fbd19087e37f1885f7ca8a9dc/aslite/arxiv.py#L15
# https://info.arxiv.org/help/api/user-manual.html
# sortOrder=descending
add_url_dyn = ADD_URL.replace(TOPICS_REPL_STR, TOPICS).replace(MAXRES_REPL_STR, str(MAX_RESULTS_PER_QUERY))
search_query = BASE_URL + add_url_dyn

if not exists(OUT_FILE):
  # folder needs to exist before open() context
  makedirs(dirname(OUT_FILE), exist_ok=True)
  with open(OUT_FILE, 'w+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(HEADER)

for k in range(START_RESULT, START_RESULT + END_RESULT, MAX_RESULTS_PER_QUERY):
  search_query_k = search_query.replace(STARTRES_REPL_STR, str(k))
  response = get_api_response(search_query_k)
  out = get_parsed_output(response)
  with open(OUT_FILE, 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    print(f"start output, {len(out)=}")
    for o in out:
      print(f"{len(o)=}, {o=}")
      print(o[2])
      # writer.writerow(o)
