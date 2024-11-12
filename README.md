# Project_ML_EFG

This repository contains all the pythonic file and data files required for performing ML mapping approach to predict the electric field gradient tensors from the Kohn-Sham Fock operator, density, and atomic orbital overlap matrices.

The tree of the files is as follows:

```
.
├── 1_generate_data
│   ├── 1_Na
│   │   ├── Na_atomic_guess_density.npy
│   │   ├── Na_atomic_guess_ham.npy
│   │   ├── Na_atomic_guess_overlap.npy
│   │   ├── Na_ref_efg.npy
│   │   ├── Na_xtb_guess_density.npy
│   │   ├── Na_xtb_guess_ham.npy
│   │   ├── Na_xtb_guess_overlap.npy
│   │   ├── run_calc.py
│   │   ├── submit_template.slm
│   │   └── xtb.inp
│   ├── 2_I
│   │   ├── I_atomic_guess_density.npy
│   │   ├── I_atomic_guess_ham.npy
│   │   ├── I_atomic_guess_overlap.npy
│   │   ├── I_ref_efg.npy
│   │   ├── I_xtb_guess_densities.npy
│   │   ├── I_xtb_guess_density.npy
│   │   ├── I_xtb_guess_ham.npy
│   │   ├── I_xtb_guess_hams.npy
│   │   ├── I_xtb_guess_overlap.npy
│   │   ├── I_xtb_guess_overlaps.npy
│   │   ├── run_calc.py
│   │   ├── submit_template.slm
│   │   └── xtb.inp
│   ├── 3_Cs
│   │   ├── Cs_atomic_guess_density.npy
│   │   ├── Cs_atomic_guess_ham.npy
│   │   ├── Cs_atomic_guess_overlap.npy
│   │   ├── Cs_ref_efg.npy
│   │   ├── Cs_xtb_guess_density.npy
│   │   ├── Cs_xtb_guess_ham.npy
│   │   ├── Cs_xtb_guess_overlap.npy
│   │   ├── run_calc.py
│   │   ├── submit_template.slm
│   │   └── xtb.inp
│   └── extract_data.py
├── 2_ml_mapping
│   └── ml_mapping.ipynb
├── 3_dynpy_calc
│   └── compute_properties.py
├── LICENSE
└── README.md

6 directories, 38 files
```
