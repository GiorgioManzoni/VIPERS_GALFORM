import numpy as np
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rc('xtick', labelsize=10) 
matplotlib.rc('ytick', labelsize=10)
matplotlib.rcParams.update({'font.size': 20})
import pandas as pd

def integ_trap(func,z1,z2,N=1000):
    z = np.logspace(np.log10(z1),np.log10(z2),N)
    y = func(z)
    
    A = 0
    for i in range(len(z)-1):
        A += np.abs((z[i+1]-z[i]))*(y[i]+y[i+1])/2
    return A

def E(z,Om_rad=8.4*10**(-5),Om_lambda=0.7,Om_mat=0.3):
    return np.sqrt(Om_rad*(1+z)**4 + Om_mat*(1+z)**3 + Om_lambda)

def over_E(z):
    return E(z)**(-1)

def comoving_distance(z):
    zero = 10**(-20)
    c = 3e5 #km/s
    H0=100. #km/s/Mpc
    return (c*H0**(-1)*integ_trap(over_E,zero,z,10**(3))) #Mpc h^-1

vec_r = np.vectorize(comoving_distance)

def Luminosity_distance(z):
    '''Returns the Luminosity distance in units of Mpc h^-1'''
    return comoving_distance(z)*(1.+z)

def ABSOLUTE_MAGNITUDE_minus5logh(m,z,K_correction=False,ratio_L=1.):
    if K_correction:
        return m -25. -5.*np.log10(Luminosity_distance(z)) -2.5*np.log10(ratio_L*(1.+z))
    else:
        return m -25. -5.*np.log10(Luminosity_distance(z))

vec_ABSOLUTE_MAGNITUDE_minus5logh = np.vectorize(ABSOLUTE_MAGNITUDE_minus5logh)


def EDGE(x,y,x_min=-26.,x_max=-15.,x_bin_size=0.1,y_min=0.55,y_max=2.1,y_bin_size=0.15,threashold =0.15):
    '''It returns two arrays containing the x and y of the edge'''
    y_Nbins = int((y_max - y_min) / y_bin_size)
    x_Nbins = int((x_max - x_min) / x_bin_size)
    x_edge=[]
    y_edge=[]
    #loop on y bins
    for i in range(y_Nbins):
        # define y bin
        y_low = y_min + y_bin_size * i
        y_high = y_min + y_bin_size * (i+1)
        y_center = (y_low+y_high)/2.
        select_y_in_ybin = np.where((y>=y_low)&(y<y_high))
        # histogram of x in a selected y bin
        x_histo, x_histo_bins = np.histogram(x[select_y_in_ybin],bins=x_Nbins,range=(x_min,x_max))
        #find most populated bin
        x_histo_max = np.max(x_histo[:-1])
        x_histo_max_index = np.argmax(x_histo[:-1])
        #loop to find the edge
        for j in range(x_histo_max_index,0,-1):
            if (x_histo[j]<x_histo_max * threashold):
                edge_index = j
                break
        x_edge.append(x_histo_bins[j])
        y_edge.append(y_center)
    return np.array(x_edge), np.array(y_edge)


def histo_in_colour_bin_general(min_col,max_col,u,v,i,redshift,thr=0.15,xbsz=0.1,save=True,path='./plots/image.png'):
    plt.figure(figsize=(10,8))
    
    sec = np.where(i<ABSOLUTE_MAGNITUDE_minus5logh(22.5,z=redshift))
    
    select_colour_bin = np.where(((u[sec]-v[sec])<max_col)&((u[sec]-v[sec])>min_col))
    plt.hist(v[sec][select_colour_bin],bins=int((26-18)/xbsz),range=(-26,-18),label=str(min_col)+'<U-V<'+str(max_col))
    #print(int((22-10)/0.1))
    
    counts,b = np.histogram(v[sec][select_colour_bin],bins=int((26-18)/xbsz),range=(-26,-18))
    
    #plt.axvline(b[np.where(counts==np.max(counts))],c='k',lw=3)
    plt.axvline(b[np.argmax(counts)],c='k',lw=3)
    
    #loop to find the edge
    for j in range(np.argmax(counts),0,-1):
        if (counts[j]<np.max(counts) * thr):
            edge_index = j
            break
    plt.axvline(b[j],c='k',lw=3)
    plt.xlabel("mag_V_ext")
    plt.ylabel('counts')
    plt.legend()
    if save:
        plt.savefig(path)

    plt.show()
