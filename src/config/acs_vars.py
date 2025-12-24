# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 21:43:17 2025

@author: youse
"""

ACS_VARS = {
    
    # --- Population ---
    "B01003_001E": "total_population",

    # --- Income & Inequality ---
    "B19013_001E": "median_household_income",
    "B19083_001E": "gini_index",

    # --- Poverty ---
    "B17001_001E": "population_poverty_universe",
    "B17001_002E": "population_below_poverty",

    # --- Employment ---
    "B23025_003E": "labor_force",
    "B23025_005E": "unemployed_population",

    # --- Education (25+) ---
    "B15003_001E": "population_25_plus",
    "B15003_022E": "bachelors_degree",
    "B15003_023E": "masters_degree",
    "B15003_024E": "professional_degree",
    "B15003_025E": "doctorate_degree",

    # --- Housing ---
    "B25003_001E": "occupied_housing_units",
    "B25003_003E": "renter_occupied_units",

    # --- Rent ---
    "B25064_001E": "median_gross_rent",

    # --- Housing Cost Burden (Renters) ---
    "B25070_001E": "rent_burden_universe",
    "B25070_007E": "rent_30_to_34_pct_income",
    "B25070_008E": "rent_35_to_39_pct_income",
    "B25070_009E": "rent_40_to_49_pct_income",
    "B25070_010E": "rent_50_plus_pct_income",

    # --- Vehicle Access ---
    "B25044_001E": "vehicle_availability_universe",
    "B25044_003E": "households_no_vehicle",

    # --- Crowding ---
    "B25014_005E": "renter_crowded_units",

    # --- Age (65+) ---
    "B01001_020E": "male_65_66",
    "B01001_021E": "male_67_69",
    "B01001_022E": "male_70_74",
    "B01001_023E": "male_75_79",
    "B01001_024E": "male_80_84",
    "B01001_025E": "male_85_plus",
    "B01001_044E": "female_65_66",
    "B01001_045E": "female_67_69",
    "B01001_046E": "female_70_74",
    "B01001_047E": "female_75_79",
    "B01001_048E": "female_80_84",
    "B01001_049E": "female_85_plus",

    # --- Disability ---
    "B18101_001E": "disability_universe",
    "B18101_002E": "male_with_disability",
    "B18101_003E": "male_without_disability",
    "B18101_004E": "female_with_disability",
    "B18101_005E": "female_without_disability"
}