# -*- coding: utf-8 -*-
"""
Class of GIS features from the attribute table converted into a dataframe

Created on Mon Sep  9 11:13:09 2019

@author: Govs
"""

import pandas as pd

class GISFeatures:
    def __init__(self,in_tbl):
        self.in_tbl = in_tbl
        
    def to_df(self):
        new_tbl=[]
        tbl = self.in_tbl.split('\t')
        cols = i = tbl.index('SHAPE *') + 1
        while i < len(tbl):
            try:
                temp = tbl[i].split(' ')
                tbl[i:i] = temp
                new_tbl.append(tbl[i - (cols - 1):i + 1])
                del tbl[i + 2]
                i += cols + 1
            except:
                break
        temp = pd.DataFrame(new_tbl[1:],columns=new_tbl[0])
        return temp

    