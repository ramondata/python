#!/usr/bin/env python3

import sys
import os
import calendar

class words:

	def __init__(self,a):
		self.__a = a

	@property
	def a(self):
		return self.__a

	def print(self):
		sys.stdout.write(self.__a)

	def print_vertical(self):
		for char in self.__a:
			print(f'{char}\n')

	@staticmethod
	def dev():
		return print('ramon barbosa')
