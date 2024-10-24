#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 17:01:03 2024

Determines the 2 Lens system to obtain an EFL of 600mm with a desired magnification

@author: thomas
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import pi as pi
import EFLTools as Tools
from tqdm import tqdm
from ThorLabsLenses import WavelengthAdapter

def Finder2Lens(F1, F2, d1, tubeSize, inputBeam, fEff = 600, tolerance = 1e-1,
                wavelength = 253e-6, transportDistance = 1200) :
    # --- Extracting variables --- 
    x, alpha = inputBeam
    
    #Creating a 3D Meshgrid to find all possible combinations of lens arrangements
    f1, f2, d1 = np.meshgrid(F1, F2, d1, indexing ='xy')

    # --- Preparing the Matrix Representations --- 
    A = 1-d1/f1
    B = d1
    C = - (f1+f2-d1)/(f1*f2)
    D = 1-d1/f2
    
    # --- Determine the EFL for a 2 Lens system ---
    EFL = 1 / (1/f1 + 1/f2 - d1/(f1 * f2))

    # --- Determine the Principal Plane distance from the last lens ---
    H2 = (1-A)/C
    
    # --- Finding Beam Widths --- 
    q0 = Tools.BuildingInput(inputBeam)
    
    # --- Determine the width of the beam at the second lens ---
    qLens = (A * q0 + B)/(C* q0 + D)
    
    lensRadius = np.abs((-pi/wavelength * np.imag(1/qLens))**(-1/2))
    
    # --- Determine the beam width at the cathode --- 
    #Finding the final Transfer Matrix parameters
    Af = A + C * (H2 + fEff)
    Bf = B + D * (H2 + fEff)
    Cf, Df = C, D
    
    qPrime = (Af * q0 + Bf)/(Cf* q0 + Df)

    #print(qPrime)
    finalRadius = np.abs((-pi/wavelength * np.imag(1/qPrime))**(-1/2))
    #print(finalRadius)
    # --- Selecting Acceptable setups ---
    tubeLength = H2 + d1 - (transportDistance - fEff)  #total size of the system assuming thin lens 
    mask = (
        (fEff == np.round(EFL, 0)) # We need the correct effective focal length 
        & 
        (np.abs(tubeLength) < tubeSize) #resticted by the size of the optical holder
        &
        (lensRadius > 2 * inputBeam[0]) # (np.abs(lensRadius - 2 * inputBeam[0]) < 1)
        &
        (np.abs(H2+fEff)>transportDistance)
        )
   
    f1Valid = f1[mask]
    f2Valid = f2[mask]
    d1Valid = d1[mask]
    H2Valid = H2[mask]
    tubeValid = tubeLength[mask]
    validEFL = EFL[mask]
    finalValidRadius = finalRadius[mask]
    print(f1[mask], f2[mask])
    # --- Pairing up the pair wise valid solutions --- 
    valid_pairs = list(zip(f1Valid, f2Valid, d1Valid, H2Valid, tubeValid, finalValidRadius, validEFL))
    
    return valid_pairs



if __name__ == "__main__":
    wavelength = 253e-6 #253 nm in mm
    inputBeam = [4, 1e-6]
    d1 = np.arange(20, 100, 0.005)
    d2 = np.arange(10, 30, 0.1)
    d3 = np.arange(1200, 1500, 0.1)
    fConcaveNP = [-1000, -250,-200, -150,-100, -75, -50, -10]
    focals_1_inch = WavelengthAdapter(253, size = '1 inch')
    fConcave, fConvex = [x for x in focals_1_inch if x < 0], [x for x in focals_1_inch if x >= 0]

    effective = Finder2Lens(fConcave, fConvex, d1, 150, inputBeam,
                            tolerance = 1, fEff = 900)
    print(len(effective))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
