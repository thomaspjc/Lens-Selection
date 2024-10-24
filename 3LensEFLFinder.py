#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 16:41:51 2024

@author: thomas
"""

import numpy as np
from numpy import pi as pi
import EFLTools as Tools
from tqdm import tqdm
from ThorLabsLenses import WavelengthAdapter
from itertools import product

def Finder2Lens(F1, F2, F3, d1_range, d2_range, tubeSize, inputBeam, fEff=1200, wavelength=253e-6, magnification=2):
    x, alpha = inputBeam
    
    
    '''
    Could make the distances range depending on the focals at hand
    No need to go longer than 1.5x the inital focal length to get the correct magnification
    '''
    # Pre-filter d1 and d2 using vectorized operations
    d1_range = d1_range[d1_range <= np.abs(2.5 * max(F1))]
    d2_range = d2_range[d2_range <= max(F2)/3]
    print(len(d1_range), len(d2_range))
    
    # We replace the 5D meshgrid with a generator to avoid creating huge arrays
    valid_pairs = []
    totalCombinations = len(F1) * len(F2) * len(F3) * len(d1_range) * len(d2_range)
    
    
    
    for f1, f2, f3, d1, d2 in tqdm(product(F1, F2, F3, d1_range, d2_range), total = totalCombinations):
        # -------------- Determine appropriate distance ranges ----------------
        if d1 > 2.5*f1 or d2 > f2/3:
            continue
        
        # -------------- Determine the EFL for a 3 Lens system ----------------
        EFL = (f1 * f2 * f3) / (f1 * f2 - d2 * (f1 + f2) + d1 * (d2 - f3) + f1 * f3 + f2 * f3)

        # Remove invalid combinations early
        if not np.isclose(fEff, EFL, atol=1.0):
            continue

        # Extract Transfer Matrix parameters
        A = (d1 * (d2 - f2) + f1 * f2 - d2 * (f1 + f2)) / (f1 * f2)
        B = (d1 + d2 - (d1 * d2) / f2)
        C = (-f1 * f2 + d2 * (f1 + f2) - f1 * f3 - f2 * f3 + d1 * (-d2 + f2 + f3)) / (f1 * f2 * f3)
        D = (d1 * (d2 - f2 - f3) + f2 * (-d2 + f3)) / (f2 * f3)

        # Calculate Principal Plane distance from the last lens
        H2 = (1 - A) / C

        # Calculate tube length and apply the tube size mask
        tubeLength = d1 + d2 + H2
        if tubeLength >= tubeSize:
            continue
        
        # Calculate the beam widths at lens 2 and lens 3
        q0 = Tools.BuildingInput(inputBeam)
        qLens3 = (A * q0 + B) / (C * q0 + D)
        lensRadius3 = np.abs((-pi / wavelength * np.imag(1 / qLens3)) ** (-1 / 2))

        A2 = 1 - d1 / f1
        B2 = d1
        C2 = - (f1 + f2 - d1) / (f1 * f2)
        D2 = 1 - d1 / f2

        qLens2 = (A2 * q0 + B2) / (C2 * q0 + D2)
        lensRadius2 = np.abs((-pi / wavelength * np.imag(1 / qLens2)) ** (-1 / 2))

        # Apply width mask
        if lensRadius2 > magnification * inputBeam[0] or lensRadius3 > magnification * inputBeam[0]:
            continue
         
        # Output a valid solution on that run
        valid_solution = (f1, f2, f3, d1, d2, H2, tubeLength, EFL)
        print(valid_solution)
        
        # Save valid configuration
        valid_pairs.append(valid_solution)

    return valid_pairs

if __name__ == "__main__":
    wavelength = 253e-6 # 253 nm in mm
    inputBeam = [4, 4e-4]
    d1 = np.arange(5, 150, 0.01)
    d2 = np.arange(5, 150, 0.01)
    fConcaveNP = [-1000, -250, -200, -150, -100, -75, -50, -10]
    focals_1_inch = WavelengthAdapter(253, size='1 inch')
    fConcave, fConvex = [x for x in focals_1_inch if x < 0], [x for x in focals_1_inch if x >= 0]
    fConcave = np.array(fConcave)
    fConcave = fConcave[(fConcave > -80)]
    print(fConcave)
    effective = Finder2Lens(fConcave, fConvex, fConvex, d1, d2, 150, inputBeam, magnification=1.3)
    print(len(effective))
