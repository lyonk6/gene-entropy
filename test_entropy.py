# content of test_sample.py
from rna_entropy import calculate_shannon_information, calculate_shannon_entropy

naive_probabilities = {"a": 0.25, "g": 0.25, "c": 0.25, "u": 0.25}
short_nucleotide_list = ['a','g','c']


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


def test_calculate_shannon_information():
    # Case 1: The RNA sequence is invalid
    assert calculate_shannon_information(['a', 'b', 'c'], naive_probabilities) == -1    

    # The sequence is valid but the is all in lowercase. 
    assert calculate_shannon_information(['a', 'g', 'c'], naive_probabilities) == -1     

def test_calculate_shannon_entropy():
    # Case 1: The RNA sequence is invalid
    assert calculate_shannon_information(['a', 'b', 'c'], naive_probabilities) == -1
