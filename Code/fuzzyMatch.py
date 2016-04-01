#!/usr/bin/env python
#-*- coding: utf-8 -*-

from fuzzywuzzy import process
import pandas as pd


def fuzzyMatch(ser1, ser2):
    '''
    creates comparison/merge connector dataframe
    '''
    df = pd.Dataframe(ser1)
    df.columns = [ 'key1' ] 
    df['try'] = df.key1.apply(lambda x: process.extractOne(x, ser2.tolist()))

    df['ratio'] = df['try'].str.get(1)
    df['name'] = df['try'].str.get(0)
    print df.ratio.describe()
    return df
