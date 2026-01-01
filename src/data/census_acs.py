# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 20:15:48 2025

@author: youse
"""

import os
import sys
import requests
import numpy as np
import pandas as pd
from pathlib import Path

sys.path.append(str(Path.cwd().parent))

from config.acs_vars import ACS_VARS

PATH_ACS = '../../data/raw/census_acs.csv' # TODO: handle this path more dynamically
API_KEY = os.getenv("CENSUS_API_KEY")
YEAR = 2023 # most recent ACS 5-year estimates 
VARS =  list(ACS_VARS.keys()) # see src/config/acs_vars for info about these variables
STATE = "36" # NY State
COUNTIES = ["005","047","061","081","085"]  # Bronx, Kings, New York, Queens, Richmond

# perform API request
url = f"https://api.census.gov/data/{YEAR}/acs/acs5"
params = {
    "get": ",".join(VARS),
    "for": "tract:*",
    "in": f"state:{STATE} county:{','.join(COUNTIES)}",
    "key": API_KEY
}

# get results from api request
resp = requests.get(url, params=params)

# store results as df
df_acs = pd.DataFrame(resp.json()[1:], columns=resp.json()[0])

# create geoid column (primary key for all other tables)
df_acs['GEOID'] = df_acs.state + df_acs.county + df_acs.tract

# ensure all GEOID's are 11 characters long
assert((df_acs['GEOID'].str.len() == 11).all())

# convert raw ACS variable names to human legible ones
df_acs.rename(columns=ACS_VARS, inplace=True)

# drop unneeded columns
df_acs.drop(columns=['state', 'county', 'tract'], inplace=True)

# missing values are stored as -666666666, convert these to nan
df_acs = df_acs.replace('-666666666', np.nan)
df_acs = df_acs.replace('-666666666.0000', np.nan)
df_acs = df_acs.astype(float)

# save results
df_acs.to_csv(PATH_ACS, index=False)