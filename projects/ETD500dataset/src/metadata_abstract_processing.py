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
import re
import ast


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
#ETDmetadata.to_csv("metadata.csv")


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
fileid = fileid.iloc[1: , :]
fileid.to_csv("./data/file_id.csv", index = None)

## Reading the ETDabstract500 file and processing text column (i.e., abstract)  
data = pd.read_csv('ETDabstract500.csv')
data = data.drop("file_idx", axis =1)
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
rows with same id. Then join all the string elements in a list.
'''
## Preprocessing based on ETD file id

def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list


df1 = pd.read_csv("./data/abstract.csv")
df1['text'] = df1.groupby(['etd_file_id'])['text'].transform(lambda x : ','.join(x))
df1 = df1.drop_duplicates()
df1.to_csv("./data/abstract_output.csv", index = None) 

## Further preprocessing of string elements in a list. 
## We are joining fragments of strings whihc are comma separated
list_data = []
for texts in df1['text']:
    abstract = ast.literal_eval(str(texts))
    abs_text = [items for items in abstract]
    abs_text_list = flatten_list(abs_text)
    list_data.append(abs_text_list)

data = zip(list_data)
dataframe = pd.DataFrame(data)


list_abs = []
for items in dataframe[0]:
   vals = [ ' '.join(element.lstrip().rstrip().split('  ')) for element in items]
   vals_str = ' '.join(vals)
   list_value = [vals_str]
   list_abs.append(list_value)
   

data2 = zip(list_abs)
dataframe2 = pd.DataFrame(data2, columns = ['text'])
dataframe3 = pd.read_csv("./data/abstract_output.csv")

file_id = dataframe3['etd_file_id']
abstract_text = dataframe2['text']

res_list = [list(item) for item in list(zip(file_id, abstract_text))]
output = pd.DataFrame(res_list, columns = ['etd_file_id', 'text'])
output.to_csv("./data/abstract_output_final.csv", index = None)


## Combining metadata and abstract
data1 = pd.read_csv('metadata.csv')
data2 = pd.read_csv('./data/abstract_output_final.csv')


## Using merge function by setting how='left'
final_out = pd.merge(data1, data2, 
                   on='etd_file_id', 
                   how='left')

final_out.to_csv("./data/metadata_abstract.csv", index = None)