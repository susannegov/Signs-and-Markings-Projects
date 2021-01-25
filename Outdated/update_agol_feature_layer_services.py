# -*- coding: utf-8 -*-
"""
Created on Weds December 4 2019

author: Susanne Gov

This script will update the Bus lane retroreflectivity measurements layer 
available on ArcGIS Online. This is run on a daily basis to update the
ATTACHMENT_ID and MEASURE_ID columns for each new row from the related table.

Future update: Make the script flexible to any AGOL feature layer.

"""

# Packages I import
from arcgis.gis import GIS
from arcgis.features import FeatureLayer
import pandas as pd
import geopandas as gpd
# setup feature layer to update
# client_id='CrnxPfTcm7Y7ZGl7'
gis = GIS("https://austin.maps.arcgis.com/home/index.html")

url = r"https://services.arcgis.com/0L95CJ0VTaxqcmED/arcgis/rest/services/{}/FeatureServer/1"
feature_name = "Data_Tracker_Signs_Markings"
out_path = r"G:\ATD\Signs_and_Markings\MARKINGS\Markings WORK ORDERS"
shp_name = "markings_work_orders.shp"

fl = FeatureLayer(url.format(feature_name))

sdf =  pd.DataFrame.spatial.from_layer(fl)
print(sdf.head())

df = gpd.GeoDataFrame(sdf)
print(df)
#df.to_file(driver = 'ESRI Shapefile', filename = out_path + '//' + shp_name)

