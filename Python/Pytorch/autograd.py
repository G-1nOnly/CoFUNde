import torch
import torchvision

x = torch.tensor([2.,3.],requires_grad=True)
y = torch.tensor([6.,4.],requires_grad=True)
Q = 3*x**3 - y**2
g = torch.tensor([1,1],dtype=torch.float) # Only float type could be calculated grad
Q.backward(gradient=g)
print(x.grad, y.grad)

x = torch.tensor([1], dtype=torch.float, requires_grad=True)
# no_grad() thread local
with torch.no_grad():
    y = x**2
print(y.requires_grad)   
y = x.pow(2)
print(x is y.grad_fn._saved_self) 
y = x.exp()
print(y is y.grad_fn._saved_result)
print(y.equal(y.grad_fn._saved_result))

model = torchvision.models.resnet18(pretrained=True)
data = torch.rand(1,3,64,64)
labels = torch.rand(1,1000)
prediction = model(data)
loss = (prediction-labels).sum()
loss.backward()
optim = torch.optim.SGD(model.parameters(),lr=1e-2,momentum=0.9)
optim.step()

model_new = torchvision.models.resnet18(pretrained=True)

# Freeze all the parameters in the network
for param in model_new.parameters():
    param.requires_grad = False
    
model_new.fc = torch.nn.Linear(512, 10)
optimizer = torch.optim.SGD(model_new.parameters(), lr=1e-2, momentum=0.9) # Only optimize the classifier
