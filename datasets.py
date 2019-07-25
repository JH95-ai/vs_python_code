import torch 
from torch.utils.data import DataLoader,Dataset
from utils import *

class IrisDataset(DataSet):
    def __init__(self,root_dir,train=True,mean=0,std=0):
        self.loder=load_data(root_dir)
        self.std=std
        self.mean=mean
        self.train=train
        self.root_dir=root_dir

    def __len__(self):
        return len(self.loder)
    
    def __getitem__(self,idx):
        path,target=self.loder(idx)
        img=cv2.imread(path,0)
        if img is None:
            print(path)
            assert img is not None

        #data augmentation
        if self.train:
            if random.random()<0.5:
                img=cv2.flip(img,1)
            if random.random()<0.1:
                img=motion_gauss_blur(img,degree=5,k=3)
                img=gaussian_noise(img,std=0.001)
                img=brightness(img,bright_factor=0.3)
        img=cv2.resize(img,(112,112))
        img=(img/255.0-self.mean)/self.std
        img=np.array(img)[np.newaxis,:,:]
        img=torch.Tensor(img)
        return img,target

def main():
    root_dir='some_path'
    datasets=IrisDataset(root_dir=root_dir,train=False)
    dataloader=DataLoader(datasets,batch_size=4,shuffle=True)
    for i,(imgs,targets) in enumerate(dataloader):
        for i in range(len(imgs)):
            img=imgs[i].data.numpy()
            target=targets[i].data.numpy()
            print(target)
            cv2.imshow('s',img)
            cv2.waitKey()

if __name__=="__main__":
    main()
