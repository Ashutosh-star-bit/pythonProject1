import pandas as pd
import numpy as np
na = pd.Series(data = [1 , 2 , 3 , 4 ,5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 ,np.NaN,np.NaN,np.NaN],\
               index=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o'])
na.name="Ashutosh" # can be used to get or set the name of a series object
na.index.name="Ash" # can be used to assign new name to index
print(na)
print(na.index) # The index(axis labels) of the series
print(na.values) # Return series as ndarray or ndarray-like depending on the dtype
print(na.dtype) # return the dtype object of the underlying data
print(na.shape) # Return number of elements it contains including missing or empty values(NaNs)
print(na.nbytes) # To know total number of bytes taken by Series object data
print(na.ndim) # To know total the dimension (number of axis)
print(na.size) # To know about the number of element in the Series object
print(na.hasnans) # Return True if there are any NaN values; otherwise return False
print(na.empty) # Return true if the Series object is empty , false otherwise

print("ALL TYPE OF SERIES OBJECT ATTRIBUTES ")