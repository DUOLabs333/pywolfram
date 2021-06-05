#!/usr/bin/env python
from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wlexpr
import readline
Quit=['Quit','Quit[]', 'Exit', 'Exit[]']

count=0

session=WolframLanguageSession('/cygdrive/c/Users/School/Downloads/Mathematica/WolframKernel.exe')
session.start()
session.evaluate(wlexpr('Unprotect[Out];'))
print('\nWolfram Language 12.2.0 Engine for Microsoft Windows (64-bit)\n Copyright 1988-2021 Wolfram Research, Inc.\n')
try:
    while True:
        expr=input('In['+str(count)+']:= ')
        if expr in Quit:
            raise KeyboardInterrupt
        
        session.evaluate(wlexpr(f'$Line={count};'))
        
        result=session.evaluate(wlexpr('ToString['+expr+',InputForm]'))
        
        session.evaluate(wlexpr(f'Out[{count}]={result};'))
        
        print(f'Out[{count}]={result}\n')
        
        count+=1
except KeyboardInterrupt:
    print()
    session.terminate()
    exit()
