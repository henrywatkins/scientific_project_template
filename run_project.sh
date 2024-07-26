!#/usr/bin/env bash
# bash script to run project scripts
# projects generally consist of a set of sets, often encapsulated in scripts
# these could be data download and processing, followed by analysis and plotting
# collect the overall project run process using this bash script
DATA=/example/
python src/script1.py $DATA
python src/script2.py


