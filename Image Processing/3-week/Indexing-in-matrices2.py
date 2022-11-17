import numpy as np

A = np.array([ [ 1, 4,  5],
               [-5, 8,  9],
               [ 6, 8, 10],
               [ 0, 2, 38]])

print("Type = ", type(A))
print("A =", "\n", A, "\n")
print("A[1] = ", A[1])
print("A[1][2] = ", A[1][2])
print("A[0][-1] = ", A[0][-1])


# OUTPUT
# Type =  <class 'numpy.ndarray'>
# A =
#  [[ 1  4  5] 
#  [-5  8  9]  
#  [ 6  8 10]  
#  [ 0  2 38]] 

# A[1] =  [-5  8  9]
# A[1][2] =  9
# A[0][-1] =  5
