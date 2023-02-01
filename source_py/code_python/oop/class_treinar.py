#!/usr/bin/env python3

from sys import __stdin__

class myClass:

	cpfSize = 11
	name = "ramon"	

	def __init__(self, cpf, nome):
		self.cpf = cpf
		self.nome = nome
		self.dado_in = None

	def valida_cpf(self):
		if len(self.cpf) == __class__.cpfSize:
			return True
		else:
			return False

	@classmethod
	def name_dev(cls):
		return print(f"{cls.name}")

	def __str__(self):
		return f"cpf deste cliente {self.cpf}"

	def __getitem__(self, item):
		return self.nome[item]

	def __len__(self):
		return len(self.nome)

	def __stdin__(self):
		return stdin.readline()
