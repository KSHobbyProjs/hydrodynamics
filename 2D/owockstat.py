'''
Updated on Jan 7 2023

A module for handling the statistics for 2D hydrodynamics simulations.
The statistics are taken from the Owocki paper on simulated clumps.

4.9.2023 Update: I don't have the time right now, but this should be updated so 
that it functions similar to the plotter that I made for PY 452. This one's a tad
clunky (mainly with the way the figure is initialized). Overall, it's ok, though

Created by Keanan Scarbro
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os 

import owockstat_constants as consts


def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
        xs = [float(datai.split()[0]) for datai in data]
        yss = [[float(datai.split()[i]) for datai in data] for i in range(1, len(data[0].split()))]
    return xs, yss

def plot_data(ax, xs, ys, xscale, yscale, xlabel, ylabel, label, title, xlim, ylim, rstar_line):
    ax.plot(np.array(xs) / xscale, np.array(ys) / yscale, '.' ,label = label)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    if label: ax.legend()
    if rstar_line: ax.axvline(x = consts.bsep / consts.rstar, linestyle = ':', color = 'r')


#define the Gaussian function
def gauss(x, H, A, x0, sigma):
    return H + A * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))

if __name__ == "__main__":
    # Defining the correlation functions figure
    fig_cor, ax_cor = plt.subplots()
    ax_cor.axvline(x = 0, linestyle = ':', color = 'r')
    for file in os.listdir():
        # If the file in the directory doesn't end with .dat, skip it
        if not file.endswith('.dat'): continue
        xs, yss = read_file(file)
        for i, ys in enumerate(yss): 
            # If the file is a correlation function, plot it on the correlation figure
            # Otherwise, create a new figure for each plot
            if file.find("cor.dat") != -1: ax = ax_cor
            else: fig, ax = plt.subplots()
            plot_data(ax, xs, ys, *consts.plot_data[f"{file.strip('.dat')}{i}"])
        
        # If the file is the correlation function for the whole circumference, take the gaussian fit
        if file == "fullcor.dat":
            parameters, covariance = curve_fit(gauss, xs, yss[0])
            cor_fit = gauss(xs, parameters[0], parameters[1], parameters[2], parameters[3])
            fwhm = 2 * np.sqrt(2 * np.log(2)) * parameters[3]
            ax_cor.plot([-fwhm / 2 + parameters[2], fwhm / 2 + parameters[2]], [parameters[1] / 2, parameters[1] / 2], '-.r')
            ax_cor.plot(xs, cor_fit, '--')
            print(f"The full-width half-max for the approximate gaussian is {fwhm}")
    plt.show()