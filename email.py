#!/usr/bin/python3
"""
    Extract email from combos using regex
    Coded by m1ck-t3sla
"""
import re
from os import system as sys
from sys import argv
def rewrite(file):
    sF = open(file)
    mailP = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9.-]+')
    sF = mailP.findall(sF.read())
    lenC = len(sF)
    with open(file+'tmp','a') as new:
        for i in range(lenC):
            new.write("\n"+str(sF[i]))
try:
    rewrite(argv[1])
    sys("mv "+argv[1]+"tmp "+argv[1])
except Exception as e:
    print("Error : {}".format(str(e))

