#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:05:53 2024

Tool Functions for EFL uses

@author: thomas
"""
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi as pi
from tqdm import tqdm
from matplotlib.colors import LogNorm
from matplotlib.colors import LinearSegmentedColormap
from cmocean import cm
import seaborn as sns
from matplotlib.colors import Normalize
from ThorLabsLenses import WavelengthAdapter

# --- Globals ---
inch1 = 25.4 # in mm
inch2 = 50.8 # in mm
wavelength = 253e-9

def BuildingInput(inputBeam, wavelength = 253e-9):
    wZ, alpha = inputBeam
    z = wZ / np.tan(2*alpha)
    w0 = np.sqrt(wZ**2 + np.sqrt(pi**2 * wZ**4 - 4 * z**2 * wavelength**2) / pi) / np.sqrt(2)
    w0 = np.sqrt(wZ**2 - np.sqrt(pi**2 * wZ**4 - 4 * z**2 * wavelength**2) / pi) / np.sqrt(2)
    
    z0 = pi * w0**2/wavelength
    qZ = z + 1j * z0
    
    return qZ

def Lens(f):
    return np.array([[1,0],[-1/f, 1]])

def Propagate(z):
    return np.array([[1, z],[0, 1]])

def Transfer(inputQ, transferMatrix):
    
    # --- Extracting the Parameters ---
    (A,B),(C,D) = transferMatrix[0], transferMatrix[1]
    # --- Applying the transfer Matrix ---
    qPrime = (A * inputQ + B)/(C*inputQ + D)
    
    # --- Extracting new parameters for the beam ---
    w_z = np.abs((-pi/wavelength * np.imag(1/qPrime))**(-1/2))
    R_z = ((1/qPrime).real)**(-1)
    
    return qPrime, w_z, R_z