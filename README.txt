003_colour_magniyude.ipynb: 
- plot a couple of snapshots from the millennium simulation (galform) gonzalez2014, to be compared with vipers data.
- plot the transmission curves for the VIPERS filters and the filter which galform wants to reproduce
- establish a connection to the VIRGO database in order to perform queries interactively.

005_progenitor:
-plot the evolutionary track of a single galaxy in the colour-magnitude diagram. Using the GALFORM simulation and selecting of the progenitor of the galaxy with galaxyID =0. 
Remember that if you do the normal query from the Virgo database (GP2), this run from GalaxyID to LastProgenitorID and that includes all the galaxies who contributes to the merger tree. That query is saved in 'data'. 'data_30' instead is the same query but starting from GalaxyID=30. Instead if we select galaxies between GalaxyID and MainLeafID we obtain the evolution of just one 'branch' i.e. just the evolution of the main progenitor. That is what is saved in data_leaf.
