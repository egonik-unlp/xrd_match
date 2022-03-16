import os
import json
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
file = "diffraction_patterns.json"


def load_data(file):
    with open(file) as f:
        data = json.dump(f)
    return file

def find_peaks_and_get_index(theta, intensity):
    peaks = sp.signal.find_peaks(intensity)
    return peaks, theta[peaks]


def parse_data(dataset):
    """
    Parse the data from the json file
    """
    data = load_data(dataset)
    parsed_data = {}
    for filename, key in data.items():
    
        theta = data[key][0]
        intensity = data[key][1]
        peaks, theta_peaks = find_peaks_and_get_index(theta, intensity)
        parsed_data[filename] = theta_peaks
    return parsed_data


def match_data_to_target(target_file):
    """
    Match the data to the target file
    """
    differences = {}
    peaks_from_mof = parse_data(target_file)
    theta_tgt,intensity_tgt = load_data(target_file)
    target_peaks, target_theta_peaks = find_peaks_and_get_index(theta_tgt, intensity_tgt)
    for filename, key in peaks_from_mof.items():
        dif = target_theta_peaks - key
        differences[filename] = dif.sum()
    with open("differences.json","w") as file:
        json.dump(differences,file)

    return differences



         
        
