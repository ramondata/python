#!/usr/bin/env python3

import connect_spark
from connect_spark import session
from sys import argv
arq = argv[1]
def main(object_name):
	object_name.open_session()
	object_name.read_file(f"/Users/ramon/Documents/Dados/{arq}")
	object_name.show(35)

if(__name__ != "__main__"):
	pass
else:
	obj1 = session()
	main(obj1)
	
