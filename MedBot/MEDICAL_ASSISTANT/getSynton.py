# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
def getDeases(sym1,sym2):
    df = pd.read_csv('final dataset.csv', engine='python')
    df1 = df['DESEASE'][df['SYMTOM'].str.contains(sym1) & df['SYMTOM'].str.contains(sym2) ]
    return list(df1)[0]


def getMedicine(des):
    df = pd.read_csv('DATASET.csv', engine='python')
    df1 = df['MEDICINE'][df['DISEASE']==des ]
    return list(df1)[0]
    
    
des = getDeases("cough","shortness of breath")

mdcn = getMedicine(des) 

print(mdcn)


    