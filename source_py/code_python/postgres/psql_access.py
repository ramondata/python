#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import psycopg2 as pg
import pandas as pd
import csv

#-------------------------------- dados de insert:
list_data = list()

with open('/Users/ramon/Documents/indicadores_financeiros.csv', 'r') as arq:
    data = csv.reader(arq, delimiter=";")
    list_data = [line for line in data]

del list_data[0]
print(list_data)

#------------------------------------- select no postgresql:

host='localhost'
port='5432'
dbname='financas'
user='postgres'
#password='1234'
tbname = 'indicadores_fin'
connection = pg.connect("host='{}' port='{}' dbname='{}' user='{}'"
                        .format(host, port, dbname, user))
df = pd.read_sql_query("select * from {0}".format(tbname), con=connection)
df.info()

#------------------------------ insert no postgresql:

cursor = connection.cursor()

for a,b,c,d,e,f in list_data:    
    postgres_insert_query = """ INSERT INTO indicadores_fin (data, entrada, saida, saldo, investimento, patrimonio)
                             VALUES (%s,%s,%s,%s,%s,%s)"""
    record_to_insert = (a,b,c,d,e,f)
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()

#count = cursor.rowcount