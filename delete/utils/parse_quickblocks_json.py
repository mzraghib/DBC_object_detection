"""
Parse the array of jsons' file and generate a .csv file with all the transaction data

"""

import json
import pandas as pd

# FILE NAMES
input_dir = '/home/zuhayr/DBC2/DApp/data/ETH_blocks/'
output_dir = '/home/zuhayr/DBC2/DApp/data/ETH_Transactions/'

input_json = input_dir + 'ETH_blocks_5491500_5492500.json'
output_csv = output_dir + 'ETH_txs_5491500_5492500.csv'



with open(input_json) as f:
    data = json.load(f)

''' create a dict copy without specific keys - stackoverflow '''
def without_keys(d, keys):
    return {x: d[x] for x in d if x not in keys}

''' make all values of a dictionary into lists, to be convert the dict to a dataframe '''
def listify(d):
    return {x: [d[x]] for x in d}


def extract_transaction_data(data):
    
    df_main = pd.DataFrame()
    flag = 0
        
    block_num = 1
    for block in data:

        all_transactions = block['transactions']
        for transaction in all_transactions:    
            
               
            transaction['value'] = float(transaction['value']) # too large for int
            t = without_keys(transaction, {'receipt'})
            df = pd.DataFrame(listify(t))           
            
            # base dataframe
            if(flag == 0):
                df_main = df
                flag = 1
                continue

            df_main = pd.concat([df_main,df])
            
        print(block_num)
        block_num += 1
        
    
    df_main.to_csv(output_csv, encoding='utf-8', index=False)   
    
    
if __name__ == '__main__':
    print('STARTED')
    extract_transaction_data(data)
    print('COMPLETED....CSV FILE IS READY')