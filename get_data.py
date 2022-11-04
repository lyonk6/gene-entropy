import numpy as np
import math

def clean_ribozyme(raw):
    drop_chars = ['5','P','O','H','3','\'','-','\n']
    for x in drop_chars:
        raw = raw.replace(x, '')
    return raw.upper()

def get_lincoln_joyce_data():
    """
    Return a single rna ribozyme
    """
    path = "data/lincoln_joyce/ribozyme.txt"
    with open(path, 'r') as file:
        return file.read()

def get_mizuuchi_furubayashi_ichihashi_data():
    """
    Return a dictionary of rna ribozymes
    """
    path = "data/lincoln_joyce/ribozyme.txt"
    with open(path, 'r') as file:
        return file.read()



if __name__ == '__main__':  
    input_data       = get_lincoln_joyce_data()
    cleaned_data     = clean_ribozyme(input_data)
    nucleotide_list  = list(cleaned_data)

    plt.hist(list(nucleotide_list))
    plt.show()
