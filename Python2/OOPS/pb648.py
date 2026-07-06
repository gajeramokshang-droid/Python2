# Print max from axis 0 and min from axis 1 from the following 2-D array.
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])

import numpy as np
sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])

arr=sampleArray.max(axis=0)
print(arr)

arr1 = sampleArray.min(axis=1)
print(arr1)

