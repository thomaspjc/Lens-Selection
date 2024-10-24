#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 11:04:48 2024

Finding a 1200mm EFL lens system using parallel computing to speed up iterations

@author: thomas
"""

import numpy as np
from numpy import pi as pi
import EFLTools as Tools
from tqdm import tqdm
from ThorLabsLenses import WavelengthAdapter
from itertools import product
from concurrent.futures import ProcessPoolExecutor, as_completed

def compute_valid_pairs(f1, f2, f3, d1_range, d2_range, tubeSize, inputBeam, fEff, wavelength, magnification):
    valid_pairs = []
    x, alpha = inputBeam
    

    for d1, d2 in product(d1_range, d2_range):
        if d1 > 2.5*f1 or d2 > f2:
            continue

        EFL = (f1 * f2 * f3) / (f1 * f2 - d2 * (f1 + f2) + d1 * (d2 - f3) + f1 * f3 + f2 * f3)

        if not np.isclose(fEff, EFL, atol=1.0):
            continue

        A = (d1 * (d2 - f2) + f1 * f2 - d2 * (f1 + f2)) / (f1 * f2)
        B = (d1 + d2 - (d1 * d2) / f2)
        C = (-f1 * f2 + d2 * (f1 + f2) - f1 * f3 - f2 * f3 + d1 * (-d2 + f2 + f3)) / (f1 * f2 * f3)
        D = (d1 * (d2 - f2 - f3) + f2 * (-d2 + f3)) / (f2 * f3)

        H2 = (1 - A) / C
        tubeLength = d1 + d2 + H2
        if tubeLength >= tubeSize:
            continue

        q0 = Tools.BuildingInput(inputBeam)
        qLens3 = (A * q0 + B) / (C * q0 + D)
        lensRadius3 = np.abs((-pi / wavelength * np.imag(1 / qLens3)) ** (-1 / 2))

        A2 = 1 - d1 / f1
        B2 = d1
        C2 = - (f1 + f2 - d1) / (f1 * f2)
        D2 = 1 - d1 / f2

        qLens2 = (A2 * q0 + B2) / (C2 * q0 + D2)
        lensRadius2 = np.abs((-pi / wavelength * np.imag(1 / qLens2)) ** (-1 / 2))

        if lensRadius2 > magnification * inputBeam[0] or lensRadius3 > magnification * inputBeam[0]:
            continue

        valid_solution = (f1, f2, f3, d1, d2, H2, tubeLength, EFL)
        valid_pairs.append(valid_solution)

    return valid_pairs

def Finder2Lens(F1, F2, F3, d1_range, d2_range, tubeSize, inputBeam, fEff=1200, wavelength=253e-6, magnification=2):
    totalCombinations = len(F1) * len(F2) * len(F3)
    valid_pairs = []

    with ProcessPoolExecutor() as executor:
        futures = []
        for f1, f2, f3 in tqdm(product(F1, F2, F3), total=totalCombinations):
            futures.append(
                executor.submit(compute_valid_pairs, f1, f2, f3, d1_range, d2_range, tubeSize, inputBeam, fEff, wavelength, magnification)
            )

        for future in tqdm(as_completed(futures), total=len(futures)):
            valid_pairs.extend(future.result())

    return valid_pairs

if __name__ == "__main__":
    wavelength = 253e-6  # 253 nm in mm
    inputBeam = [4, 4e-4]
    d1 = np.arange(5, 150, 0.01)
    d2 = np.arange(5, 150, 0.01)
    fConcaveNP = [-1000, -250, -200, -150, -100, -75, -50, -10]
    focals_1_inch = WavelengthAdapter(253, size='1 inch')
    fConcave, fConvex = [x for x in focals_1_inch if x < 0], [x for x in focals_1_inch if x >= 0]

    effective = Finder2Lens(fConcave, fConvex, fConvex, d1, d2, 150, inputBeam, magnification=1.3)
    print(len(effective))