\# NORI - Neighborhood Opportunity and Resilience Index (MVP) -> working title


The goal is to be able to target and prioritize specific neighborhoods for interventions and developments in order to build more equitable socioeconomic outcomes for all. 
1. We identify which neighborhoods are doing well (the people are healthy, educated, and in good economic standing)
2. We identify which neighborhoods are not doing well (high disease prevalence, lack of economic mobility and opportunity).
3. We try and understand what the structural differences are between these neighborhoods that explain the different outcomes we are observing in their populations. 
4. We use this to design programs and interventions that will build a more equitable socioeconomic landscape, ensuring all tracts have at least a baseline level of health and opportunity, closing the gap between those doing well, and those left behind.   

-------------

**LEFT OFF HERE**

-------------

1. shap pipeline 
	answering questions about performance and feature importance between outcome models

**** ensure different kernel, ensure proper renaming of variables, restart kernel between runs to make sure, inspect new feature importance plots

2. Update health pipeline, side by side comparison bw health and mobility
3. quickly finish day 7 
	- nori index score
	- create map
	- create list of ranked tracts
4. Before moving on to causation, slap a bow on this phase of the project: NORI has been built. The rest is just add-ons (right chatgpt?). I believe you should include what you have so far into your portfolio to start applying for better jobs now, mentioning that the project is still evolving, and including a link to the repo and screenshot of map with ranked tract index next to it.

revisit fork in the road (where I decided to skip adding features to get pipeline moving) and see where to go from here

finish editing documentation above all ipynb's
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













