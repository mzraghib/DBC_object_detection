#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 14:45:27 2018

@author: zuhayr
"""

import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--root_path',
        default='/home/zuhayr/DBC2/DApp',
        type=str,
        help='Root directory path of data')
    
    parser.add_argument(
        '--window_path',
        default='/data/combined_ETH_transactions/',
        type=str,
        help='Directory path for data in the window segment')
    
    parser.add_argument(
        '--block_path',
        default='/data/block_ETH_transaction_test/',
        type=str,
        help='Root directory path of data')    
    
    parser.add_argument(
        '--output_path',
        default='output.json',
        type=str,
        help='Output path')
   
    parser.add_argument(
        '--window_size',
        help='size of window time frame in days')
    parser.set_defaults(window_size=1)
    
    parser.add_argument(
        '--test_size',
        help='size of test window time frame in blocks')
    parser.set_defaults(test_size=1)


    args = parser.parse_args()

    return args