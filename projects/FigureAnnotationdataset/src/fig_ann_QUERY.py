#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 16:33:41 2022

@author: muntabir
"""


import mysql.connector as mysql
import configparser
import csv

config = configparser.ConfigParser()
config.read('DB.config')


#enter your server IP address/domain name
HOST = config['SERVER_CONFIG']['HOST']
# this is the user you create
USER = config['SERVER_CONFIG']['USER']
# user password
PASSWORD = config['SERVER_CONFIG']['PASSWORD']
# database name, if you want just to connect to MySQL server, leave it empty
DATABASE = config['DATABASE_CONFIG']['DATABASE']

#Update the original ETD tabel name and the Shadow table name here
tablename = config['DATABASE_CONFIG']['TABLE']

db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)

print("Connected to:", db_connection.get_server_info())
mycursor = db_connection.cursor()


query = 'SELECT * FROM figure_segmented_nipseval_test2007;'
mycursor.execute(query)
rows = mycursor.fetchall()

def tuplesTolist(tuple_text):
    list_ = []
    for values in tuple_text:
        fig_ann = list(values)
        list_.append(fig_ann)
    
    return list_

record = tuplesTolist(rows)
csvfile = open('fig_ann.csv', 'w')
writer = csv.writer(csvfile)
writer.writerow(['id', 'patentID', 'patentdate', 'figid', 'caption', 'object', 'aspect', 'figure_file', 'subfigure_file', 'object_title', 'groupID'])

for data in record:
    writer.writerow(data)

csvfile.close()
    
