
import json
import os
from scipy.signal import find_peaks 
import numpy as np
import pandas as pd
from pymatgen.io.cif import CifParser
import matplotlib.pyplot as plt

file="patterns.json"


def load_patterns(file):
    with open(file) as f:
        data=json.load(f)
    return data



def find_peaks_and_get_index():
    data = load_patterns(file)
    peaks = {}
    for key,value in data.items():
        theta,intensity = value
        pks=find_peaks(intensity,height=0.1)[0] # no me importan los valores de intensidad
        peaks[key]=np.array(theta)[pks].tolist()
    return peaks


def compare_pattern_to_target(peaks,target="xe.dat", epsilon=1):
    retval= {}
    target_theta, target_intensity=pd.read_csv(target).to_numpy().T
    target_peaks=find_peaks(target_intensity,height=0.1)[0]
    target_peaks_theta=target_theta[target_peaks]
    for fname,peaklist in peaks.items():
        matches=(peaklist - target_peaks_theta.reshape(-1,1) < epsilon).sum()
        retval[fname]=int(matches)
    return retval



def main():
    peaks=find_peaks_and_get_index()
    matches=compare_pattern_to_target(peaks)
    data_final={
        "peaks":peaks,
        "matches":matches
    }
    # with open("finaldump.json", "w") as f:
    #     json.dump(data_final,f)
    
    return data_final




if __name__=="__main__":
    data=main()
