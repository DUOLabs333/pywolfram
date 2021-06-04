#!/usr/bin/env python
from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wlexpr
import readline

count=0

session=WolframLanguageSession('/cygdrive/c/Users/School/Downloads/Mathematica/WolframKernel.exe')
session.start()
session.evaluate(wlexpr('D[x^2,x]'))
print('\nWolfram Language 12.2.0 Engine for Microsoft Windows (64-bit)\n Copyright 1988-2021 Wolfram Research, Inc.\n')
try:
    while True:
        expr='ToString['+input('In['+str(count)+']:= ')+',InputForm]'
        print('Out['+str(count)+']= '+str(session.evaluate(wlexpr(expr))))
        print()
        count+=1
except KeyboardInterrupt:
    print()
    session.terminate()
    exit()
