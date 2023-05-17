# HYDRODYNAMICS

Developers: Keanan Scarbro

Date: 5/17/2023
___
## DESCRIPTION

This is a repository of work from my undergraduate research in the Blondin Research Group. While researching under Dr. John Blondin, I used VH-1, a hydrodynamics simulation code created by Dr. Blondin, to analyze the accretion process in high-mass X-ray binaries (HMXBs) when the stellar outflow from the primary star is densely inhomogeneous. I focused on the archetypical HMXB Vela X-1.
___

## DETAILS
Instead of introducing physically-motivated density inhomogeneities (clumps) into the primary's stellar wind, we simulate them. In the initial stages of my research, I did this by altering the equations in VH-1 that governed gravity (a choice that makes no sense). 

Then, I tried to alter the alpha (abbott) parameter (the parameter that governs how the gas is accelerated as it moves away from the primary star through line driving) in time using random numbers. 

Following this, I altered the inner density boundary with time using random numbers.

Lastly, I went back to altering the alpha parameter. I altered abbott with a Gaussian that was scaled with random numbers and lastly added the Perlin algorithm to give extra control over how these random numbers are generated. To be clear, alpha is initially set to a constant pervasive throughout the gas; I then changed this pervasive value in time using random numbers; then, I added a Gaussian so that alpha wasn't changed in the same way with the random numbers everywhere but instead only locally around some region; lastly, I added the Perlin algorithm so that the random numbers were more controllable.

The repository is structured in the following way:
- Perlin_Noise is a folder dedicated to showing how the random numbers can be controlled using the Perlin algorithm. There are a few parameters associated with the Perlin algorithm that can be altered, and the one that I changed to achieve the variation in the plots is nearly akin to "frequency." In the plots, the x-axis is just the index of the random numbers, and the y-axis is the value of the random number
- 1D has all results and code associated with one-dimensional simualtions. There are three folders: Abbott_Mod, Dinflo_Mod, and Perlin, each corresponding to the era in my research where I was exploring the different methods of simulating clumps, as listed above. Most of the plots (produced by denvel.py) are of the density and velocity profiles of the gas for various adjustments of abbott or dinflo in time.
- 2D is similarly structured to 1D, but the results are from two-dimensional simulations. The animations are usually of density or velocity profiles, but the plots are of statistical diagnostics produced by the owockstat.py module. owockstat_constants.py is just a config file for owockstat.py, and cor_fix.py is a helper module that adjusts how the correlation data files (produced by a program I wrote in FORTRAN) format the data.
- 3D is similarly structured to 1D and 2D, but the results are from three-dimensional simulations. "DeepSlow" and "IntrmSlow" refer to various models setup in 3D that are related to my associate's (Anna Taylor's) research. Based on data from observations, the radius of the primary star and the speed of the primary star's wind in Vela X-1 have a smaller/slower and larger/faster bound. "Deep" refers to the smallest radius primary possible, "Intrm" refers to the intermediate radius primary possible, "Close" refers to the largest radius primary possible, "Slow" refers to the slowest wind speed possible, and "Fast" refers to the fastest wind speed possible. These different setups have massive affects on the formation of wind captured disks (Anna's research) and how density inhomogeneties are formed.
___

## AUTHOR
Name: Keanan Scarbro <br>
Email: scarbro.kms1@gmail.com

It's May 2023, and I'm a grad student in physics at NCSU going into my first year this fall.