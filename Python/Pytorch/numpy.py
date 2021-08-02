import torch
import numpy as np
a = np.ones(5)
b = torch.from_numpy(a)
np.add(a, 1, out=a)
print(a)
print(b)

x = torch.empty(5, 3)
print(x)   # We can not create empty matrix, so the matrix would be assigned to some initial values when created
x = x.new_ones(5, 3, dtype=torch.double)      # new_* methods take in sizes
print(x)

x = torch.randn_like(x, dtype=torch.float)    # override dtype!
print(x)      # result has the same size
print(x[:, 0])    # The first column of the matrix
