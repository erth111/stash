import json
from pprint import pprint

with open('json.json') as f:
  data = json.load(f)

for x in range(0, len(data)):
  list = data[x]['requested_reviewers']
  for y in range(0, len(list)):
    pprint(list[y]['login'])
