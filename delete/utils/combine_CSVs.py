#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Combine a number of CSV files to a single CSV file
"""

import pandas as pd
import glob

input_dir = '/home/zuhayr/DBC2/DApp/data/ETH_Transactions/'
output_dir = '/home/zuhayr/DBC2/DApp/data/combined_ETH_transactions/'


start = 5491500
finish = 5499000


def open_single_csv(input_csv):
    
    # Read in .csv
    df = pd.read_csv(input_csv)
    
    return df


def open_mulitple_csv(input_dir):
    
    allFiles = glob.glob(input_dir + "/*.csv")
    frame = pd.DataFrame()
    list_ = []
    for file_ in allFiles:
        df = pd.read_csv(file_,index_col=None, header=0)
        list_.append(df)
    frame = pd.concat(list_)
    
    #reset indeces
    frame = frame.reset_index(drop=True)
    return frame


if __name__ == '__main__':

    df = open_mulitple_csv(input_dir)
    
    df.to_csv(output_dir + 'ETH_txs_{}_{}.csv'.format(start, finish), encoding='utf-8', index=False)   

    print('DONE')


    