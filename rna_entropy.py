import math
import pandas as pd
import numpy as np
from get_data import get_combined_data

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
            sum += math.log(probability_map[x], 2)
        else:
            print("Error. Character not allowed: ", x)
            return -1
    return 0 - sum

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
            return -1
    return 0 - sum


if __name__ == '__main__':
    naive_probabilities = {"a": 0.25, "g": 0.25, "c": 0.25, "u": 0.25}

    myDF = get_combined_data()
    print(myDF)