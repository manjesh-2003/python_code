from scipy import linalg
import numpy as np

a= np.array([[7,2],[4,5]]) #this is the coefficient matrix
b= np.array([8,10]) #this is the constant matrix
x= linalg.solve(a,b) #this is the solution matrix       
print(x)