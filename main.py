#!/usr/bin/env python
import os
from flask import *
import sys
import webbrowser
from flask import Flask, render_template, request

print("\n-----------------------------WELCOME----------------------------\n")
pages = input("Enter the amount of pages you want to crawl: ")
hops = input("Enter the amount of hops you want each page to crawl: ")

os.system('python3 crawler.py seed.txt {} {} output.json'.format(pages, hops))

print("\n---------------------STARTING ELASTIC SEARCH---------------------\n")

import es

indexName = es.getIndexName()
scores = """curl -X GET -u elastic:M77LQYm5A0S28md0CVfOWaqY "https://final172.es.eastus2.azure.elastic-cloud.com:9243/""" + indexName+ """/_doc/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "size": 10,
  "sort": [
     "_score"
  ]
}
' > scoring.txt"""

from tkinter import *

root = Tk()
fram = Frame(root)
Label(fram,text='Your Index:').pack(side=LEFT)
edit = Entry(fram)
edit.pack(side=LEFT, fill=BOTH, expand=1)
edit.focus_set()
butt = Button(fram, text='Search')
butt.pack(side=RIGHT)
butt2 = Button(fram, text='Find')
butt2.pack(side=RIGHT)
fram.pack(side=TOP)
  
text = Text(root)
text.pack(side=BOTTOM)

os.system(scores)
f = open('scoring.txt')
line = f.readline()
while line:
    if("_id" in line):
        line = line.split()
        text.insert(1.0, line[2] + "\n")
    line = f.readline()
text.insert(1.0, "Ranked Documents\n")

def display(s):
    query = """curl -X GET -u elastic:M77LQYm5A0S28md0CVfOWaqY "https://final172.es.eastus2.azure.elastic-cloud.com:9243/""" + indexName + """/_search?pretty" -H 'Content-Type: application/json' -d' {
   "query": {
     "match": {
          "html": """ + '"' + s + '"' + """
 }
}
}' > query.txt"""

    os.system(query)
    os.system("python3 filterQuery.py > sample.txt")
    f = open('sample.txt')
    result = f.readlines()
    p = 1.0
    text.insert(p, s + "\n\n\n\n\n")
    text.insert(p, result)
    text.pack(side=BOTTOM)

def displayF(s):
    query = """curl -X GET -u elastic:M77LQYm5A0S28md0CVfOWaqY "https://final172.es.eastus2.azure.elastic-cloud.com:9243/""" + indexName + """/_search?pretty" -H 'Content-Type: application/json' -d' {
   "query": {
     "match": {
          "html": """ + '"' + s + '"' + """
 }
}
}' > Squery.txt"""

    os.system(query)
    f = open('Squery.txt')
    result = f.readlines()
    p = 1.0
    text.insert(p, result)
    text.pack(side=BOTTOM)

def search():
      
    text.tag_remove('found', '1.0', END)
    s = edit.get()
    if s:
        display(s)
        idx = '1.0'
        while 1:
            idx = text.search(s, idx, nocase=1,
                              stopindex=END)
            if not idx: break
            lastidx = '%s+%dc' % (idx, len(s))
            text.tag_add('found', idx, lastidx)
            idx = lastidx
        text.tag_config('found', foreground='red')
    edit.focus_set()

def find():
      
    text.tag_remove('found', '1.0', END)
    s = edit.get()
    if s:
        displayF(s)
        idx = '1.0'
        while 1:
            idx = text.search(s, idx, nocase=1,
                              stopindex=END)
            if not idx: break
            lastidx = '%s+%dc' % (idx, len(s))
            text.tag_add('found', idx, lastidx)
            idx = lastidx
        text.tag_config('found', foreground='red')
    edit.focus_set()
butt.config(command = search)
butt2.config(command = find)
root.mainloop()
