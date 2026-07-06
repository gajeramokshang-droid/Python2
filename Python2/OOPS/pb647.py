# Sort following NumPy array
# Case 1: Sort array by the second row
# Case 2: Sort the array by the second column
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])

import numpy as np
sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
p1 = sampleArray[:, np.argsort(sampleArray[1])]
print(p1)

