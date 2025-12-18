# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 23:28:15 2025

@author: youse
"""

from dataclasses import dataclass

@dataclass 
class HealthIndicators:
    tract_id: str
    asthma: float
    diabetes: float
    mental_health: float  
    
@dataclass 
class GreenSpacePolygons: 
    geom: object 
    parm_name: str 
    area_m2: float