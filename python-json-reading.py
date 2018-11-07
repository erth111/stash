#get list of logins that were requested a review on github
#input file example: https://api.github.com/repos/tensorflow/tensorflow/pulls

import json
from pprint import pprint

with open('json.json') as f:
  data = json.load(f)

for x in range(0, len(data)):
  list = data[x]['requested_reviewers']
  for y in range(0, len(list)):
    pprint(list[y]['login'])
