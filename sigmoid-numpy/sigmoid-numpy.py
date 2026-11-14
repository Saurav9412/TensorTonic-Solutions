import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    x = np.array(x)
    # Write code here
    neg_x = - x
    return 1 / ( 1 + (np.exp(neg_x)))