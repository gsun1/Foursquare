#!/bin/bash

rm dictionary.txt results.txt regress.csv final.txt

python3 foursquare.py $1 $2 > dictionary.txt

python3 fstest.py dictionary.txt > results.txt

python3 analysis.py rest.txt results.txt > regress.csv

python3 logit.py > final.txt