\# NORI - Neighborhood Opportunity and Resilience Index (MVP) -> working title



-------------

**LEFT OFF HERE**

-------------

Add ACS features to methods-and-notes (maybe rename this to model feature notes)

!!!!!!!rerun all notebooks given new csv output paths

# recommended transforms
log_income = np.log1p(median_income)
log_density = np.log1p(pop_density)

questions:
	
	why log transforms?
	 why use pop 25+ for higher ed (instead of 21 and up)?


raster at high-res is causing memory issues. You can either do nested windowing, or resample the raster at a lower resolution (but still high enough to capture canopies). Pick your poison.

quick visualization, ensure it looks good, then move on to health outcomes prep


---------------

**IDEAS FOR LATER**

---------------

* **blacken scripts**


-----------------------

**KEEP IN MIND THROUGHOUT**

-----------------------


* pull requests
* update journal.md
* update running daily list below
* add documentation to top of files when creating new 
* THE LONGER YOU WAIT TO RENAME PROJECT, THE MORE PAINFUL THE REFACTORING
* Make sure any gpkg write includes a layer name



----------

**TODO TODAY**

----------

review todo.txt and add todo items for today below


[ ] ACS demographics
[ ] econ mobility model
[ ] handle missing values in modeling pipeline
[ ] tree canopy from raster data
[ ] skipped day 1.7, transit data
[ ] transit access + walkability (this will require revisiting skipped items)



use this for documentation:

what the feature is and what its not

“Tree canopy estimates are derived from NLCD 30m land cover data and primarily capture large contiguous forested areas. This metric likely underestimates fine-grained urban canopy such as street trees and small pocket parks.”

why this is still used

“NLCD was selected for nationwide consistency and reproducibility. While it underrepresents fine-scale urban canopy, it reliably captures larger forested areas and serves as a comparable baseline across geographies.”

can I replace this with a more fine-grained raster?

Yes, but its old - 2017. As long as you make note of this (see chat response for how to frame this). Here's the link:













