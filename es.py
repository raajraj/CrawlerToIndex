from datetime import datetime
from elasticsearch import Elasticsearch
import os

# command to start Elastic Search
startES = "curl -u elastic:M77LQYm5A0S28md0CVfOWaqY https://final172.es.eastus2.azure.elastic-cloud.com:9243"
os.system(startES)

indexName = input("\nWhat do you want to name your index? ")
print("\n\n")

def getIndexName():
    return indexName

# command to make a new index
makeIndex = """curl -X PUT -u elastic:M77LQYm5A0S28md0CVfOWaqY "https://final172.es.eastus2.azure.elastic-cloud.com:9243/""" + indexName + """?pretty" -H 'Content-Type: application/json' -d'
{"settings": {
    "analysis": {
      "analyzer": {
        "htmlStripAnalyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": ["lowercase"],
          "char_filter": [ "html_strip" ]
        }
      }
    }
  },"mappings": {
      "properties": {
        "html": {
          "type": "text",
          "analyzer": "htmlStripAnalyzer"
        }
      }
  }
}'"""

# command to bulk load
bulkLoad = """curl -X POST -u elastic:M77LQYm5A0S28md0CVfOWaqY "https://final172.es.eastus2.azure.elastic-cloud.com:9243/""" + indexName + """/_bulk" -H "Content-Type: application/x-ndjson" --data-binary @output.json"""

# command to match all queries
matchAll = """curl -X GET -u elastic:M77LQYm5A0S28md0CVfOWaqY "https://final172.es.eastus2.azure.elastic-cloud.com:9243/""" + indexName + """/_search?pretty" -H 'Content-Type: application/json' -d' {
  "query": {
    "match_all": { }
  }
}'"""
print("----------------------------------------------------------------------")
print("Making new index named " + indexName + "...")
print("----------------------------------------------------------------------")
os.system(makeIndex)
print("----------------------------------------------------------------------")
print("Bulk loading .json file...")
print("----------------------------------------------------------------------")
os.system(bulkLoad)
print("\n----------------------------------------------------------------------")
print("Printing all queries...")
print("----------------------------------------------------------------------")
os.system(matchAll)
