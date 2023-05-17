# -*- coding: utf-8 -*-
"""
Created on Jan  7 2023

A module to hold all of the constants for the owockstat module

Author: Keanan Scarbro
"""

# imax, jmax = 512, 512
# cor full is the full circumference
# cor half is the half circumference
# cor is .30 * np.pi

# cfac - 0: rs, 1: cfac, 2: rdisp, 3: tdisp
# mloss - 0: ts, 1: mloss
# cor - 0: mesh point, 1: arc length, 2: cor


rstar = 1.850e+12 # Deep
#rstar = 2.160e+12 # Intrm
#rstar = 2.285e+12 # Close
bsep = 3.687e+12 

# The numbers on the labels below are to separate the different columns
# 0 is the plot of xs and ys, 1 is the plot of xs and ys1, etc (this really only
# affects the cfac data because it's the only dat file with multiple columns).
plot_data = {
    "cfac0": [rstar, 1.0, r"$r/R_*$", r"$f_{cl}$", None, "Clumping Factor", None, None, True],
    "cfac1": [rstar, 1e5, r"$r/R_*$", r"$v_r$ Dispersion (km/s)", None, "Radial Velocity Dispersion", None, None, True],
    "cfac2": [rstar, 1e5, r"$r/R_*$", r"$v_t$ Dispersion (km/s)", None, "Tranverse Velocity Dispersion", None, None, True],
    "mloss0": [1e5, 6.305e25, r"Time ($1\times10^5$ s)", r"$\dot{M}_{opt}$ ($M_{\odot}$ yr$^{-1}$)", None, "Massloss Rate", None, None, False],
    "cor0": [1.0, 1.0, "Spatial Offset", "Density Correlation", "Cor", "Auto Correlation Length", [-.2,.2], None, None],
    "halfcor0": [1.0, 1.0, "Spatial Offset", "Density Correlation", "HalfCor", "Auto Correlation Length", None, None, None],
    "hhhalfcor0": [1.0, 1.0, "Spatial Offset", "Density Correlation", "HHHalfCor", "Auto Correlation Length", None, None, None],
    "hhalfcor0": [1.0, 1.0, "Spatial Offset", "Density Correlation", "HHalfCor", "Auto Correlation Length", None, None, None],
    #"fullcor0": [1.0, 1.0, "Spatial Offset", "Density Correlation", "FullCor", "Auto Correlation Length", [-.3, .3], None, None]
    }