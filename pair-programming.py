import numpy as np
def arr_to_arrscaled(arr):
    """ 
    Decription: Sceles an array to values from 0 to 1
    
    Paramerters
    _______
    input : numpy array
        Any numpy array of ints or floats
        
    Returns
    _______
    
    output : numpy array
        numpy array of floats that have a mximum value of 1.0
    
    Notes
    _______
    maps min to 0 and max to 1
    
    examples
    _______
    [1, 2, 3, 4, 5] -> [0, .25, .5, .75, 1]
    [-1, 0, 1] -> [0, .5, 1]

    """
    assert (type(arr) == np.ndarray and (arr.dtype == int or arr.dtype == float)), "Input must be an array of ints or floats"
    maximum = np.max(arr)
    minimum = np.min(arr)
    newarr = (arr-minimum)/(maximum-minimum)
    return newarr