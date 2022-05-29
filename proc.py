import json 
from sklearn.decomposition import PCA
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, Normalizer, MinMaxScaler
from scipy.signal import find_peaks








def load_file(file):
    with open(file) as f:
        data = json.load(f)
    return data

scaler = StandardScaler()

def find_peaks_for_all_files(peak_file = "patterns.json",height=1, scaler = scaler):
    """
    Find the peaks for all the files in the json file
    """

    data = load_file(peak_file)
    pks = {}
    for file, (x,y) in data.items():
        x,y = np.array(np.vstack([x,y]))
        scaler.fit_transform(y.reshape(-1,1))
        idxs, mdata = find_peaks(y, height=height)
        pks[file] = x[idxs], mdata["peak_heights"]
    return pks


def main():
    return find_peaks_for_all_files()



if __name__ == "__main__":
    rv = main()
        