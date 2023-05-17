import matplotlib.pyplot as plt

# Read a data file
def readfile(file_path):
    with open(file_path, 'r') as f:
        data = f.readlines()
        if closeup:
            rs = [(float(datai.split()[0]) - rstar) / float(datai.split()[0]) for datai in data]
        else:
            rs = [float(datai.split()[0]) / rstar for datai in data]
        rhos = [float(datai.split()[1]) for datai in data]
        us = [float(datai.split()[3]) for datai in data]
        data_dict = {"rs": rs, "den": rhos, "vel": us}
    return data_dict

# Looks to see if a key is entered in a dictionary; if it doesn't, return none; if it does, return the value
def check_dict(dict_, key):
    if key in dict_: return dict_[key]
    else: return  None
    
# Initialize the figure
def init_fig(ax, **kwargs):
    if "xscale" in kwargs: ax.set_xscale(kwargs["xscale"])
    if "yscale" in kwargs: ax.set_yscale(kwargs["yscale"])
    ax.set_xlabel(check_dict(kwargs, "xlabel"))
    ax.set_ylabel(check_dict(kwargs, "ylabel"))
    ax.set_title(check_dict(kwargs, "title"))
    ax.set_xlim(check_dict(kwargs, "xlim"))
    ax.set_ylim(check_dict(kwargs, "ylim"))
    
# Plot the data
def plot_data(ax, xs, ys, **kwargs):
    ax.plot(xs, ys)
    

if __name__ == "__main__":
    # Constants
    #rstar = 1.850e+12 # Deep
    rstar = 2.160e+12 # Intrm
    #rstar = 2.285e+12 # Close
    bsep =  3.687e+12 # binary separation

    ampabb = .07          # amplitude of abbott Gaussian
    radabb = 2.52e+12 # radius/rstar where abbott Gaussian is maximum
    widabb = 5.0e+11 # width/rstar of abbott Gaussian (half of standard deviation)
    
    print("What is the file prefix?")
    file_prefix = input()
    print("What is the beginning and ending time (enter tuple)")
    times = input()
    a, b = int(times.split()[0]), int(times.split()[1])
    print("Do you want a closeup?")
    closeup = True if input().lower() == 'y' else False
    
    if closeup:
        radabb = (radabb - rstar) / radabb
        bsep = (bsep - rstar) / bsep
    else:
        radabb = radabb / rstar
        bsep = bsep / rstar
    
    
    all_data = [readfile(f"abmod/{file_prefix}{file_num}.dat") for file_num in range(a, b)]
    steady_data = readfile("abmod/steady.dat")
    fig_den, ax_den = plt.subplots()
    fig_vel, ax_vel = plt.subplots()
    for ax in [ax_den, ax_vel]:
        stat = "den" if ax == ax_den else "vel"
        for i in range(b - a): plot_data(ax, all_data[i]["rs"], all_data[i][stat])
        ax.axvline(x = radabb, linestyle = ':', color = 'r')
        ax.axvline(x = bsep, linestyle = ':', color = 'green')
        plot_data(ax, steady_data["rs"], steady_data[stat])
    if closeup:
        init_fig(ax_den, xscale = 'log', yscale = 'log', xlabel = r'$(r-R_*)/r$', ylabel = 'Density (g/cm^3)', title = 'Density')
        init_fig(ax_vel, xscale = 'log', xlabel = r"$(r-R_*)/r$", ylabel = "Velocity (cm/s)", title = "Velocity")
    else:
        init_fig(ax_den, yscale = 'log', xlabel = r'$r/R_*$', ylabel = 'Density (g/cm^3)', title = 'Density')
        init_fig(ax_vel, xlabel = r"$r/R_*$", ylabel = "Velocity (cm/s)", title = "Velocity")
  
    #if sphere_diver:
  #    outputnums = [output * rnums[i]**2 for i, output in enumerate(outputnums)]
  #    for i in range(4): 
  #        abmodnums[i, :] = [modnum * rnums[j]**2 for j, modnum in enumerate(abmodnums[i, :])]
  