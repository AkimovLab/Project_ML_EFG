#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import glob
import numpy as np
import matplotlib.pyplot as plt
import libra_py.packages.cp2k.methods as CP2K_methods
from IPython.display import clear_output
import pandas as pd


# In[26]:

atom = "Na"
size = 4
overlaps = []
densities = []
hams = []
for i in range(0,502):
    try:
        print(i)
        prop, matrices = CP2K_methods.read_ao_matrices(f'{atom}/xtb_guess_{i}-libra-1_0.Log')
        overlap = matrices[0][0:size,0:size]
        density = matrices[1][0:size,0:size]
        ham = matrices[2][0:size,0:size]
        upper_indices = np.triu_indices(density.shape[0])
        # 1
        tmp1 = overlap[upper_indices]
        tmp2 = matrices[0][0:size,size:].flatten()
        tmp3 = np.concatenate((tmp1,tmp2))
        overlaps.append(tmp3)
        # 1 
        # 2
        tmp1 = density[upper_indices]
        tmp2 = matrices[1][0:size,size:].flatten()
        tmp3 = np.concatenate((tmp1,tmp2))
        densities.append(tmp3)
        # 2
        # 3
        tmp1 = ham[upper_indices]
        tmp2 = matrices[2][0:size,size:].flatten()
        tmp3 = np.concatenate((tmp1,tmp2))
        hams.append(tmp3)
        # 3
        clear_output()
    except:
        pass
min_size = 1e10
for i in range(len(overlaps)):
    min_size = min(min_size, len(overlaps[i]))
overlaps_ = []
densities_ = []
hams_ = []
for i in range(len(overlaps)):
    overlaps_.append(overlaps[i][0:min_size])
    densities_.append(densities[i][0:min_size])
    hams_.append(hams[i][0:min_size])
overlaps_ = np.array(overlaps_)
densities_ = np.array(densities_)
hams_ = np.array(hams_)
print(densities_.shape, hams_.shape, overlaps_.shape)
np.save(f'{atom}_xtb_guess_overlap.npy', overlaps_)
np.save(f'{atom}_xtb_guess_density.npy', densities_)
np.save(f'{atom}_xtb_guess_ham.npy', hams_)


# In[23]:


atom = "Na"
size = 9
overlaps = []
densities = []
hams = []
for i in range(0,502):
    try:
        print(i)
        prop, matrices = CP2K_methods.read_ao_matrices(f'{atom}/pbe_guess_{i}-libra-1_0.Log')
        overlap = matrices[0][0:size,0:size]
        density = matrices[1][0:size,0:size]
        ham = matrices[2][0:size,0:size]
        upper_indices = np.triu_indices(density.shape[0])
        # 1
        tmp1 = overlap[upper_indices]
        tmp2 = matrices[0][0:size,size:].flatten()
        tmp3 = np.concatenate((tmp1,tmp2))
        overlaps.append(tmp3)
        # 1 
        # 2
        tmp1 = density[upper_indices]
        tmp2 = matrices[1][0:size,size:].flatten()
        tmp3 = np.concatenate((tmp1,tmp2))
        densities.append(tmp3)
        # 2
        # 3
        tmp1 = ham[upper_indices]
        tmp2 = matrices[2][0:size,size:].flatten()
        tmp3 = np.concatenate((tmp1,tmp2))
        hams.append(tmp3)
        # 3
        clear_output()
    except:
        pass
min_size = 1e10
for i in range(len(overlaps)):
    min_size = min(min_size, len(overlaps[i]))
overlaps_ = []
densities_ = []
hams_ = []
for i in range(len(overlaps)):
    overlaps_.append(overlaps[i][0:min_size])
    densities_.append(densities[i][0:min_size])
    hams_.append(hams[i][0:min_size])
overlaps_ = np.array(overlaps_)
densities_ = np.array(densities_)
hams_ = np.array(hams_)
print(densities_.shape, hams_.shape, overlaps_.shape)
np.save(f'{atom}_atomic_guess_overlap.npy', overlaps_)
np.save(f'{atom}_atomic_guess_density.npy', densities_)
np.save(f'{atom}_atomic_guess_ham.npy', hams_)


# In[23]:


data = pd.read_csv('Na/Na_data.csv')
ref_data = data[['Vxx','Vxy','Vxz','Vyx','Vyy','Vyz','Vzx','Vzy','Vzz']].to_numpy()[0:501,:]
print(ref_data.shape)
np.save('Na_ref_efg.npy',ref_data)


# In[25]:


data = pd.read_csv('Cs/Cs_data.csv')
ref_data = data[['Vxx','Vxy','Vxz','Vyx','Vyy','Vyz','Vzx','Vzy','Vzz']].to_numpy()[0:433,:]
print(ref_data.shape)
np.save('Cs_ref_efg.npy',ref_data)


# In[26]:


data = pd.read_csv('I/I_data.csv')
ref_data = data[['Vxx','Vxy','Vxz','Vyx','Vyy','Vyz','Vzx','Vzy','Vzz']].to_numpy()[0:498,:]
print(ref_data.shape)
np.save('I_ref_efg.npy',ref_data)

