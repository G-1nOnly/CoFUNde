from __future__ import print_function
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader
import torchvision
import torchvision.datasets as datasets
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
import six

class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

        # Spatial transformer localization-network
        self.localization = nn.Sequential(
            nn.Conv2d(1, 8, kernel_size=7),
            nn.MaxPool2d(2, stride=2),
            nn.ReLU(True),
            nn.Conv2d(8, 10, kernel_size=5),
            nn.MaxPool2d(2, stride=2),
            nn.ReLU(True)
        )

        self.fc = nn.Sequential(
            nn.Linear(10 * 3 * 3, 32),
            nn.ReLU(True),
            nn.Linear(32, 3 * 2)
        )

        # Initialize the weights/bias with identity transformation
        self.fc[2].weight.data.zero_()
        self.fc[2].bias.data.copy_(torch.tensor([1., 0., 0., 0., 1., 0.]))


    def forward(self, x):
        x = self.stn(x)
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        
        return F.log_softmax(x, dim=1)
    
    def stn(self, x):
        x_t = self.localization(x)
        x_t = x_t.view(-1, 10 * 3 * 3)
        theta = self.fc(x_t)
        theta = theta.view(-1, 2, 3)

        grid = F.affine_grid(theta, x.size(),align_corners=True)
        x = F.grid_sample(x, grid,align_corners=True)

        return x


def train(epoch,device,train_loader,model,optimizer,criterion):
    model.train()
    train_loss = []
    for e in range(epoch):
        for iter,(data,target) in enumerate(train_loader):
            data, target = data.to(device), target.to(device)
            
            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output,target)
            loss.backward()
            optimizer.step()
            
            if iter == len(train_loader)-1:
                print('Train Epoch: {} \tLoss: {:.6f}'.format(e+1,loss.item()))   
            train_loss.append(loss.item())
                
        if e == epoch-1:
            print("\n")
            print('-'*20)
            print("Training finished!!!")
            print('-'*20)
                
    return train_loss  
        
        
def test(device,test_loader,model,criterion):
    with torch.no_grad():
        model.eval()
        test_loss = 0
        correct = 0
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            
            test_loss = test_loss + criterion(output, target).sum().item()
            pred = output.max(1, keepdim=True)[1]
            correct = correct + pred.eq(target.view_as(pred)).sum().item()

        test_loss = test_loss/len(test_loader.dataset)
        print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'
              .format(test_loss, correct, len(test_loader.dataset),
                      100. * correct / len(test_loader.dataset)))
        
def image_conversion(img):
    """Convert a Tensor to numpy image."""
    img = img.numpy().transpose((1, 2, 0))
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    img = std * img + mean
    img = np.clip(img, 0, 1)
    return img
 
def loss_plot(train_loss):
    plt.figure(figsize=(8, 5))
    plt.title("Loss During Training")
    plt.plot(train_loss, label="Train")
    plt.xlabel("iterations")
    plt.ylabel("Loss")
    plt.legend()
    plt.show()
        
def visualize_stn():
    with torch.no_grad():
        # Get a batch of training data
        data = next(iter(test_loader))[0].to(device)

        input_tensor = data.cpu()
        transformed_input_tensor = model.stn(data).cpu()

        in_grid = image_conversion(torchvision.utils.make_grid(input_tensor))

        out_grid = image_conversion(torchvision.utils.make_grid(transformed_input_tensor))

        # Plot the results side-by-side
        _, axarr = plt.subplots(1, 2)
        axarr[0].imshow(in_grid)
        axarr[0].set_title('Dataset Images')

        axarr[1].imshow(out_grid)
        axarr[1].set_title('Transformed Images')
        plt.ioff()
        plt.show()
        
                
if __name__ == '__main__':
    plt.ion()
    opener = six.moves.urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    six.moves.urllib.request.install_opener(opener)

    device = torch.device('cuda'  if torch.cuda.is_available() else 'cpu')

    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
        ])
    train_set = datasets.MNIST(root='./MNIST',train=True, transform=transform, download=True)
    train_loader = DataLoader(train_set,batch_size=64,shuffle=True,num_workers=4)
    test_set = datasets.MNIST(root='./MNIST',train=False, transform=transform, download=True)
    test_loader = DataLoader(train_set,batch_size=64,shuffle=True,num_workers=4)
    
    model = Net().to(device)
    criterion = nn.NLLLoss()
    optimizer = optim.SGD(model.parameters(),lr=0.01)    
    epoch_end = 20
    
    train_loss = train(epoch_end+1,device,train_loader,model,optimizer,criterion)
    test(device,test_loader,model,criterion)
    loss_plot(train_loss)
    visualize_stn()
       
