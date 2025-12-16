# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 23:57:03 2025

@author: youse
"""

import pandas as pd 


class Storage:
    
    def __init__(self, config):
        self.backend = config["storage_backend"]
        self.paths = config["paths"]
        
    def save(self, df, name):
        if self.backend == "parquet":
            df.to_parquet(self.paths["processed"] + f"{name}.parquet")
        elif self.backend == "postgis":
            # future load into database
            pass
        
    def load(self, name):
        if self.backend == "parquet":
            return pd.read_parquet(self.paths["processed"] + f"{name}.parquet")