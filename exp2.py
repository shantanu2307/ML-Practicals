import numpy as np
a1= [[1,-2,3],[4,-5,6],[7,8,9]]
a2= [[2,3,4],[5,6,7],[8,9,10]]
a1=np.array(a1)
a2=np.array(a2)

#Printing absolute values
a1=np.absolute(a1)
print(a1)

#taking negatives
a1=np.negative(a1)
print(a1)

#adding rows 
row=[1,5,6]
a1=np.append(a1,[row],axis=0)
print(a1)

#adding coloums
coloumn=[[1],[2],[3],[4]]
a1=np.append(a1,coloumn,axis=1)
print(a1)

#removing first row
a1=np.delete(a1,0,0)
print(a1)

#removing coloumn 
a1=np.delete(a1,0,1)
print(a1)

#printing maximum along each coloumn
x=np.amax(a1,0)
print(x)

#printing maximum along each row
x=np.amax(a1,1)
print(x)

#printing minimum along each coloumn
x=np.amin(a1,0)
print(x)

#printing minimum along each row
x=np.amin(a1,1)
print(x)
