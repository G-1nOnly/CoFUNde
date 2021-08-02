import torch

x = torch.rand(5, 3)
y = torch.rand(5, 3)
print(x)
print(y)
result = torch.empty(5, 3)
torch.add(x, y, out=result)
print(result)
y_new = torch.rand(5, 3)
y_new.add_(x)  # inplace there exits a '_' in the structure
print(y_new)

matrix = torch.randn(3, 3)
print(matrix)
matrix = matrix.t()
print(matrix)
print(matrix.size())

z = torch.zeros(5, 3)
print(z)

t = torch.tensor([3, 4])
print(t)
