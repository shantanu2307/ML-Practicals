import numpy as np
import pandas as pd

a1= [[1,2,3],[4,5,6],[7,8,9]]
a2= [[2,3,4],[5,6,7],[8,9,10]]
a1=np.array(a1)
a2=np.array(a2)


#Transpose of a matrix
a1=np.transpose(a1)
print(a1)

#Adding matrices 
b=np.add(a1,a2)
print(b)

#Substracting matrices
c=np.subtract(a1,a2)
print(c)

#Multiplying
d=np.dot(a1,a2)
print(d)
