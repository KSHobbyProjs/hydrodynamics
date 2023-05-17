# -*- coding: utf-8 -*-
"""
A module to handle 3D hydrodynamics statistics

Dr. Blondin Research Group

Date created: 4/22/2022

"""
import numpy as np
import matplotlib.pyplot as plt

# open and read acc file
abbvar_acc = open("./3dAbbVar.acc", "r")
abbvar_lines = abbvar_acc.readlines()

# initialize lists to hold time and mass loss values
times = np.zeros(len(abbvar_lines))
mass_loss = np.zeros(len(abbvar_lines))

# grab the data from the acc file
for i in range(len(abbvar_lines)):
    times[i] = float(abbvar_lines[i].split()[0])
    mass_loss[i] = float(abbvar_lines[i].split()[1])
    
# get rid of initial conditions
times = times[1700:]
mass_loss = mass_loss[1700:]  

# plot (taking normalization into account)  
plt.plot(times/1e5, mass_loss*1.586e-26) 
plt.xlabel(r"Time ($1\times10^5$ s)")
plt.ylabel(r"$\dot{M}_{NS}$   ($M_{\odot}$ yr$^{-1}$)")
plt.title("Massloss Rate")
plt.show()
