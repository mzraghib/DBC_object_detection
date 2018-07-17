#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 14:43:14 2018

@author: zuhayr



    Main function - STATIC window - batch detection (NOT STREAMING )

    Returns
    
    * annoted datapoints that seem anomalous
    * 
    
    

"""


from arg_parser import parse_args
import pandas as pd
from utils.combine_CSVs import open_mulitple_csv
from AD_methods.methods1 import KNN, method1


def load_data(path):
    '''
    Load input window data into a dataframe
    '''
    df = open_mulitple_csv(args.root_path + path)
    return df

def main(df_block, df_window, args):
    '''

    
    '''

    
    res = KNN(f_block, df_window, args)
    #TODO: rename method1.py
    res1 = method1(df_block, df_window, args)
  
    # read in input window data    
    df.plot(x='timestamp', y='value', style='x')    
    
    
    
    
    
    
    
    

if __name__ == '__main__':
    # read command line args
    args = parse_args()

    
    df_window = load_data(args.window_path)
    df_block = load_data(args.block_path)
    

    main(df_block, df_window, args)
