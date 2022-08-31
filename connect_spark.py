#!usr/bin/env python3

import pyspark
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import*
from pyspark.sql.types import*

class session:

	def __init__(self):
		self.__sc = None
		self.__spark = None
		self.__dado = None

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

	def show(self, limit):
		return self.__dado.show(limit, truncate=False)
