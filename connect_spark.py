#!usr/bin/env python3
# -*- encoding:utf-8 -*-

import pyspark
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import*
from pyspark.sql.types import*
from sys import stdin
from sys import stdout



class session:

	def __init__(self):
		self.__sc = None
		self.__spark = None
		self.__dado = None
		self.__agrupado = None
		self.__cols = None
		self.__choose = None

	def open_session(self):
		self.__sc = SparkContext()
		self.__spark = SQLContext(self.__sc)

	def read_file(self, path):
		self.__dado = self.__spark.read\
			.option("header", "true")\
			.option("delimiter", ";")\
			.option("inferschema", "true")\
			.csv(path)
		return self.__dado

	def agrupa_conta(self, name_col):
		self.__agrupado = self.__dado.groupby(name_col).count()
		self.__agrupado = self.__agrupado.sort(col(name_col).asc())
		return self.__agrupado

	def cols(self):
		self.__cols = self.__dado.columns
		return self.__cols

	def show(self, limit):
		return self.__dado.show(limit, truncate=False)

	def show_grupo(self, limit):
		return self.__agrupado.show(limit, truncate=False)

	def set_choose(self):
		stdout.write("Escolha a coluna para agrupamento da análise\n")
		self.__choose = stdin.readline()

	@property
	def choose(self):
		return self.__choose
