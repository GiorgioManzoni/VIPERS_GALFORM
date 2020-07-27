import fase
import fase.fileio
import numpy as np
from fase.fileio import Table

from init import *  #init contains data about the definition of the edges

#IF IMPORTED, THIS PROGRAM LOADS DATA FROM VIPERS (BOLOGNA+GOSSIP+MATCH) AND FROM ZCOSMOS
#The object number indicated is relative to the full sample without considering np.where selections
#Table objects are deleted because there are problems in the importation process.
#Therefore if you want to extract others columns you have to do this here.

#_________________________________________________________________________________________________________
#18,143 objects
zcosmos = Table("./ZCOSMOS/absmags_zcosmos_bright4.2.dat")
cZ = zcosmos.getCol("2.ZSPEC")
cU = zcosmos.getCol("5.MU_JKC")
cV = zcosmos.getCol("7.MV_JKC")
cUV = cU-cV
good_mag = np.where(cV!=-99)
cZ = cZ[good_mag]
cU = cU[good_mag]
cV = cV[good_mag]
cUV = cUV[good_mag]
del zcosmos

#________________________________________________________________________________________________________
#98,739 objects
bologna = fase.fileio.Table("Data_Sample_V7.fits",hdu=4)
bZ = bologna.getCol("zspec")
bU = bologna.getCol("M_Uj")
bV = bologna.getCol("M_V")
bUV = bU-bV
bTAU = bologna.getCol("tau")
bAGE = bologna.getCol("age")
bmass = bologna.getCol("log_stellar_mass")

good_mag = np.where(bV!=-99)
bZ = bZ[good_mag]
bU = bU[good_mag]
bV = bV[good_mag]
bUV = bUV[good_mag]
bTAU = bTAU[good_mag]
bAGE = bAGE[good_mag]
bmass = bmass[good_mag]
del bologna

#________________________________________________________________________________________________________
#77,105 objects
gossip = fase.fileio.Table("Data_Sample_V7.fits",hdu=3)
gZ = gossip.getCol("Z")
gU = gossip.getCol("UJ_abs")
gV = gossip.getCol("VJ_abs")
gUV = gU-gV
gTAU = gossip.getCol("TAU")
gAGE = gossip.getCol("AGE")
gmass = gossip.getCol("STELLAR_MASS")

good_mag = np.where(gV!=-99)
gZ = gZ[good_mag]
gU = gU[good_mag]
gV = gV[good_mag]
gUV = gUV[good_mag]
gTAU = gTAU[good_mag]
gAGE = gAGE[good_mag]
gmass = gmass[good_mag]
del gossip

#________________________________________________________________________________________________________
#73,160 objects
match = Table("Data_Sample_V7.fits",hdu=8)
#here we choose Bologna absolute magnitude (only to be consistent with my previous, not conscious, work)
mZ = match.getCol("zspec_1")
mU = match.getCol("M_Uj")
mV = match.getCol("M_V")
mUV = mU-mV
mTAU = match.getCol("TAU_2")
mmass = match.getCol("log_stellar_mass")

mD4000 = match.getCol("D4000n_Mean")

#till now I've been using bologna variables
# when I match bologna data with gossip one.
#Infact magnitudes are more reliable than the gossip one.
#johnson magnitudes are VEGA magnitudes (vega to ab = 0.96).
# I think that the mismatch with
# bologna mags (particularly the Uj magnitudes)
# could be due to this fact.
# Ages estimations are complitely different, but this
# is motivated by the different choice
# of SFH (declaying for bologna and delayed for gossip)
#So, I add variables for both samples.

#m=match b=bologna
mbU = mU
mbV = mV
mbUV = mUV
mbTAU = match.getCol("tau_3")
mbAGE = match.getCol("age_3") #age of bologna, not reliable
mbMASS = mmass


#m=match g=gossip
mgU = match.getCol("UJ_abs")
mgV = match.getCol("VJ_abs")
mgUV = mgU-mgV
mgTAU = mTAU
mgAGE = match.getCol("AGE_2")
mgMASS = match.getCol("STELLAR_MASS")

SFR_Moust_log = np.array(match.getCol("sfrOIIMoust"))
SFR_Gossip = np.array(match.getCol("STAR_FORMATION_RATE"))


good_mag = np.where(mV!=-99)
mZ = mZ[good_mag]
mU = mU[good_mag]
mV = mV[good_mag]
mUV = mUV[good_mag]
mTAU = mTAU[good_mag]
mmass = mmass[good_mag]
mD4000 = mD4000[good_mag]

mbU = mbU[good_mag]
mbV = mbV[good_mag]
mbUV = mbUV[good_mag]
mbTAU = mbTAU[good_mag]
mbAGE = mbAGE[good_mag]
mbMASS = mbMASS[good_mag]

mgU = mgU[good_mag]
mgV = mgV[good_mag]
mgUV = mgUV[good_mag]
mgTAU = mgTAU[good_mag]
mgAGE = mgAGE[good_mag]
mgMASS = mgMASS[good_mag]

SFR_Moust_log = SFR_Moust_log[good_mag]
SFR_Gossip = SFR_Gossip[good_mag]

del match