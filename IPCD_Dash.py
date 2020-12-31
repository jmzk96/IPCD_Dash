import pandas as pd
import numpy as np
import seaborn as sns
from dash.dependencies import Input, Output
import dash_table
import dash_core_components
import dash_html_components
import plotly.express as xp

#--------------------------------------------------------------------------------------------------------------------------------#
#Read Data
ipcd_2018 = pd.read_csv("IPCD_2018.csv",delimiter=",")

#Filter unwanted columns
unwanted = ["near_id_1","near_id_2","near_id_3","air_code","air_code2","bike_id","fac_id","amtrakcode","ferry_code","website"
           ,"point_lat","point_lon","cbsa_code","cbsa_type","source","notes","bike_sys_id","ferry_code","rail_id","bike_id",
            "longitude","latitude","point_id","metro_area"]
ipcd_2018.drop(columns=unwanted,inplace =True)

#Take cities of importance
states =["AZ","IL","NV","NC","OH","PA","WI"]


important_states_data = []

for i in ipcd_2018.values.tolist():
    for j in states:
        if j in i :
            important_states_data.append(i)

important_states_data = pd.DataFrame(important_states_data,columns = ipcd_2018.columns)
#--------------------------------------------------------------------------------------------------------------------------------#
