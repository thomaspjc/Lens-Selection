#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 17:27:08 2024

Storing all the information from the Thorlabs UV Lenses in a dictionary

@author: thomas
"""

import numpy as np
from FusedSilica import FusedSilica, CalciumFluoride

# Dictionary for 1/2" (12.7 mm) UV Fused Silica Bi-Concave Lenses
lenses_0_5_inch = {
    "help": ["Diameter (mm)", "Focal Length (mm)", "Diopter", "Radius of Curvature (mm)", 
             "Center Thickness (mm)", "Edge Thickness (mm)", "Back Focal Length (mm)"],
    -15: np.array([12.7, -15.0, -66.6, -14.3, 3.0, 6.0, -16.0]),
    -30: np.array([12.7, -30.0, -33.3, -28.1, 3.0, 4.5, -31.0])
    }

# Dictionary for 1" (25.4 mm) UV Fused Silica Bi-Concave Lenses
lenses_1_inch = {
    "help": ["Diameter (mm)", "Focal Length (mm)", "Diopter", "Radius of Curvature (mm)", 
             "Center Thickness (mm)", "Edge Thickness (mm)", "Back Focal Length (mm)"],
   """-25: np.array([25.4, -25.0, -40.0, -23.5, 3.0, 10.5, -26.0]),
    -50: np.array([25.4, -50.0, -20.0, -46.6, 3.5, 7.0, -51.2]),
    -75: np.array([25.4, -75.0, -13.3, -69.6, 3.5, 5.8, -76.2]),
    -100: np.array([25.4, -100.0, -10.0, -92.6, 3.5, 5.3, -101.2]),
    35: np.array([25.4, 35.0, 28.6, 31.0, 7.4, 2.0, 32.4]),
    40: np.array([25.4, 40.0, 25.0, 35.7, 6.7, 2.0, 37.6]),
    50: np.array([25.4, 50.0, 20.0, 45.1, 5.7, 2.0, 48.0]),
    75: np.array([25.4, 75.0, 13.3, 68.3, 4.4, 2.0, 73.5]),
    100: np.array([25.4, 100.0, 10.0, 91.4, 3.8, 2.0, 98.7]),
    125: np.array([25.4, 125.0, 8.0, 114.5, 3.4, 2.0, 123.8]),
    150: np.array([25.4, 150.0, 6.7, 137.5, 3.2, 2.0, 148.9]),
    200: np.array([25.4, 200.0, 5.0, 183.6, 2.9, 2.0, 199.0]),
    250: np.array([25.4, 250.0, 4.0, 229.6, 2.7, 2.0, 249.1]),
    300: np.array([25.4, 300.0, 3.3, 275.6, 2.6, 2.0, 299.1]),
    500: np.array([25.4, 500.0, 2.0, 459.7, 2.4, 2.0, 499.2]),
    750: np.array([25.4, 750.0, 1.3, 689.8, 2.2, 2.0, 749.2]),
    1000: np.array([25.4, 1000.0, 1.0, 919.8, 2.2, 2.0, 999.3]),
    
    -150: np.array([25.4, -150.0, -6.7, -138.092, 2.5, 3.45, -150.85]),#Newport
    -200: np.array([25.4, -200.0, -5.0, -183.993, 2.5, 3.21, -200.85]),
    -250: np.array([25.4, -250.0, -4.0, -229.890, 2.5, 3.07, -250.85]),
    -1000: np.array([25.4, -1000.0, -1.0, -918.377, 2.5, 2.64, -1000.85])}"""

    "-30.0PCC": np.array([25.4, -30.0, -33.3, -13.8, 3.0, 11.4, -32.1, ">Ø22.86"]),# PlanoConcave
    "-75.0PCC": np.array([25.4, -75.0, -13.3, -34.5, 3.5, 5.9, -77.4, ">Ø22.86"]),
    "-100.0PCC": np.array([25.4, -100.0, -10.0, -46.0, 3.5, 5.3, -102.4, ">Ø22.86"]),
    "-150.0PCC":np.array([25.4, -150, -10, -68.850, 2.5, 3.46, -151.70, ">Ø22.86"]),
    "-200.0PCC":np.array([25.4, -200, -10, -91.800, 2.5, 3.21, -201.71, ">Ø22.86"]),
    
    
    "35.0PCX": np.array([25.4, 35.0, +28.6, 16.1, 8.2, 2.0, 29.4, ">Ø22.86"]),#PlanoConvex
    "40.0PCX": np.array([25.4, 40.0, +25.0, 18.4, 7.1, 2.0, 35.2, ">Ø22.86"]),
    "50.0PCX": np.array([25.4, 50.0, +20.0, 23.0, 5.8, 2.0, 46.0, ">Ø22.86"]),
    "75.0PCX": np.array([25.4, 75.0, +13.3, 34.5, 4.4, 2.0, 72.0, ">Ø22.86"]),
    "100.0PCX": np.array([25.4, 100.0, +10.0, 46.0, 3.8, 2.0, 97.4, ">Ø22.86"]),
    "125.0PCX": np.array([25.4, 125.0, +8.0, 57.5, 3.4, 2.0, 122.7, ">Ø22.86"]),
    "150.0PCX": np.array([25.4, 150.0, +6.7, 69.0, 3.2, 2.0, 147.8, ">Ø22.86"]),
    "175.0PCX": np.array([25.4, 175.0, +5.7, 80.5, 3.0, 2.0, 172.9, ">Ø22.86"]),
    "200.0PCX": np.array([25.4, 200.0, +5.0, 92.0, 2.9, 2.0, 198.0, ">Ø22.86"]),
    "250.0PCX": np.array([25.4, 250.0, +4.0, 115.0, 2.7, 2.0, 248.2, ">Ø22.86"]),
    "300.0PCX": np.array([25.4, 300.0, +3.3, 138.0, 2.6, 2.0, 298.2, ">Ø22.86"]),
    "500.0PCX": np.array([25.4, 500.0, +2.0, 230.0, 2.4, 2.0, 498.4, ">Ø22.86"]),
    "750.0PCX": np.array([25.4, 750.0, +1.3, 345.1, 2.2, 2.0, 748.5, ">Ø22.86"]),
    "1000.0PCX": np.array([25.4, 1000.0, +1.0, 460.1, 2.2, 2.0, 998.5, ">Ø22.86"])
    
    }

PlanoConvex = {
    "help": ["Diameter (mm)", "Focal Length (mm)", "Diopter", "Radius of Curvature (mm)", 
         "Center Thickness (mm)", "Edge Thickness (mm)", "Back Focal Length (mm)"],
    35.0: np.array([25.4, 35.0, +28.6, 16.1, 8.2, 2.0, 29.4, ">Ø22.86"]),
    40.0: np.array([25.4, 40.0, +25.0, 18.4, 7.1, 2.0, 35.2, ">Ø22.86"]),
    50.0: np.array([25.4, 50.0, +20.0, 23.0, 5.8, 2.0, 46.0, ">Ø22.86"]),
    75.0: np.array([25.4, 75.0, +13.3, 34.5, 4.4, 2.0, 72.0, ">Ø22.86"]),
    100.0: np.array([25.4, 100.0, +10.0, 46.0, 3.8, 2.0, 97.4, ">Ø22.86"]),
    125.0: np.array([25.4, 125.0, +8.0, 57.5, 3.4, 2.0, 122.7, ">Ø22.86"]),
    150.0: np.array([25.4, 150.0, +6.7, 69.0, 3.2, 2.0, 147.8, ">Ø22.86"]),
    175.0: np.array([25.4, 175.0, +5.7, 80.5, 3.0, 2.0, 172.9, ">Ø22.86"]),
    200.0: np.array([25.4, 200.0, +5.0, 92.0, 2.9, 2.0, 198.0, ">Ø22.86"]),
    250.0: np.array([25.4, 250.0, +4.0, 115.0, 2.7, 2.0, 248.2, ">Ø22.86"]),
    300.0: np.array([25.4, 300.0, +3.3, 138.0, 2.6, 2.0, 298.2, ">Ø22.86"]),
    500.0: np.array([25.4, 500.0, +2.0, 230.0, 2.4, 2.0, 498.4, ">Ø22.86"]),
    750.0: np.array([25.4, 750.0, +1.3, 345.1, 2.2, 2.0, 748.5, ">Ø22.86"]),
    1000.0: np.array([25.4, 1000.0, +1.0, 460.1, 2.2, 2.0, 998.5, ">Ø22.86"])
    }

PlanoConcave = {
    "help": ["Diameter (mm)", "Focal Length (mm)", "Diopter", "Radius of Curvature (mm)", 
             "Center Thickness (mm)", "Edge Thickness (mm)", "Back Focal Length (mm)", "Clear Aperture (mm)"],
    -30.0: np.array([25.4, -30.0, -33.3, -13.8, 3.0, 11.4, -32.1, ">Ø22.86"]),
    -75.0: np.array([25.4, -75.0, -13.3, -34.5, 3.5, 5.9, -77.4, ">Ø22.86"]),
    -100.0: np.array([25.4, -100.0, -10.0, -46.0, 3.5, 5.3, -102.4, ">Ø22.86"]),
    }

lenses_2_inch = {
    60: np.array([50.8, 60.0, 16.7, 52.6, 15.6, 2.5, 54.4]),
    75: np.array([50.8, 75.0, 13.3, 67.0, 12.5, 2.5, 70.6]),
    100: np.array([50.8, 100.0, 10.0, 90.4, 10.3, 3.0, 96.4]),
    150: np.array([50.8, 150.0, 6.7, 136.8, 7.8, 3.0, 147.3]),
    200: np.array([50.8, 200.0, 5.0, 183.0, 6.5, 3.0, 197.7]),
    250: np.array([50.8, 250.0, 4.0, 229.1, 5.8, 3.0, 248.0]),
    300: np.array([50.8, 300.0, 3.3, 275.2, 5.4, 3.0, 298.2]),
    500: np.array([50.8, 500.0, 2.0, 459.4, 4.4, 3.0, 498.5]),
    1000: np.array([50.8, 1000.0, 1.0, 919.6, 3.7, 3.0, 998.7])
    }

PurchasedFS = {
    "help": ["Diameter (mm)", "Focal Length (mm)", "Diopter", "Radius of Curvature (mm)", 
             "Center Thickness (mm)", "Edge Thickness (mm)", "Back Focal Length (mm)", "Clear Aperture (mm)"],
    "100.0PCX": np.array([25.4, 100.0, +10.0, 46.0, 3.8, 2.0, 97.4, ">Ø22.86"]),
    "-100.0PCC": np.array([25.4, -100.0, -10.0, -46.0, 3.5, 5.3, -102.4, ">Ø22.86"]),
    "200.0PCX": np.array([25.4, 200.0, +5.0, 92.0, 2.9, 2.0, 198.0, ">Ø22.86"]),

    }
PurchasedCaF2 ={
    "help": ["Diameter (mm)", "Focal Length (mm)", "Diopter", "Radius of Curvature (mm)", 
             "Center Thickness (mm)", "Edge Thickness (mm)", "Back Focal Length (mm)", "Clear Aperture (mm)"],
    "-200.0PCC": np.array([25.4, -200.0, -5.0, -86.8, 3.5, 4.5, -202.4, ">Ø22.86"]),
    }

# Dictionary for Ø1" (25.4 mm) CaF2 Bi-Convex Lenses, Uncoated
lenses_1_inch_caf2 = {
    "help": ["Diameter (mm)", "Focal Length (mm)", "Diopter", "Radius of Curvature (mm)", 
             "Center Thickness (mm)", "Edge Thickness (mm)", "Back Focal Length (mm)"],
    #-30.0: np.array([25.4, -30.0, -33.3, -26.4, 2.5, 9.0, -30.9]),
    #-50.0: np.array([25.4, -50.0, -20.0, -43.8, 3.0, 6.8, -51.0]),
    #25.4: np.array([25.4, 25.4, +39.4, 20.2, 11.0, 2.0, 21.2]),
    #50.0: np.array([25.4, 50.0, +20.0, 42.5, 5.9, 2.0, 47.9]),
    #75.0: np.array([25.4, 75.0, +13.3, 64.4, 4.5, 2.0, 73.4]),
    #100.0: np.array([25.4, 100.0, +10.0, 86.2, 3.9, 2.0, 98.6]),
    #200.0: np.array([25.4, 200.0, +5.0, 173.1, 2.9, 2.0, 199.0]),
    40.0 : np.array([25.4, 40, 25, 7.4, 7.5, 2.0, 34.7]),
    75.0: np.array([25.4, 75, 13.3, 32.5, 4.6, 2.0, 71.8]),
    100.0: np.array([25.4, 100.0, +10.0, 43.4, 3.9, 2.0, 97.3]),
    150.0: np.array([25.4, 150.0, 6.7, 65.1, 3.3, 2.0, 147.7]),
    200.0: np.array([25.4, 200, 5, 86.8, 2.9, 2.0, 198.0])
}

# Combine all dictionaries into one main dictionary
thorlabsFusedSilica = {
    "0.5 inch": lenses_0_5_inch,
    "1 inch": lenses_1_inch,
    "2_inch": lenses_2_inch,
    "Purchased": PurchasedFS,
    }

thorlabsCaF2 = {
    "1 inch": lenses_1_inch_caf2,
    "Purchased" : PurchasedCaF2,
    }

def WavelengthAdapter(wavelength, size = "1 inch"):
    lensDictFS = thorlabsFusedSilica[size]
    lensDictCaF2 = thorlabsCaF2[size]
    
    nWavelengthFS = FusedSilica(wavelength)
    nWavelengthCaF2 = CalciumFluoride(wavelength)
    
    trueFocals = trueFocal(lensDictFS, nWavelengthFS)
    trueFocals += trueFocal(lensDictCaF2, nWavelengthCaF2)
    return trueFocals


# Lens maker's formula function
def lensMaker(n, R1, R2):
    return 1 / ((n - 1) * (1 / R1 - 1 / R2))

# Function to calculate true focal lengths for each lens in the dictionary
def trueFocal(lens_dict, n):
    # Get the help key to understand the structure of the data
    keys = lens_dict["help"]
    
    # Initialize a dictionary to store the true focal lengths
    trueFocals = []

    # Iterate through each focal length in the dictionary
    for focal_length, data in lens_dict.items():
        if focal_length == "help":  # Skip the 'help' entry
            continue
        
        # Extract radius of curvature from the dictionary data
        R1 = data[keys.index("Radius of Curvature (mm)")]
        R1 = float(R1)
        R2 = np.inf  # For bi-convex lenses, R2 is typically -R1
        #R2 = -R1 
        # Calculate the true focal length using the lens maker's formula
        f_true = lensMaker(n, R1, R2)
        
        # Store the true focal length in the result dictionary
        trueFocals += [f_true]
    return trueFocals

if __name__ == "__main__":
    print(WavelengthAdapter(253))



































