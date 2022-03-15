import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pymatgen.core import Structure
from pymatgen.io.cif import CifParser
from pymatgen.analysis.diffraction.xrd import XRDCalculator

calculator = XRDCalculator(
    wavelength="CuKa"
)

os.chdir("data")
maxes=set()
patterns = {}
for file in os.listdir():
    try: 
        structure = CifParser(file).get_structures()[0]
        xrd = calculator.get_pattern(structure)
    except Exception as e :
        print(e)
    maxes.add(xrd.y.max())
    patterns[file]= xrd.x,xrd.y
print(maxes)



