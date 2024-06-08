import utils
if not exists("${{ env.CSV_FILE }}"):
  # folder needs to exist before open()
  makedirs(dirname("${{ env.CSV_FILE }}"), exist_ok=True)
  header = ["published", "updated", "id", "version", "title"] # ak: "time", "time_str"
  print(f"{header}")
  with open("${{ env.CSV_FILE }}", 'w+', newline='', encoding='UTF8') as f:
    csv.writer(f).writerow(header)
# https://github.com/karpathy/arxiv-sanity-lite/blob/d7a303b410b0246fbd19087e37f1885f7ca8a9dc/aslite/arxiv.py#L15
# https://info.arxiv.org/help/api/user-manual.html
# sortOrder=descending
add_url = "${{ env.ADD_URL }}".replace("#TOPICS#", "${{ env.TOPICS }}")
add_url = add_url.replace("#MAXRES#", "${{ env.MAX_RESULTS_PER_QUERY }}")
search_query = "${{ env.BASE_URL }}" + add_url
for k in range(
  ${{ env.START_RESULT }},
  ${{ env.START_RESULT }} + ${{ env.END_RESULT }},
  ${{ env.MAX_RESULTS_PER_QUERY }}
):
  search_query_k = search_query.replace("#STARTRES#", str(k))
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
  with open("${{ env.CSV_FILE }}", 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    for o in out:
      writer.writerow(o)
