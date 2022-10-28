import matplotlib.pyplot as plt
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


def calculate_shannon_information(message, probability_map):
    """
    For each character in a message, look up its probability of
    appearing, then plug it into the logarithmic function:
        -1 * math.log(prob, base)

    Return the sum.
    """
    sum = 0
    for x in message:
        if x in probability_map:
            sum += probability_map[x]
            sum -= math.log(probability_map[x], 2)
    return sum

def calculate_shannon_entropy(message, probability_map):
    """
    For each character in a message, look up its probability of
    appearing, then plug it into the logarithmic function:
        prob * math.log(prob, base)

    Return the sum of character probabilities.
    """
    sum = 0
    for x in message:
        if x in probability_map:
            sum += probability_map[x] * math.log(probability_map[x], 2)
        else:
            print("Error. Character not allowed: ", x)
            return 0
    return 0 - sum


if __name__ == '__main__':  
    input_data       = get_lincoln_joyce_data()
    cleaned_data     = clean_ribozyme(input_data)
    nucleotide_list  = list(cleaned_data)

    plt.hist(list(nucleotide_list))
    plt.show()

    naive_probabilities = {"a": 0.25, "g": 0.25, "c": 0.25, "u": 0.25}
    short_nucleotide_list = ['a','g','c']

    entropy =  calculate_shannon_entropy(short_nucleotide_list, naive_probabilities)
    print("Entropy: ", entropy)

# for x in nucleotide_list:
# a_count = data.count('a')
# g_count = data.count('g')
# c_count = data.count('c')
# u_count = data.count('u')
