#!/usr/bin/python3
import os

#Default

os.chdir('Domains')
os.mkdir('inf')
file_list=os.listdir('.')
types=[]

#get domain type

def Dom(ml):
	ml=ml.replace('.txt','') #gmail.com
	mlF=ml.split('.') # ['gmail','com']
	try: mlF.remove('')
	except: pass
	mlForm=mlF[-1] # 'com'
	return mlForm

#get len on maillist

def gelLen(ml):
	return len(open(ml).read().split('\n'))

#filter by country

def sort(ml):	#gmail.com.txt
	if Dom(ml) in types:
		os.system('mv '+ml+' '+mlForm+'/')
	else:
		os.mkdir(Dom(ml))
		types.append(ml)
		sort(ml)

#main

for file in file_list:
	try: sort(file)
	except Exception as e: print(e)
