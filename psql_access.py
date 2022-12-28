#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import psycopg2 as pg
import pandas as pd
import csv

list_data = list()

with open('/Users/ramon/Documents/indicadores_financeiros.csv', 'r') as arq:
    data = csv.reader(arq)
    list_data = [line for line in data]


cab = list('%s' % list_data[0])
del list_data[0]
print(list_data)




host='localhost'
port='5432'
dbname='ramon'
user='postgres'
#password='1234'
tbname = 'aanx'
connection = pg.connect("host='{}' port='{}' dbname='{}' user='{}'"
                        .format(host, port, dbname, user))
#df = pd.read_sql_query("insert into {} values (4,40)".format(tbname), con=connection)
#df.info()
