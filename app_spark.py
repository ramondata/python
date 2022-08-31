#!/usr/bin/env python3

import connect_spark
from connect_spark import session

def main(object_name):
	object_name.open_session()
	object_name.read_file("/Users/ramon/Documents/Dados/ovni.csv")
	object_name.show(35)

if(__name__ == "__main__"):
	a = session()
	main(a)
	
