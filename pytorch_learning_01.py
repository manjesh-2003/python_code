import torch

#create a tensors
a= torch.tensor([1.0,2.0,3.0]) #default CPU tensor
b= torch.tensor([[1,2],[3,4]], dtype=torch.float32)

#Tensor operations
print(a+2) #element wise addition
print(b.T) #transpose of a tensor

#for gradient calculation
x= torch.tensor(2.0, requires_grad=True)
y= x**2 + 3*x + 2 #function
y.backward() #compute dy/dx
print(x.grad) #print 7 (derivative at x=2)
