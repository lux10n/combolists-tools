#!/usr/bin/python3
from sys import argv
from os import system
import re
script , combo_file , ex_file = argv
cfile = open(combo_file,'r',encoding='utf8',errors='ignore')
system("./convert "+combo_file)
xfile = open(ex_file, 'w')
def rexmail(cfile):
	rexmail = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9.-]+:[a-zA-Z0-9._-]+')
	cfile = rexmail.findall(cfile.read())
	lenofclist = len(cfile)
	for i in range(lenofclist):
		xfile.write("\n")
		xfile.write(str(cfile[i]))
	print("[-]Done.[-]\n")
	print("[-]Check "+ex_file+" for results. [+]\n")
def header():
	print('''
			made by m1ckT3sl4 °_°
 
                           email:pass extractor from any txt file .
		''')

header()
rexmail(cfile)

