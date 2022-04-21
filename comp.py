

import json
import os
from scipy.signal import find_peaks 
import numpy as np
import pandas as pd
from pymatgen.io.cif import CifParser
import matplotlib.pyplot as plt
from pymatgen.analysis.diffraction.xrd import XRDCalculator

calculator = XRDCalculator(
    wavelength="CuKa"
)





stru_comp = CifParser('data/ja406844r_si_002_freeONLY.cif').get_structures()[0]
xrd_comp = calculator.get_pattern(stru_comp)


xrd_tgt = pd.read_csv("xe.dat").to_numpy().T


xt,yt = xrd_tgt

yt = yt * 100


xc,yc = xrd_comp.x,xrd_comp.y



plt.plot(xt,yt, label = "target")
plt.plot(xc,yc, label = "mas similar")
plt.legend()
plt.show()