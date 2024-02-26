import numpy as np
def arr_to_arrscaled(arr):
    #The documentation and function look neat and have all of the components
    #The function works properly
    #The examples header should be capitalized like the rest of the headers
    #The spelling of scales should be fixed from sceles to scales
    #The spelling of parameters should be fixed from paramerters to parameters
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

def test_arr_to_arrscaled():
    assert all(arr_to_arrscaled(np.array([1, 2, 3, 4, 5])) == [0, 0.25, 0.5, 0.75, 1]), "Test 1 failed"
    assert all(arr_to_arrscaled(np.array([1, 2, 3, 4, 5])) == [0, 0.25, 0.5, 0.75, 1]), "Test 2 failed"
    assert all(arr_to_arrscaled(np.array([5, 3, 4, 2, 1])) == [1, .5 , .75, .25, 0]), "Test 3 failed"
    assert all(arr_to_arrscaled(np.array([-1, 0, 1])) == [0, .5, 1]), "Test 4 failed"                       
    print("Passed all tests")