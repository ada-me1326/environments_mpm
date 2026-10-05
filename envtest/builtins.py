import numpy as np
from scipy.ndimage import gaussian_filter
import pandas

__all__ = ['rand_array', 'smooth_image', 'my_mat_solve', 'panda_dummy'] #shows what is available to import from this file 


def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)

def my_mat_solve(A, b):
    return A.inv()*b

def panda_dummy(mydataset):
    myvar = pandas.DataFrame(mydataset)
    print(myvar)