# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
Date: August 28, 2022                         "
Title: Cross-Border Payments WG Dashboard     "
Author: bocrodh                               "
"""""""""""""""""""""""""""""""""""""""""""""""

#Import libraries 
import pandas as pd 
import streamlit as st
import plotly.graph_objects as go


#Create blank webpage 
st.set_page_config(page_title="Main CB dashboard", 
                  page_icon=":money_with_wings:", 
                  layout="wide" 
                  ) 

#Reading Main CB Dashboard tab from workbook 
url = (r'https://github.com/bocrodh/xb_payment_WG_dashboard/blob/main/CB%20BB%20Dashboard%20for%20Canada%20(September%202022).csv?raw=true')
df = pd.read_csv(url)

#Formatting dataframe
df = df.drop_duplicates(keep='first') 
df = df[~df['Name of BB'].isnull()]   
df = df.fillna('')


#Filters
st.sidebar.header("Please Filter Here:") 
bb_number = st.sidebar.multiselect( 
    "BB Number:",  
    options=df["BB Number"].unique(), 
    default=df['BB Number'].unique(),
)  


position = st.sidebar.multiselect( 
    "Relative Position of Canada:",  
    options=df["Relative Position of Canada"].unique(), 
    default=df["Relative Position of Canada"].unique()
) 

links = st.sidebar.multiselect( 
    "Links with domestic Payments Modernization work:",  
    options=df["Links with domestic Payments Modernization work"].unique(), 
    default=df["Links with domestic Payments Modernization work"].unique()
) 

df_selection = df.query( 
    "`BB Number` ==@bb_number & `Relative Position of Canada`==@position & `Links with domestic Payments Modernization work`==@links" 
) 

#st.dataframe (df_selection) 
filtered = st.multiselect("Filter fields", options=df_selection.columns)

fig = go.Figure(data=[go.Table(
    header=dict(values=list(filtered),
                fill_color='darkcyan',
                align='center', 
                font=dict(color='white', size=15)),
    cells=dict(values=[df_selection[col] for col in filtered],
               fill_color='lavender',
               align='center'))
])

fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}, height=800)

st.plotly_chart(fig, use_container_width=True)

