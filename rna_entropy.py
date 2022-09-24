import matplotlib.pyplot as plt
import numpy as np
import math

def clean_ribozyme(raw):
    drop_chars = ['5','P','O','H','3','\'','-','\n']
    for x in drop_chars:
        print("Here is a x: ", x)
        raw = raw.replace(x, '')
    return raw


def get_lincoln_joyce_data():
    path = "data/lincoln_joyce/ribozyme.txt"
    with open(path, 'r') as file:
        return file.read()



input_data       = get_lincoln_joyce_data()
cleaned_data     = clean_ribozyme(input_data)
nucleotide_list  = list(cleaned_data)


plt.hist(list(nucleotide_list))
plt.show()

naive_probabilities = {
    "a": 0.25,
    "g": 0.25,
    "c": 0.25,
    "u": 0.25
}

short_nucleotide_list = ['a','g','c']

# Calculate entropy: 
# for each character in a message, look up it's probability 
# value, then plug in to the following function:

# probability * math.log(probability, Base)
sum = 0
for x in short_nucleotide_list:
    sum += naive_probabilities[x] * math.log(naive_probabilities[x], 2)
sum = 0 - sum
print(sum)


# for x in nucleotide_list:
# a_count = data.count('a')
# g_count = data.count('g')
# c_count = data.count('c')
# u_count = data.count('u')
