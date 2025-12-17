\# NORI - Neighborhood Opportunity and Resilience Index (MVP) -> working title



-------------

**LEFT OFF HERE**

-------------



keep moving forward, but don't completely forget skipped items. 



finished distance\_to\_parks and park\_area\_<within buffer>



Go back and just QA check these to ensure they are calculating what is expected, then proceed with raster feature engineering



Something to keep in mind -> buffer intersections are from the buffer of tract centroids, not tract edges. Weigh pros and cons of each approach, and whatever you go with, document this in model feature notes





---------------

**IDEAS FOR LATER**

---------------



* **blacken scripts**
* **remove organizing from your portfolio. Reframe as equitable social development**





-----------------------

**KEEP IN MIND THROUGHOUT**

-----------------------



* pull requests
* update journal.md
* update running daily list below
* add documentation to top of files when creating new 
* THE LONGER YOU WAIT TO RENAME PROJECT, THE MORE PAINFUL THE REFACTORING
* Make sure any gpkg write includes a layer name



--------------------

**SKIPPED COME BACK TO**

--------------------



Day 1

* skipped day 0, repo skeleton and such - probz v important
* skipped day 1.4, acs demo bc multiple files
* skipped day 1.7, transit 



Day 2

* because of not having the data from day 1, also skipped corresponding notebooks in day 2
* loading opp atlas in python requires polar (alt to pandas for large dfs) (notebook 03)
* master\_table does not have columns that will come from the above skipped data



----------

**TODO TODAY**

----------





overall goal: single tract-level table with geographic features



1. XX distance to nearest park
2. XX park area within buffers
3. tree canopy from raster data
4. transit access + walkability (this will require revisiting skipped items)











Day 0:

&nbsp;	repo scaffold and environment setup



Day 1: 

&nbsp;	downloaded raw data from sources



Day 2:

&nbsp;	prepare raw data (extract, filter for nyc tracts)



Day 3:

&nbsp;	feature engineering











