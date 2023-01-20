#!/usr/bin/env python3

import connect_spark
from connect_spark import session
from sys import argv
from sys import stdin
from sys import stdout

arq = argv[1]

def main(object_name):
	object_name.open_session()
	object_name.read_file(f"/Users/ramon/Documents/Dados/{arq}")
	stdout.write(f"{object_name.cols()}\n")
	object_name.set_choose()
	object_name.show(35)
	col = object_name.choose[:-1]
	object_name.agrupa_conta(f"{col}")
	object_name.show_grupo(40)

if(__name__ != "__main__"):
	pass
else:
	obj1 = session()
	main(obj1)
	
