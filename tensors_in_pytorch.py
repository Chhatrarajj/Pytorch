# -*- coding: utf-8 -*-
"""Tensors in Pytorch.ipynb


import torch
print(torch.__version__)

if torch.cuda.is_available():
  print("GPU is available")
  print(f"Using GPU:{torch.cuda.get_device_name(0)}")
else:
  print("GPU is not available")

"""# Creating Tensors"""

#empty
a= torch.empty(2,3)

#check type
type(a)
type(b)

#using zeros
b=torch.zeros(3,3)

#using ones
torch.ones(3,3)

#using rand
torch.rand(2,3)

#use of weeds

#manual seed
torch.manual_seed(100)
torch.rand(2,3)

#tensors
torch.tensor([[1,2,3],[4,5,6]])

print(torch.arange(0,10,3))
print(torch.linspace(0,10,10))
print(torch.eye(3))
print(torch.full((3,3),5))

"""## **Tensor shapes**

"""

x = torch.tensor(([1,2,3],[4,5,6]))
x
x.shape

torch.empty_like(x)
x

torch.ones_like(x)
x

torch.zeros_like(x)
x

torch.rand_like(x,dtype=torch.float64)

"""# Tensor Data Types"""

x.dtype

torch.tensor([1.0,2.0,3.0],dtype=torch.int32)

torch.tensor([1,2,3,4],dtype=torch.float64)

x.to(torch.float64)

"""# Mathematical Operations

## 1.Scalar Operation
"""

y=torch.rand(2,2)
x

#addition
x+2
#sub
x-2
#mul
x*2
#div
x/2
#int divison
(x*100)//3
#mod
x%3
#pow
x**0

"""# Element Wise Operation"""

a = torch.rand(2,3)
b = torch.rand(2,3)
print(a)
print(b)

#add
a+b
#sub
a-b
#mul
a*b
#div
a/b
#pow
a**b
#mod
a%b

#abs
torch.absolute(a)

#negative
torch.neg(a)

torch.round(a)

torch.ceil(a)

torch.floor(a)

torch.clamp(a,min=0,max=5)

"""# 3.Reduction Operation"""

e = torch.randint(size=(2,3),low=0,high=10,dtype=torch.float32)
e

torch.sum(e)

torch.sum(e,dim=0)

torch.sum(e,dim=1)

torch.mean(e)

torch.mean(e,dim=0)

torch.mean(e,dim=1)

torch.median(e)

torch.max(e)

torch.min(e)

torch.prod(e)

torch.std(e)

torch.var(e)

torch.argmax(e)

torch.argmin(e)

"""# 4.Matrix Operations"""

f= torch.randint(size=(2,3),low=0,high=10)
g = torch.randint(size=(3,2),low=0,high=10)
print(f)
print(g)

#matrix multiplication
torch.matmul(f,g)

#dot prod
vector1=torch.tensor([1,2])
vector2=torch.tensor([3,4])
torch.dot(vector1,vector2)

print(f)
torch.transpose(f,0,1)

h = torch.randint(size=(3,3),low=0,high=10,dtype=torch.float32)
h

torch.det(h)

torch.inverse(h)

"""# 5. Comparsion Operation"""

i = torch.randint(size=(2,3),low=0,high=10)
j= torch.randint(size=(2,3),low=0,high=10)
print(i)
print(j)

#greater
i>j
#less
i<j
#equal
i==j
#not equal
i!=j

"""# 6.Special Functions"""

k = torch.randint(size=(2,3),low=0,high=10,dtype=torch.float32)
print(k)

#log
torch.log(k)

torch.exp(k)

torch.sqrt(k)

torch.sigmoid(k)

torch.softmax(k,dim=0)

torch.relu(k)

"""# Inplace Operations

Add "_" after any opertion for permanent operation
"""

m= torch.rand(2,3)
n= torch.rand(2,3)
print(m)
print(n)

m.add_(m+n)

print(m)

m.relu_()

m

"""# Copying Tensor"""

a = torch.rand(2,3)
a

b=a

b

b= a.clone()

b

a[0] [0]=0
a

b

id(a)

id(b)

"""# Tensor Operations on Gpu"""

torch.cuda.is_available()

device = torch.device('cuda')

#creating tensor in gpu
torch.rand((2,3),device=device)

#moving an existing tensor to GPU
a = torch.rand((3,3))
b=a.to(device)

b+5

"""# Reshaping"""

a = torch.ones(4,4)
a

a.reshape(4,2,2)

a.flatten()

b = torch.rand(2,3,4)
b

b.permute(2,0,1).shape

#typical image size
c= torch.rand(226,226,3)
c.unsqueeze(0).shape

d = torch.rand(1,20)
d.squeeze(0).shape

"""# Numpy And PYtorch"""

import numpy as np

a= torch.tensor([1,2,3])
a

b=a.numpy()

type(b)

c = np.array([12,23,34])

torch.from_numpy(c)

