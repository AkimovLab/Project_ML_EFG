import os
import sys
import glob
import numpy as np
from libra_py import data_conv

input_template = "xtb.inp"
submit_template = "submit_template.slm"
prefix = "xtb_guess"
nprocs = 9
atom = "I"

def sort_coordinates(filename, atom):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    f = open(filename, 'w')
    f.write(lines[0])
    f.write(lines[1])
    for i in range(2,len(lines)):
        if atom in lines[i]:
            f.write(lines[i])
    for i in range(2,len(lines)):
        if atom not in lines[i]:
            f.write(lines[i])
    f.close()

def read_charge(filename):
    f = open(filename,'r')
    lines = f.readlines()
    f.close()
    charge = 0
    for i in range(len(lines)):
        if 'charge' in lines[i].lower():
            charge = int(lines[i].split()[1])
    return charge

f = open(input_template,'r')
lines_input = f.readlines()
f.close()

f = open(submit_template,'r')
lines_submit = f.readlines()
f.close()
not_run = []
for i in range(1,501):
    if not os.path.exists(f'{prefix}_{i}-libra-1_0.Log'):
        not_run.append(i)
#for step in range(0, 501):
for step in not_run:
    try:
        print('Submitting EFG calculations for step', step)
        formatted_step = "{:04d}".format(step)
        data_conv.adf_to_xyz(f'{formatted_step}-scf.inp', step)
        sort_coordinates(f"coord-{step}.xyz", atom) 
        charge = read_charge(f'{formatted_step}-scf.inp')
        f = open(F"input_{prefix}_{step}.inp", "w")
        for i in range(len(lines_input)):
            if "COORD_FILE_NAME".lower() in lines_input[i].lower():
                f.write(F"     COORD_FILE_NAME  coord-{step}.xyz \n")
            elif "project " in lines_input[i].lower() or "project_name" in lines_input[i].lower():
                f.write(F"  PROJECT {prefix}_{step}\n")
            elif "charge " in lines_input[i].lower() and "!" not in lines_input[i]:
                f.write(f"     CHARGE {charge}\n")
            elif "filename" in lines_input[i].lower() and "!" not in lines_input[i]:
                f.write("     FILENAME libra\n")
            else:
                f.write(lines_input[i])
        f.close()
        
        f = open('submit_1.slm','w')
        f.write('#!/bin/sh -l \n')
        for i in range(len(lines_submit)):
            if '#SBATCH' in lines_submit[i]:
                f.write(lines_submit[i])
        f.write('module use /projects/academic/cyberwksp21/MODULES \nmodule load cp2k/v24/avx512')
        f.write(f'\nmpirun -np {nprocs} cp2k.psmp -i input_{prefix}_{step}.inp -o output_{prefix}_{step}.log\n')
        f.write('rm *wfn*')
        f.close()
        os.system('sbatch submit_1.slm')
    except:
        print('Failed submission for step', step)


