#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:00:19 2022

@author: muntabir
"""
import pandas as pd
import numpy as np
import glob
import os
import warnings
import csv
import re

warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

# Path to the ground truth metadata which is parsed from library repo
file_path = os.path.join("/Users/muntabir/Documents/etdExtraction/etd_crf_result/orig-metadata/", "*.csv")
files = sorted(glob.glob(file_path))

## Reading all the csv files in a directory
dataframe = list(map(pd.read_csv, files))

## concatanating all the csv files
dfList = []
colname = ['advisor', 'advisor-vis', 'author', 'degree', 'program', 'program-vis', 'title', 'university', 'year']
df = pd.DataFrame(dataframe)
dfList.append(df)
ETDmetadata = pd.concat(dataframe, axis = 1)
ETDmetadata.columns=colname
ETDmetadata.to_csv("metadata.csv", index = None)


'''
Processing the ETD500 abstract file which contains file_id, text, bbox, and class name
Using ETDSegmentation tool to parse and get the abstract related data
'''

## Reading the ETDabstract500 file and processing file_idx column
with open('ETDabstract500.csv', 'r') as infile:
    
    fileID_ = []
    for fileid in infile.readlines():
        fields = fileid.split(',')[1]
        fileID_process = fields.lstrip('"File Name:td')
        fileID = re.sub(r'_page.*', "", fileID_process)
        fileID_.append(fileID)
        
## Saving the processed file_id result
fileid = pd.DataFrame(fileID_, columns = ['etd_file_id'])
fileid = fileid.iloc[1: , :] ## removing first row
fileid.to_csv("./data/file_id.csv", index = None)

## Reading the ETDabstract500 file and saving only text column (i.e., abstract)  
data = pd.read_csv('ETDabstract500.csv')
data = data.drop("file_idx", axis =1)
data = data.drop("bbox", axis =1)
data = data.drop("class", axis =1)
data = data.drop("Unnamed: 0", axis =1)
data.to_csv("./data/abstract_text.csv", index = None)

## Merging processed file_id and abstract text
file_id = pd.read_csv('./data/file_id.csv')
abstract = pd.read_csv('./data/abstract_text.csv')
merge_file = pd.concat([file_id, abstract], axis = 1)
merge_file.to_csv('./data/abstract.csv', index = None)

'''
A lot of ETD does not contain abstract and a lot ETD Abstract is 2-3 pages long.
So, ETD abstract which is 2-3 pages long, they belongs to same id. 
We need to further preprocess the "abstract.csv" file. We are merging or combining 
rows with same id.
'''
## Preprocessing based on ETD file id
dict_ = {}
with open('./data/abstract.csv') as f:
    reader = csv.reader(f)
    for idx, text in reader:
        temp = dict_.get(idx, "")
        dict_[idx] = temp+" "+text if temp else text

df_abs_idx_process = pd.Series(dict_)
df_abs_idx_process.to_csv("./data/abstract_output.csv", header = False)

## Combining metadata and abstract
data1 = pd.read_csv('metadata.csv')
data2 = pd.read_csv('./data/abstract_output.csv')

## Using merge function by setting how='left'
output = pd.merge(data1, data2, 
                   on='etd_file_id', 
                   how='left')

output.to_csv("./data/metadata_abstract.csv", index = None)