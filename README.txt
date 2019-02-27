003_colour_magniyude.ipynb: 
- plot a couple of snapshots from the millennium simulation (galform) gonzalez2014, to be compared with vipers data.
- plot the transmission curves for the VIPERS filters and the filter which galform wants to reproduce
- establish a connection to the VIRGO database in order to perform queries interactively.

005_progenitor:
-plot the evolutionary track of a single galaxy in the colour-magnitude diagram. Using the GALFORM simulation and selecting of the progenitor of the galaxy with galaxyID =0. 
Remember that if you do the normal query from the Virgo database (GP2), this run from GalaxyID to LastProgenitorID and that includes all the galaxies who contributes to the merger tree. That query is saved in 'data'. 'data_30' instead is the same query but starting from GalaxyID=30. Instead if we select galaxies between GalaxyID and MainLeafID we obtain the evolution of just one 'branch' i.e. just the evolution of the main progenitor. That is what is saved in data_leaf.

006_save_progenitors: Actually it was born with the idea of just saving in a txt file all of the data coming from long queries but then I started doing tests on weird galaxies that are main leaves. Since I was going nowhere. I stopped the investigation and I came back to what I actually need in the VIPERS paper, in 007.

007_PROGENITOR_VIPERSLIKE: From the merger three of GALFORM Gonzalez+14 I selected the galaxies at the snapnum 47 that redshift araund z=0.46 (that I call descendants) and following the main branch of the merger three I selected the progenitor at redshift 1.1 (snap 47) that is the highest redshift bin tht I used in VIPERS. Since the query is very long and it reaches the timeout limit of 18000 seconds I only obtain few objects (1591) instead of about 3 millions. I will optimize the query following John Helly's advice in 008.

008_progenito_EDGE_egltools: In here I used a different package to query the database called eagleSqlTools (https://github.com/kyleaoman/eagleSqlTools) instead of the usual virgodb.py. But this doesn't change anything, it's just important because it can be run in COSMA while virgodb.py needs packages that are not present in cosma. By the way, virgodb.py can be find in the documentation webpage of the virgo database (http://virgodb.dur.ac.uk:8080/MyMillennium/Help?page=python/python). 
--> potential plot for the paper: histogram with threshold indicated,


Instead, what is very important in 008 is the new query provided by JOHN HELLY that is more efficient as it sorts the galaxyid in order to optimize the query. In this way I actuallty obtain 3 millions entry. I have also rewritten the algorithm to define the edge like in VIPERS paper. and I run it again both on VIPERS and GALFORM GP14.

In the meantime I also run the edge in ../../PAU/code/read_something.ipynb on the snapnum 37 and 47 without any contraints descendent/progenitor.v Just as they are. So that we can say this is like observations and instead the plot from 008 is how actually the same population of galaxies move.


009: Clean version of 008 I can read the fiole obtained from John Helly's query directly from a text file. Also, I applied to the colour magnitude the correct magnitude cuts at 22.5 (I use my COSMOLOGY functions to convert apparent in absolute magnitudes).

010: Something wrong with the i-band magnitude cut in the colour magnitude. Just ignore this notebook. I have done things correctly in cosma in ./galform/python/galform/read/Plot_colour_magnitude.ipynb. 

011: Very important because I'm doing all the plots in the VIPERS paper again.

014: I start working on the luminosity function coming from GALFORM in order to compare it to the luminosity function of VIPERS as comin from Fritz 2014. However I have just taken the important pieces of code and added to 011 (so that you can actually ignore 014).