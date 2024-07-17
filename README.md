# arxiv-papers-stats-log

Logs daily stats of papers submitted to [arxiv.org](https://arxiv.org/). Inspired by [stats@arxiv-sanity-lite.com](https://arxiv-sanity-lite.com/stats).

[![Update arxiv.org stats](https://github.com/qte77/arxiv-stats-action/actions/workflows/write-arxiv-stats.yml/badge.svg)](https://github.com/qte77/arxiv-stats-action/actions/workflows/write-arxiv-stats.yml)
[![CodeFactor](https://www.codefactor.io/repository/github/qte77/arxiv-stats-action/badge)](https://www.codefactor.io/repository/github/qte77/arxiv-stats-action)
[![CodeQL](https://github.com/qte77/arxiv-stats-action/actions/workflows/codeql.yml/badge.svg)](https://github.com/qte77/arxiv-stats-action/actions/workflows/codeql.yml)
[![Ruff](https://github.com/qte77/arxiv-stats-action/actions/workflows/ruff.yml/badge.svg)](https://github.com/qte77/arxiv-stats-action/actions/workflows/ruff.yml)
[![Open in Visual Studio Code](https://img.shields.io/static/v1?logo=visualstudiocode&label=&message=Open%20in%20Visual%20Studio%20Code&labelColor=2c2c32&color=007acc&logoColor=007acc)](https://open.vscode.dev/qte77/arxiv-stats-action)

<!--
[![Cirrus CI - Base Branch Build Status](https://img.shields.io/cirrus/github/qte77/arxiv-stats-action?logo=Cirrus-ci)](https://cirrus-ci.com/github/gte77/arxiv-stats-action)
[![wakatime](https://wakatime.com/badge/github/qte77/arxiv-stats-action.svg)](https://wakatime.com/badge/github/qte77/arxiv-stats-action)
-->

## Environment Variables

Used environment variables and their defaults.

```python
# workflow
APP_DIR  ('./app')
PY_VER  ('3.10')
# app
OUT_DIR ('./data')
TOPICS ('cat:cs.CV+OR+cat:cs.LG+OR+cat:cs.CL+OR+cat:cs.AI+OR+cat:cs.NE+OR+cat:cs.RO')
BASE_URL ('https://export.arxiv.org/api/query?')
ADD_URL ('search_query=#TOPICS#&start=#STARTRES#&max_results=#MAXRES#&sortBy=submittedDate')
START_RESULT (0)
END_RESULT (199)
MAX_RESULTS_PER_QUERY (100)
```

## Similar projects

- [monologg/nlp-arxiv-daily)](https://github.com/monologg/nlp-arxiv-daily), uses [pypi/arxiv.py](https://pypi.org/project/arxiv/) and [PwC API](https://arxiv.paperswithcode.com/api/v0/papers/).

## Further reading

- [Today, arXivLabs launched a new Code tab, a shortcut linking Machine Learning articles with their associated code](https://blog.arxiv.org/2020/10/08/new-arxivlabs-feature-provides-instant-access-to-code/), 2020-10-08
- [PapersWithCode API Documentation](https://paperswithcode-client.readthedocs.io/en/latest/index.html), [pypi/paperswithcode-client](https://pypi.org/project/paperswithcode-client/)
