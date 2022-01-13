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
