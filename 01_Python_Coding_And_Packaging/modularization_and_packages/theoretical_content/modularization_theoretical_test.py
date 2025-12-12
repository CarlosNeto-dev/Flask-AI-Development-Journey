"""explanatory archive on modularization content"""

import numpy as np

def multiplication_function(num1, num2):
    """
    :param num1: First parameter of function
    :param num2: Second parameter of function
    :return: The multiplication of these two parameters.
    """
    return num1 * num2


def array_range(start=0, stop=0, step=0):
    """
    :param start: The first parameter of function and starts the array.
    :param stop:  The second parameter of function and stop the array.
    :param step:  The third parameter of function and do the steps of array.
    :return: return the function np.arange(start, stop, step)
    """
    return np.arange(start, stop, step)