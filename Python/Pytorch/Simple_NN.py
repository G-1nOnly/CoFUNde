import torch
import torch.optim as optim
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt

class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.conv1 = nn.Conv2d(1,6,5)
        self.conv2 = nn.Conv2d(6,16,5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120,84)
        self.fc3 = nn.Linear(84,10)
        
    def forward(self,x):
        x = F.max_pool2d(F.relu(self.conv1(x)),(2,2))
        x = F.max_pool2d(F.relu(self.conv2(x)),2)
        x = torch.flatten(x,1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
    


net = Net()
input = torch.randn(1,1,32,32)
out = net(input)
target = torch.randn(10)
target = target.view(1,-1)
criterion = nn.MSELoss()
loss = criterion(out,target)
print(loss)

optimizer = optim.SGD(net.parameters(),lr=1e-2,momentum=0.8)

loss_ls = []
i = []
for iter in range(100):
    i.append(iter)
    optimizer.zero_grad() # Clear the buffer
    output = net(input)
    loss = criterion(output,target)
    loss_ls.append(loss)
    if (loss<1e-4):
        break
    loss.backward()
    optimizer.step()

plt.plot(i,loss_ls)
plt.show()