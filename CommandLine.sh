#!/bin/bash

# We have ran these commands on clean datasets after doing the required preprocessing and removing the commas (",") within hero's names and comic's names,
#as we find out that the csv file was reading the content wrongly on these cases. These clean datasets are hero-network-preprocessed.csv and edges_preprocessed.csv

#1. Most popular pair of heroes

echo 'The most popular pair of heros is:'
cut -d, -f1,2 hero-network-preprocessed.csv | sort | uniq -c | sort -nr | head -n 1

#ANSWER: The most popular pair of heros is:
#1267 PATRIOT/JEFF MACE,MISS AMERICA/MADELIN

#2. Number of comics per hero.

echo " "
echo 'The number of comics per hero is:'
cut -d, -f1 edges_preprocessed.csv | sort | uniq -c | sort -nr

#ANSWER:The number of comics per hero is:
#1577 SPIDER-MAN/PETER PARKER
#1334 CAPTAIN AMERICA
#1150 IRON MAN/TONY STARK
#...

#3. Average comics per hero:

echo 'The average number of heroes per comic is:'
cut -d, -f2 edges_preprocessed.csv | sort | uniq -c | sort -nr > comics_per_hero.csv
awk '{ total += $1 } END { print total/NR }' comics_per_hero.csv

##ANSWER: The average number of heroes per comic is:
#7.59663

