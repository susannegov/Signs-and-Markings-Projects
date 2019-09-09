# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 16:06:16 2019

@author: Govs
"""

from arcgis.features import FeatureLayer

class FeatureLayerDataFrame:
    def __init__(self,name):
        self.name = name
        self.url = (r"https://services.arcgis.com/0L95CJ0VTaxqcmED/arcgis/rest/"
                    + r"services/TRANSPORTATION_{}/FeatureServer/0")
        self.fl = FeatureLayer(self.url.format(name))
    
    def query_segments(self,segments):
        try:
            q = "SEGMENT_ID IN({})".format(str(segments)[1:-1])
            sdf = self.fl.query(where=q).sdf
            if 'markings_specialty_point' in self.name:
                sdf = self.specialty_markings(sdf)
            return sdf
        except:
            pass

    def specialty_markings(self,df):
        field = 'SPECIALTY_POINT_TYPE'
        sub_field = 'SPECIALTY_POINT_SUB_TYPE'
        renameList = list(zip(list(df[field]),list(df[sub_field])))
        word = ["Stop","Yield","Ahead","Only","Merge","Ped", "X-ing","MPH",
                "Bus Only","Ped X-ing","Keep Clear","Do Not Block"]
        arrow = ["Through","Left","Right","Left/Right",
                 "Left/Right/Through","Left/Through","Right/Through",
                 "U-turn","Lane reduction","Wrong way","Bike"]
        other = ["Green pad", "Green launch pad", "Speed hump marking",
                 "Diagonal crosshatch", "Chevron crosshatch"]
        parking = ["Parking 'L'", "Parking 'T'", 
                   "Parking stall line", "Handicap symbol"]
        symbol = ["Bike","Shared lane (Sharrow)","Bicyclist",
                  "Railroad Crossing (RxR)","Chevron","Pedestrian","Diamond"]
        rpm = ['blue','']
        t =['word','arrow','symbol','','','rpm']
        st = [word,arrow,symbol,other,parking,rpm]
        index = 0
        for i in renameList:
            x = list(map(int,list(i)))
            temp = st[x[0] - 1][x[1] - 1] + " " + t[x[0] - 1]
            renameList[index] = temp
            index += 1
        df[field] = renameList
        return df.drop(sub_field,axis=1)
