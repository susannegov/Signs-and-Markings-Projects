# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "Operational_Maintenance_Areas_200grids", "ATD_ADMIN.markings_specialty_point"
fields = 'GRIDS_200_ID "GRIDS_200_ID" true true false 4 Long 0 0 ,First,' +
'#,Operational_Maintenance_Areas_200grids,GRIDS_200_ID,-1,-1;'+
'TILE_NAME "TILE_NAME" true true false 5 Text 0 0 ,First,#,' +
'Operational_Maintenance_Areas_200grids,TILE_NAME,-1,-1;' +
'DISTRICT_ID_1 "DISTRICT_ID_1" true true false 5 Text 0 0 ,First,' +
'#,Operational_Maintenance_Areas_200grids,DISTRICT_ID_1,-1,-1;' +
'DISTRICT_ID_2 "DISTRICT_ID_2" true true false 5 Text 0 0 ,' +
'First,#,Operational_Maintenance_Areas_200grids,DISTRICT_ID_2,-1,-1;' +
'DISTRICT_ID_3 "DISTRICT_ID_3" true true false 5 Text 0 0 ,First,#,' +
'Operational_Maintenance_Areas_200grids,DISTRICT_ID_3,-1,-1;' +
'REGULATORY_SIGN_COUNT "REGULATORY_SIGN_COUNT" true true false 4' +
' Long 0 0 ,First,#,Operational_Maintenance_Areas_200grids,' +
'REGULATORY_SIGN_COUNT,-1,-1;WARNING_SIGN_COUNT "WARNING_SIGN_COUNT" true' +
' true false 4 Long 0 0 ,First,#,Operational_Maintenance_Areas_200grids,' +
'WARNING_SIGN_COUNT,-1,-1;GUIDE_SIGN_COUNT "GUIDE_SIGN_COUNT" true true false'+
' 4 Long 0 0 ,First,#,Operational_Maintenance_Areas_200grids,GUIDE_SIGN_COUNT,' +
'-1,-1;TOTAL_SIGN_COUNT "TOTAL_SIGN_COUNT" true true false 4 Long 0 0 ,First,' +
'#,Operational_Maintenance_Areas_200grids,TOTAL_SIGN_COUNT,-1,-1;' +
'MAJORITY_DISTRICT "MAJORITY_DISTRICT" true true false 75 Text 0 0 ,First,' +
'#,Operational_Maintenance_Areas_200grids,MAJORITY_DISTRICT,-1,-1;SCHOOL_COUNT "SCHOOL_COUNT" true true false 5 Text 0 0 ,First,#,Operational_Maintenance_Areas_200grids,SCHOOL_COUNT,-1,-1;FY_GROUND_SIGN_MAINT "FY_GROUND_SIGN_MAINT" true true false 5 Text 0 0 ,First,#,Operational_Maintenance_Areas_200grids,FY_GROUND_SIGN_MAINT,-1,-1;SHAPE_Length "SHAPE_Length" false true true 8 Double 0 0 ,First,#,Operational_Maintenance_Areas_200grids,SHAPE_Length,-1,-1;SHAPE_Area "SHAPE_Area" false true true 8 Double 0 0 ,First,#,Operational_Maintenance_Areas_200grids,SHAPE_Area,-1,-1;OMA_ID "OMA_ID" true true false 2 Short 0 0 ,First,#,Operational_Maintenance_Areas_200grids,OMA_ID,-1,-1;CROSSWALK_COUNT_CBD "CROSSWALK_COUNT_CBD" true true false 4 Long 0 0 ,First,#,Operational_Maintenance_Areas_200grids,CROSSWALK_COUNT_CBD,-1,-1;CROSSWALK_COUNT_SIGNAL "CROSSWALK_COUNT_SIGNAL" true true false 4 Long 0 0 ,First,#,Operational_Maintenance_Areas_200grids,CROSSWALK_COUNT_SIGNAL,-1,-1;CROSSWALK_COUNT_SCHOOL "CROSSWALK_COUNT_SCHOOL" true true false 4 Long 0 0 ,First,#,Operational_Maintenance_Areas_200grids,CROSSWALK_COUNT_SCHOOL,-1,-1;CROSSWALK_COUNT_OTHER "CROSSWALK_COUNT_OTHER" true true false 4 Long 0 0 ,First,#,Operational_Maintenance_Areas_200grids,CROSSWALK_COUNT_OTHER,-1,-1;TOTAL_CROSSWALK_COUNT "TOTAL_CROSSWALK_COUNT" true true false 4 Long 0 0 ,First,#,Operational_Maintenance_Areas_200grids,TOTAL_CROSSWALK_COUNT,-1,-1;FY_CROSSWALK_CBD "FY_CROSSWALK_CBD" true true false 5 Text 0 0 ,First,#,Operational_Maintenance_Areas_200grids,FY_CROSSWALK_CBD,-1,-1;FY_CROSSWALK_SIGNAL "FY_CROSSWALK_SIGNAL" true true false 50 Text 0 0 ,First,#,Operational_Maintenance_Areas_200grids,FY_CROSSWALK_SIGNAL,-1,-1;FY_CROSSWALK_SCHOOL "FY_CROSSWALK_SCHOOL" true true false 50 Text 0 0 ,First,#,Operational_Maintenance_Areas_200grids,FY_CROSSWALK_SCHOOL,-1,-1;FY_CROSSWALK_OTHER "FY_CROSSWALK_OTHER" true true false 50 Text 0 0 ,First,#,Operational_Maintenance_Areas_200grids,FY_CROSSWALK_OTHER,-1,-1;Square_Miles "Square_Miles" true true false 8 Double 0 0 ,First,#,Operational_Maintenance_Areas_200grids,Square_Miles,-1,-1;SIGNAL_INTERSECTION_COUNT "SIGNAL_INTERSECTION_COUNT" true true false 8 Double 0 0 ,First,#,Operational_Maintenance_Areas_200grids,SIGNAL_INTERSECTION_COUNT,-1,-1;FY_OVERHEAD_SIGN_MAINT "FY_OVERHEAD_SIGN_MAINT" true true false 5 Text 0 0 ,First,#,Operational_Maintenance_Areas_200grids,FY_OVERHEAD_SIGN_MAINT,-1,-1;FY_SPECIALTY_CBD "FY_SPECIALTY_CBD" true true false 25 Text 0 0 ,First,#,Operational_Maintenance_Areas_200grids,FY_SPECIALTY_CBD,-1,-1;FY_SPECIALTY_SIGNAL "FY_SPECIALTY_SIGNAL" true true false 25 Text 0 0 ,First,#,Operational_Maintenance_Areas_200grids,FY_SPECIALTY_SIGNAL,-1,-1;FY_SPECIALTY_BIKE "FY_SPECIALTY_BIKE" true true false 25 Text 0 0 ,First,#,Operational_Maintenance_Areas_200grids,FY_SPECIALTY_BIKE,-1,-1;FY_SPECIALTY_OTHER "FY_SPECIALTY_OTHER" true true false 2 Short 0 0 ,First,#,Operational_Maintenance_Areas_200grids,FY_SPECIALTY_OTHER,-1,-1;SPECIALTY_COUNT_CBD "SPECIALTY_COUNT_CBD" true true false 50 Long 0 0 ,Count,#;SPECIALTY_COUNT_SIGNAL "SPECIALTY_COUNT_SIGNAL" true true false 50 Long 0 0 ,Count,#;SPECIALTY_COUNT_BIKE "SPECIALTY_COUNT_BIKE" true true false 50 Long 0 0 ,Count,#;SPECIALTY_COUNT_OTHER "SPECIALTY_COUNT_OTHER" true true false 50 Long 0 0 ,Count,#', 


arcpy.SpatialJoin_analysis(target_features="Operational_Maintenance_Areas_200grids",
join_features="ATD_ADMIN.markings_specialty_point",
out_feature_class="G:/ATD/ATD_GIS/Markings/map_data/Markings.gdb/OMA_200_GRID_MAINTENANCE",
join_operation="JOIN_ONE_TO_ONE",
join_type="KEEP_ALL",
field_mapping=
match_option="COMPLETELY_CONTAINS",
search_radius="", distance_field_name="")
