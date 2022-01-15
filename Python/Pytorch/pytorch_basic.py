import torch
import numpy as np

data = [[1,2],[3,4]]
tensor1 = torch.tensor(data,dtype=torch.float64)
print(tensor1)
tensor2 = torch.from_numpy(np.array([3,4]))
print(tensor2)
print(torch.rand_like(tensor1,dtype=torch.float))
print(torch.ones_like(tensor1))
print(tensor1.device)

if torch.cuda.is_available():
    tensor1.to('cuda')
    print(tensor1.device)
    
tensor3 = torch.tensor([[1,2,3],[1,2,3]])
tensor3_cat = torch.cat([tensor3,tensor3,tensor3],dim = 0) # dim = 0 row dim = 1 column
print(tensor3_cat)

print(tensor3.mul(tensor3)) # Coulde be replaced by *
print(tensor3.matmul(tensor3.T)) # Could be replaced by @

x = torch.tensor(data) 
print(x.t_())
print(x.add_(5))  # Operations that have a _ suffix are in-place
n = x.numpy() # Share the location same as from_numpy()
print(type(n))
print(x.add_(1))
print(n)
np.add(n,1,out=n)
print(x)
print(n)

a = torch.tensor([[1.], [2.] , [3.] , [-1.], [-2.] ,[-3.]])
std = torch.std(a)
print(std)
torch.clamp(a, min=-1,max=2,out=a)
print(a)

print(type(torch.max(a)))
print(type(torch.max(a).item())) 
# After applying item, the return type would be the original type stored in the tensor

v1 = torch.tensor([1., 0., 0.])
v2 = torch.tensor([0., 1., 0.])
v3 = torch.cross(v1,v2) # Cross product
print(v3)

m1 = torch.rand(2,2)
m2 = torch.tensor([[3., 0.],[0., 3.]])
m3 = m1@m2
print(m3)
print(torch.svd(m3)) #Singular Value Decomposition

x = torch.tensor([[1, 2, 3], [4, 5, 6]])
y = x
y[0][0] = 0 # Share the same memory
print(x)
z = x.clone()  
z[0][0] = 1
print(x)

# Note that if autograd is enabled, so does the cloned object
t = torch.tensor([[1., 2., 3.], [4., 5., 6.]],requires_grad=True)
t1 = t.clone()
# Use detach() to disabled autograd
print(t1.requires_grad)
t2 = t.detach().clone()
print(t2.requires_grad)

# The function unsqueeze may be useful to add the batch-size dimension
b = torch.rand(3, 256, 256)
c = b.unsqueeze(0) # Add to the 0 dimension
print(b.shape)
print(c.shape)
