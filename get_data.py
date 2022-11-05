import matplotlib.pyplot as plt
import numpy as np
import pandas

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
    path = "data/mizuuchi_furubayashi_ichihashi/ribozymes.txt"
    return pandas.read_csv(path)

def get_combined_data():
    df = get_mizuuchi_furubayashi_ichihashi_data()
    df.append({})

    return

def plot_nucleotide_distribution():
    """
    Pass a string of nucleotids and display the 
    count of each in a histogram.
    """
    plt.hist(list(nucleotide_list))
    plt.show()


if __name__ == '__main__':  
    input_data       = get_lincoln_joyce_data()
    cleaned_data     = clean_ribozyme(input_data)
    nucleotide_list  = list(cleaned_data)

    rna_df = get_mizuuchi_furubayashi_ichihashi_data()
    print(rna_df)