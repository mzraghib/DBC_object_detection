'''
Process command-line arguments

'''
import argparse

def parse_opts():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--images', default='bdd100k/images', type=str, help='Input file path')
    parser.add_argument('--labels', default='bdd100k/labels', type=str, help='Input file path')

    parser.add_argument('--model', default='', type=str, help='Trained Model file path')
    
    # keep?
    parser.add_argument('--output', default='output.json', type=str, help='Output file path')
    
    parser.add_argument('--batch_size', default=32, type=int, help='Batch Size')
    args = parser.parse_args()
    return args