import os
import json
import numpy as np
from tqdm import tqdm 
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

<<<<<<< HEAD
def load_data(filename):
    os.chdir('/home/gonik/Documents/git/xrd_match')
    return pd.read_csv(filename)
    
=======
def load_data(file):
    return pd.read_csv(file)
>>>>>>> b290ef87164a61215fc46bd4e2190d67e30d3cd6

def filter_Zr():
    df=load_data("../2019-07-01-FSR-public_7061.csv")
    return [f"{row.filename}.cif"  for n,row in df.iterrows() if "Zr" in row["All_Metals"]]    

def filter_Zr():
    """
    Filter out structures with Zr
    """
    
    # os.chdir("")
    structure = load_data("2019-07-01-FSR-public_7061.csv")
    return [f"{row.filename}.cif" for n,row in df.iterrows() if "Zr" in row["All_Metals"]]


<<<<<<< HEAD


def main(filter = True):
    os.chdir("data")
    maxes=set()
    patterns = {}
    if filter:
        filenames = filter_Zr()
    else:
        filenames = os.listdir()
=======
def main(filter=True):
    os.chdir("data")
    if filter:
        filenames=filter_Zr()
    else:
        filenames=os.listdir()
    maxes=set()
    patterns = {}
>>>>>>> b290ef87164a61215fc46bd4e2190d67e30d3cd6
    for file in tqdm(filenames):
        try: 
            structure = CifParser(file).get_structures()[0]
            xrd = calculator.get_pattern(structure)
        except Exception as e :
            print(e)
<<<<<<< HEAD
        maxes.add(xrd.y.max())
        patterns[file]= xrd.x,xrd.y
    print(maxes)
    with open("diffraction_patterns.json","w") as file:
        json.dump(patterns,file)


if __name__ == "__main__":
    main()
=======
            continue
        maxes.add(xrd.y.max())
        patterns[file]= xrd.x.tolist(),xrd.y.tolist()
    print(maxes)
    with open("patterns.json","w") as file:
        json.dump(patterns,file)
    return filenames, patterns



if __name__=="__main__":
    fn,pt=main()
>>>>>>> b290ef87164a61215fc46bd4e2190d67e30d3cd6
