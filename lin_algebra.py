from scipy import linalg
import numpy as np

a= np.array([[5,3,10],[3,1,0]]) #this is the coefficient matrix
b= np.array([8,10]) #this is the constant matrix
x= linalg.solve(a,b) #this is the solution matrix       
print(x)