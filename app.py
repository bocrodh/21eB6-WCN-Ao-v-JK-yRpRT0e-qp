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
from PIL import Image
 
#Create blank webpage 
st.set_page_config(page_title="Cross-Border Payments WG dashboard", 
                  page_icon=":money_with_wings:", 
                  layout="wide", 
) 

#Reading Main CB Dashboard tab from workbook 
url = (r'https://github.com/bocrodh/xb_payment_WG_dashboard/blob/main/CB%20BB%20Dashboard%20for%20Canada%20(September%202022).csv?raw=true')
df = pd.read_csv(url)

#Formatting dataframe
df = df.drop_duplicates(keep='first') 
df = df[~df['Name of BB'].isnull()]   
df = df.fillna('')

#Filters
st.sidebar.header("Filter Criteria:") 

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

filtered = st.multiselect("Filter fields", options=df_selection.columns, default=['BB Number', 'Name of BB','Relative Position of Canada','Links with domestic Payments Modernization work'])

#Hyperlinks
st.sidebar.header("Useful Links:") 
planner_link = "https://tasks.office.com/BankofCanada.onmicrosoft.com/en-US/Home/Planner/#/plantaskboard?groupId=12185be2-5934-4383-a53c-1b41a10d5bc4&planId=4PAjzPLa2UChyp0AF-bvXn0AFp-h"
st.sidebar.write("[Planner](%s)" % planner_link) 
sharepoint_link = "https://bankofcanada.sharepoint.com/teams/Cross_border_Payments/Shared%20Documents/Forms/AllItems.aspx" 
st.sidebar.write("[Sharepoint Page](%s)" % sharepoint_link)

#Plotly Dataframe
fig = go.Figure(data=[go.Table(
    header=dict(values=list(filtered),
                fill_color='#293242',
                align='center', 
                font=dict(color='white', size=15)),
    cells=dict(values=[df_selection[col] for col in filtered],
               fill_color='#F6F5F0',
               align='center', 
               font=dict(color='black', size=13)))])

fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}, height=800)

st.plotly_chart(fig, use_container_width=True)

st.markdown(
    """
<style>
span[data-baseweb="tag"] {background-color: #7E7F7A !important;}
</style>
""",
    unsafe_allow_html=True,
)

#Image and Graphs 
img = Image.open("CPMI_BB.jpg") 
new_image = img.resize((400, 400))
st.image(new_image)

st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)
