# -*- coding: utf-8 -*-
"""

QA checks for data sources

Created on Mon Dec  8 23:21:02 2025
@author: youse
"""

from pathlib import Path
import geopandas as gpd
import pandas as pd


def basic_check(path):
    p = Path(path)
    if p.suffix in [".parquet", ".geojson", ".gpkg"]:
        g = gpd.read_file(path)
        print(path, " -> rows: ", len(g), " crs: ", g.crs)
    
    elif p.suffix in [".csv"]:
        df = pd.read_csv(path)
        print(path, " -> cols: ", df.columns.tolist())
    
    else:
        print("Uknown type ", path)
        

for f in Path("data/raw/").glob("*"):
    basic_check(str(f))
    
    
    
