#!/usr/bin/env python3

import csv
import json

arq: None = open("/Users/ramon/Documents/my_csv.csv", "r")

_to_csv: list = csv.reader(arq, delimiter=";")

js = {}

arq_j = open("/Users/ramon/Documents/js.json", "w")


for line in _to_csv:
    js["%s" % line[0]] = {"coluna": "%s" % line[1], "type": "%s" % line[2], "comentario": "%s" % line[3]}

arq_j.write(json.dumps(js))

arq_j.close()

arq_j = open("/Users/ramon/Documents/js.json", "r")

j = json.load(arq_j)

print(j["1"]["coluna"])

print(j.keys())

print(j.values())

#for line in j:
    #print("coluna {j[]coluna} e type {type} e comentario {comentario}".format_map(line))
