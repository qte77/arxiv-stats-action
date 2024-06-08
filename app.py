from util import get_api_response, get_parsed_output
from csv import writer
from os import getenv, makedirs
from os.path import exists, dirname

CSV_FILE = getenv("CSV_FILE")
TOPICS = getenv("TOPICS")
ADD_URL = getenv("ADD_URL")
BASE_URL = getenv("BASE_URL")
START_RESULT = int(getenv("START_RESULT"))
END_RESULT = int(getenv("END_RESULT"))
MAX_RESULTS_PER_QUERY = int(getenv("MAX_RESULTS_PER_QUERY"))

TOPICS_REPL_STR = "#TOPICS#"
MAXRES_REPL_STR = "#MAXRES#"
STARTRES_REPL_STR = "#STARTRES#"

# https://github.com/karpathy/arxiv-sanity-lite/blob/d7a303b410b0246fbd19087e37f1885f7ca8a9dc/aslite/arxiv.py#L15
# https://info.arxiv.org/help/api/user-manual.html
# sortOrder=descending
add_url = ADD_URL.replace(TOPICS_REPL_STR, TOPICS).replace(MAXRES_REPL_STR, str(MAX_RESULTS_PER_QUERY))
search_query = BASE_URL + add_url

if not exists(CSV_FILE):
  # folder needs to exist before open() context
  makedirs(dirname(CSV_FILE), exist_ok=True)
  header = ["published", "updated", "id", "version", "title"]
  print(f"{header}")
  with open(CSV_FILE, 'w+', newline='', encoding='UTF8') as f:
    csv.writer(f).writerow(header)

for k in range(START_RESULT, START_RESULT + END_RESULT, MAX_RESULTS_PER_QUERY):
  search_query_k = search_query.replace(STARTRES_REPL_STR, str(k))
  response = get_api_response(search_query_k)
  out = get_parsed_output(response)
  with open(CSV_FILE, 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    for o in out:
      writer.writerow(o)
