import os
import numpy as np
import pandas as pd
import json
from tqdm import tqdm
import matplotlib.pyplot as plt
from pymatgen.core import Structure
from pymatgen.io.cif import CifParser
from pymatgen.analysis.diffraction.xrd import XRDCalculator

calculator = XRDCalculator(
    wavelength="CuKa"
)

def load_data(file):
    return pd.read_csv(file)

def filter_Zr():
    df=load_data("../2019-07-01-FSR-public_7061.csv")
    return [f"{row.filename}.cif"  for n,row in df.iterrows() if "Zr" in row["All_Metals"]]    



def main(filter=True):
    os.chdir("data")
    if filter:
        filenames=filter_Zr()
    else:
        filenames=os.listdir()
    maxes=set()
    patterns = {}
    for file in tqdm(filenames):
        try: 
            structure = CifParser(file).get_structures()[0]
            xrd = calculator.get_pattern(structure)
        except Exception as e :
            print(e)
            continue
        maxes.add(xrd.y.max())
        patterns[file]= xrd.x.tolist(),xrd.y.tolist()
    print(maxes)
    with open("patterns.json","w") as file:
        json.dump(patterns,file)
    return filenames, patterns



if __name__=="__main__":
    fn,pt=main()