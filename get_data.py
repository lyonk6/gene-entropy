import matplotlib.pyplot as plt
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
        return clean_ribozyme(file.read())

def get_mizuuchi_furubayashi_ichihashi_data():
    """
    Return a dataframe of rna ribozymes
    """
    path = "data/mizuuchi_furubayashi_ichihashi/ribozymes.csv"
    return pandas.read_csv(path)

def get_combined_data():
    df = get_mizuuchi_furubayashi_ichihashi_data()
    lincoln_joyce_data = {'Name': ['joyce-00'], 'Sequence': [get_lincoln_joyce_data()]}
    lincoln_joyce_data = pandas.DataFrame(lincoln_joyce_data)
    return pandas.concat([df, lincoln_joyce_data], ignore_index = True)

def plot_nucleotide_distribution(df):
    """
    Pass a string of nucleotids and display the 
    count of each in a histogram.
    """
    s = ''
    for index, row in df.iterrows():
        s += row['Sequence']
    plt.hist(list(s))
    plt.show()
