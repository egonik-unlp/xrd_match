import os
import json
import numpy as np
from tqdm import tqdm 
import pandas as pd
import matplotlib.pyplot as plt
from pymatgen.core import Structure
from pymatgen.io.cif import CifParser
from pymatgen.analysis.diffraction.xrd import XRDCalculator

calculator = XRDCalculator(
    wavelength="CuKa"
)

def load_data(filename):
    os.chdir('/home/gonik/Documents/git/xrd_match')
    return pd.read_csv(filename)
    


def filter_Zr():
    """
    Filter out structures with Zr
    """
    
    # os.chdir("")
    structure = load_data("2019-07-01-FSR-public_7061.csv")
    return [f"{row.filename}.cif" for n,row in df.iterrows() if "Zr" in row["All_Metals"]]




def main(filter = True):
    os.chdir("data")
    maxes=set()
    patterns = {}
    if filter:
        filenames = filter_Zr()
    else:
        filenames = os.listdir()
    for file in tqdm(filenames):
        try: 
            structure = CifParser(file).get_structures()[0]
            xrd = calculator.get_pattern(structure)
        except Exception as e :
            print(e)
        maxes.add(xrd.y.max())
        patterns[file]= xrd.x,xrd.y
    print(maxes)
    with open("diffraction_patterns.json","w") as file:
        json.dump(patterns,file)


if __name__ == "__main__":
    main()