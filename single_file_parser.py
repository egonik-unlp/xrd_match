#!/home/gonik/anaconda3/envs/xrd/bin/python

from pymatgen.io.cif import CifParser
from pymatgen.core.structure import Structure
from pymatgen.analysis.diffraction.xrd import XRDCalculator
import sys
import json
from datetime import datetime

class TimeoutError(Exception):
    pass











def main(file):
    try:
        start = datetime.now()
        print("file = {}".format(file))
        structure = CifParser(file).get_structures()[0]
        xrd = XRDCalculator().get_pattern(structure)
        pat = [xrd.x.tolist(), xrd.y.tolist()]
        file = file.split("/")[-1]
        fn = f"data/ip/{file[:-4]}.json"
        with open(fn, "w") as f:
            json.dump(pat,f)
        print(f"{file} -> {fn}")

    except Exception as e:
        print(e)














if __name__ == "__main__":
    main(sys.argv[1])


