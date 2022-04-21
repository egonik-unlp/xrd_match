#!/usr/bin/env bash

echo "Starting program"


TCNT="$(ls -1 data/*.cif | wc -l)"
CNT=1
for filename in data/*.cif; do
    echo "Processing $filename, $CNT of $TCNT"
    ./single_file_parser.py $filename
    let CNT=CNT+1
done


