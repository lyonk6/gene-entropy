# content of test_sample.py
from rna_entropy import calculate_shannon_information, calculate_shannon_entropy

naive_probabilities = {"A": 0.25, "G": 0.25, "C": 0.25, "T": 0.25}


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


def test_calculate_shannon_information():
    # Case 1: The RNA sequence is invalid
    assert calculate_shannon_information(['a', 'b', 'c'], naive_probabilities) == -1

    # The sequence is valid but the is all in lowercase. 
    assert calculate_shannon_information(['a', 'g', 'c'], naive_probabilities) == -1

    # The sequence is valid.
    assert calculate_shannon_information(['A', 'G', 'C'], naive_probabilities) == 6

def test_calculate_shannon_entropy():
    # Case 1: The RNA sequence is invalid
    assert calculate_shannon_entropy(['a', 'b', 'c'], naive_probabilities) == -1

    assert calculate_shannon_entropy(['A', 'G', 'C'], naive_probabilities) == 1.5
