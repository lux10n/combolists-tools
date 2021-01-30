#!/usr/bin/python3
import os
	from os import chdir,mkdir,listdir,system
chdir('Domains')
try:mkdir('inf_200')
except:pass
def file_list():
	system("ls |grep '.txt' > .flist")
	l=open(".flist","r").read().split('\n')
	l.remove('')
	return l
types=[]
def getDom(fle):
	return fle.split('.')[-2]
def getLen(ml):
	a=open(ml,'r').read().split('\n')
	return len(a)
def sort(file):
	a=getDom(file)
	system('mkdir '+a)
	try:
		if a==types[-1]:
			system('mv '+file+' '+a+'/')
		else:
			types.append(a)
			sort(file)
	except IndexError:
		types.append(a)
		sort(file)
fl=file_list()
for file in fl:
	try:sort(file)
	except Exception as e: print(e)
