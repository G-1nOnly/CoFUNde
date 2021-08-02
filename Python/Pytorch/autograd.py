import torch

x = torch.ones(2, 2, requires_grad=True)
# set requires_grad=True to track computation with it
print(x)
y = x + 2
print(y)

z = y * y * 3
out = z.mean()
print(z, out)
out.backward()  # Auto Jacobian since it's noe multidimensional
print(x.grad)

# Multidimensional tensor would need a vector v to instruct how to differentiate
X = torch.randn(3, 3, requires_grad=True)
Y = X * 2
v = torch.tensor([[0.1, 1.0, 0.0001], [0.1, 1.0, 0.0001], [0.1, 1.0, 0.0001]])
Y.backward(v)
print(X.grad)

# Stop the console from printing out the grad
print((X ** 2).requires_grad)
with torch.no_grad():
    print((X ** 2).requires_grad)

# Use detach to keep the same content but stop tracking
Y_new = Y.detach()
print(Y_new.requires_grad)

# Profile
a = torch.randn((1, 1), requires_grad=True)
with torch.autograd.profiler.profile() as prof:
    # _ means whatever number could be inserted since it won't be used
    for _ in range(100):
        b = a ** 2
        b = a*2
        b = a+2
        b.backward()
        b.grad
print(prof.key_averages().table())