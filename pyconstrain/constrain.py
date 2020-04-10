import numpy as np

""" Constrains values of array or scalar to be in the range [a, b] inclusive
"""
def constrain(x, a, b):
    return np.clip(x, a, b)
