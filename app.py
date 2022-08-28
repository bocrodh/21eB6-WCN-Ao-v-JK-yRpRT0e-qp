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

#Filters
st.sidebar.header("Please Filter Here:") 
bb_number = st.sidebar.multiselect( 
    "Building Block Number:",  
    options=df["Building Block Number"].unique(), 
    default=df['Building Block Number'].unique(),
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


filtered = st.multiselect( 
    "Filter fields", 
    options=list(df.columns)
)

df_selection = df.query("`Name of BB` ==@bb_number & `Relative Position of Canada`==@position & `Links with domestic Payments Modernization work` ==@links") 

#Formatting table
fig = go.Figure(data=[go.Table(
    header=dict(values=list(df_selection.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=df_selection.transpose().values.tolist(),
               fill_color='lavender',
               align='left'))])
                

  filtered = st.multiselect("Filter fields", options=list(df_selection.columns), default=list(df_selection.columns))
st.write(df_selection[filtered], 1200, 700) 
