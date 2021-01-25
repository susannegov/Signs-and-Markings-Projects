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

# setup feature layer to update
gis = GIS("https://austin.maps.arcgis.com/home/index.html", 
          client_id='CrnxPfTcm7Y7ZGl7')
url = r"https://services.arcgis.com/0L95CJ0VTaxqcmED/arcgis/rest/services/{}"
feature_name = "Bus_Lane_Retroreflectivity_Measurements"
fl = url.format(feature_name + r"/FeatureServer")
folder = r"G:\ATD\Signs_and_Markings\MARKINGS\Red Bus Lane Pictures"
bus = FeatureLayer(fl,gis)
bus.export_attachments(folder,"ATTACHMENT_ID")