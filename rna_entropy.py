import matplotlib.pyplot as plt
import numpy as np


def clean_ribozyme(raw):
    drop_chars = ['5','P','O','H','3','\'','-','\n']
    for x in drop_chars:
        print("Here is a x: ", x)
        raw = raw.replace(x, '')
    return raw


path = "data/lincoln_joyce/ribozyme.txt"


with open(path, 'r') as file:
    raw_data = file.read()


cleaned_data     = clean_ribozyme(raw_data)
nucleotide_list  = list(cleaned_data)

plt.hist(list(nucleotide_list))
plt.show()


# a_count = data.count('a')
# g_count = data.count('g')
# c_count = data.count('c')
# u_count = data.count('u')
