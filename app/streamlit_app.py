# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 01:08:07 2025

@author: youse
"""

import streamlit as st
import geopandas as gpd 
import pandas as pd 

st.set_page_config(page_title="NORI - MVP", layout="wide")
st.title("NORI — Neighborhood Opportunity & Resilience Index (MVP)")
st.sidebar.markdown("## Controls")
st.sidebar.selectbox("Map layer", ["Health Risk", "Mobility", "Econ Forecast"])
st.map()  # placeholder; will load precomputed geodataframe
st.write("This is the starting skeleton. Models and assets load from /models and /data/processed.")