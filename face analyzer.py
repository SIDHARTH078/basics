import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from sklearn.datasets import fetch_ifw_people
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder 
from torch.utils.data import dataloader,TensorDataset
import numpy as np 

#load lfw face data

faces=fetch_ifw_people(min_faces_person=70,resize=0.4)
x=faces.images/255.0
y=faces.target
target_names=faces.target_names
n_classes=len(target_names)

#reshape x and encode y
x=x[:,np.newaxis,:,:]
x=torch.tensor(x,dtype=torch.float32)
y=torch.tensor(y,dtype=torch.long)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

train_ds=TensorDataset(x_train,y_train)
test_ds=TensorDataset(x_test,y_test)

train_loader=dataloader(train_ds,batch_size=32,shuffe=True)
test_loader=dataloader(test_ds,batch_size=32)

#build cnn model
class facenet(nn.module):
    def __init__(self,num_classes):
        super(facenet,self).__init__()
        self.conv1=nn.conv2d(1,32,kernel_size=3)
        self.pool=nn.maxpool2d(2,2)
        self.conv2=nn.conv2d(32,64,kernel_size=3)
        self.fc1=nn.Linear(100,num_classes)

        def forward(self,x):
            x=self.pool(F.relu(self.conv1(x)))
            x=self.pool(F.relu(self.conv2(x)))
            x=x.view(-1,64*11*9)
            x=F.relu(self.fc1(x))
            x=self.fc2(x)
            return x
        
device=torch.device("cuda"if torch.cuda.is_available() else "cpu")
model=facenet(n_classes).to(device)

criterion=nn.CrossEntropyLoss()
optimizer=optim.Adam(model.parameters(),lr=0.001)

for epoch in range(10):
    model.train()
    running_loss=0.0
    for inputs,labels in train_loader:
        inputs,labels=inputs.to(device),labels.to(device)

        optimizer.zer_grad()
        outputs=model(inputs)
        loss=criterion(outputs,labels)
        loss.backward()
        optimizer.step()

        running_loss+=loss.item()
    print(f"Epoch{epoch+1}-Loss:{running_loss/len(train_loader):.4f}")

    model.eval()
    correct=total=0
    with torch.no_grad():
        for inpus,labels in test_loader:
            inputs,labels=inputs.to(device),labels.to(device)
            outputs=model(inputs)
            predicted=torch.mx(outputs,1)
            total+=labels.size(0)
            correct+=(predicted==labels).sum().item()
    print(f"test accuracy:{100*correct/total:2f}%")    




