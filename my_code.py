import numpy as np
#this code is for understanding the eigen values and eigen vectors
A= np.array([[3,1],[0,2]])

eigenvalues , eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)