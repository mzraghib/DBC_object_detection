#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 13:14:06 2018

@author: zuhayr

REAL TIME ANOMALY DETECTION



* Reusable framework 
* Data integrity - how to deal with NULLs, Malformed JSON etc.


"""
from datetime import datetime



def g_score():
    
    

    
def plot(column_name):
    #    df.plot(x='timestamp', y='gas', style='o')



def basic_metrics(df):
    # print start and end time
    print('start time ... ' + str(datetime.fromtimestamp(min(df['timestamp']))))

    print('end time ... ' + str(datetime.fromtimestamp(max(df['timestamp']))))