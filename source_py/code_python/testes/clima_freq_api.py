#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os
import pandas as pd
from os.path import join
from datetime import datetime, timedelta

data_inicio = datetime.today().strftime('%Y-%m-%d')
data_fim = (datetime.today() + timedelta(days=7)).strftime('%Y-%m-%d')
city = 'Boston'
key = '3CAZUUFW52FH2SSQNAA6KP3ZH'

URL = join("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/",
          f"{city}/{data_inicio}/{data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv")

dados = pd.read_csv(URL)
print(dados.head())

file_path = f'/Users/ramon/Documents/datapipeline/semana={data_inicio}/'
os.mkdir(file_path)

dados.to_csv(file_path + 'dados_brutos.csv')
dados[['datetime','tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv')
dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')
