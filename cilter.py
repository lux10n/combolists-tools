#!/usr/bin/python3
"""
    Extract email from combos and sort by domain
    Coded by m1ck-t3sla
"""
import os
from os import system
from sys import argv

types=[]
os.mkdir("Domains")
def getmail(combo):
    mail=combo.split(':')[0]
    return mail
def gettype(combo):
    return getmail(combo).split('@')[1]
def sort(combo):
    if gettype(combo) in types:
        with open('Domains/'+gettype(combo)+'.txt', 'a') as out:
            out.write(getmail(combo)+'\n')
    elif gettype(combo) not in types:
        types.append(gettype(combo))
        sort(combo)
currfile=argv[1]
combolist=open(currfile,'r').read().split('\n')
try:
    combolist.remove('')
except ValueError:
    pass
for combo in combolist:
    if "@" in combo:
        sort(combo)
    else:
        pass
