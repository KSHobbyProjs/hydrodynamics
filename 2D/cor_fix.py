# -*- coding: utf-8 -*-
"""
Created on January 11 2023

A module to fix the cor data files to remove the mesh points

@author: Keanan Scarbro
"""

import os

def cor_fix(file):
    with open(file, "r") as f: 
        data = f.readlines()
        xs = [float(datai.split()[1]) for datai in data]
        ys = [float(datai.split()[2]) for datai in data]
    with open(f"tmp{file}", "w") as f:
        for x, y in zip(xs, ys):
            f.write(f"{x} {y} \n")
    os.remove(file)
    os.rename(f"tmp{file}", file)
                

if __name__ == "__main__":
    # Either enter a specific file name or enter "All" to comb through all cor files
    file_name = 'hhhalfcor.dat'
    
    if file_name == "All":
        for file in os.listdir():
            if file.find("cor.dat") == -1: continue
            cor_fix(file)
    else:
        if file_name.find("cor.dat") == -1:
            raise RuntimeError("Cannot change a non cor file")
        else: cor_fix(file_name)
            
            
        
            