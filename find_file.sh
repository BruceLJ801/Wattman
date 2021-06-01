#!/bin/bash 
#write by lijia 
#2021.06.01

#find . -type f -name "*_gt.json" |xargs ls

echo "This is a script to find all the files that contains a keyword!"

echo "The numbers of keyword is:"
find . -name "*_gt.json" |wc -l
