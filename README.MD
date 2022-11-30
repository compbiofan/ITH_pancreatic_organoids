This repository contains scripts for paper ***Genomic heterogeneity in pancreatic cancer organoids and its stability with culture*** by Jerome Irianto, Olalekan Usman, Liting Zhang, Gengqiang Xie, Hemant Kocher, Chang-Il Hwang, Yue Wang, and Xian Mallory.

`merge_segs.py`:
  Merge consecutive copy number segments with same copy number into one larger segment for all cells from one phase. The output will be used to generate a maximum parsimony tree using PAUP. 
 
 `cal_distance`:
  This file find the smallest copy number edit distance to attach the cells from another later phase to the cells on the copy number tree inferred from previous step. This file will output where are the later phase cells attached to and the relative distance. 
  
  
