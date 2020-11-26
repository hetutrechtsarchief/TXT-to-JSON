#!/usr/bin/env python3
import json,sys

emptylines=0
nr=0
items=[]
item=None

def fixLine(line):
  line = line.strip()
  line = line.replace('\xad', '') # soft hyphen: or use \u00ad or \N{SOFT HYPHEN}
  return line

def newItem(line):
  global item
  if item:
    items.append(item)
  item=[fixLine(line)]

def updateItem(line):
  global item
  item.append(fixLine(line))

###############

if len(sys.argv)<=1:
  print("Usage: ./txt2json.py INPUTFILE")
else:
  with open(sys.argv[1], mode="r") as file:
    for line in file:
      nr=nr+1

      if line.strip()=="": 
        emptylines=emptylines+1
      elif emptylines>=3:
        emptylines=0
        newItem(line)
      else:
        emptylines=0
        updateItem(line)  

  if item: # add the last one
    items.append(item)

  print(json.dumps(items, indent=4, ensure_ascii=False)) 

