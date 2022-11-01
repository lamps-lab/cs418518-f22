#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 16:29:24 2022

@author: muntabir
"""
import urllib.parse, urllib.request, json
import pandas as pd

def CallWikifier(text, lang="en", threshold=0.9):
    # Prepare the URL.
    data = urllib.parse.urlencode([
        ("text", text), ("lang", lang),
        ("userKey", "ityrllrpggfrygeinxbascwnbhdbfp"),
        ("pageRankSqThreshold", "%g" % threshold), ("applyPageRankSqThreshold", "true"),
        ("nTopDfValuesToIgnore", "200"), ("nWordsToIgnoreFromList", "200"),
        ("wikiDataClasses", "true"), ("wikiDataClassIds", "false"),
        ("support", "true"), ("ranges", "false"), ("minLinkFrequency", "2"),
        ("includeCosines", "false"), ("maxMentionEntropy", "3")
        ])
    url = "http://www.wikifier.org/annotate-article"
    # Call the Wikifier and read the response.
    req = urllib.request.Request(url, data=data.encode("utf8"), method="POST")
    with urllib.request.urlopen(req, timeout = 60) as f:
        response = f.read()
        response = json.loads(response.decode("utf8"))
        
    # Output the annotations.
    wikiData = []
    for annotation in response["annotations"]:
        ann_terms_url =  '{"term": "%s", "url": "%s"}' % (annotation["title"], annotation["url"])
        term_url = json.loads(ann_terms_url)
        wikiData.append(term_url)
    return wikiData

## reading the .csv file
data = pd.read_csv("./data/metadata_abstract.csv")
list_ = []
## remove the list slicing [0:2] to iterate through each rows. This [0:2]
## means it will only fetch two rows and get the terms and urls of the abstract
for abstract in data['text'][0:2]:
    wikify = CallWikifier(abstract)
    wiki_list = list(wikify)
    list_.append(wiki_list)

res_list = [list(item) for item in list(zip(list_))]
dataframe = pd.DataFrame(res_list, columns = ['wiki_terms'])
dataframe.to_csv('wikifier.csv')

#######################################################
''' write a program below to merge wikifier.csv and 
metadata_abstract.csv file. Once you merged two csv files, 
save the final output to another .csv file so that it 
contains all the metadata, abstract, and wikiterms.
HINT: you can use pandas library to do this.
'''
######################################################