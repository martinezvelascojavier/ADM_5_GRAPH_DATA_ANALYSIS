#!/bin/bash

# We suggest running these commands on the clean dataset after preprocessing

#1. Most popular pair of heroes

echo 'The most popular pair of heros is:'
cut -d, -f1,2 hero-network.csv | sort | uniq -c | sort -nr | head -n 1
#there are some outputs that dont come in pairs. Head 11 is the correct one

#2. Number of comics per hero.

echo " "
echo 'The number of comics per hero is:'
cut -d, -f1 edges.csv | sort | uniq -c | sort -nr

#3. Average comics per hero:

echo 'The average number of heroes per comic is:'
cut -d, -f2 edges_df2.csv | sort | uniq -c | sort -nr > comics_per_hero.csv
awk '{ total += $1 } END { print total/NR }' comics_per_hero.csv
#The average number of heroes per comic is:
#7.59663
#edges_df2 is a exact copy of edges.csv, but commas have been replaced with "", 
#because they were causing problems when computing the mean, as the csv file 
#interprete wrong commas within heros names.
