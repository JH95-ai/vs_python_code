import cv2
import os
import random
import numpy as np
def load_data(file_dir):
    '''
    :rtype:object
    '''
    imgs_label_list=[]
    i=0
    for x in os.listdir(file_dir):
        for y in os.listdir(file_dir+x):
            str=y.split('.')[-1]
            if str=='bmp':
                t=os.path.join(file_dir,x,y)
                imgs_label_list.append((t,i))
        i+=1
    return imgs_label_list

def centercrop(img,size):
    output_size=(int(size),int(size))
    h,w=img.shape
    th,tw=output_size
    i=int(round((h-th)/2.))
    j=int(round((w-tw)/2.))
    return img[i:i+th,j:j+tw]

def brightness(image,bright_factor):
    bf=random.uniform(max(0.0,1-bright_factor),0.5+bright_factor)
    img=image.astype(np.float32)*bf
    img=imge.clip(min=0,max=255)
    img=img.astype(image.dtype)
    return img
#动态高斯模糊
def motion_gauss_blur(img,degree=5,angle=60,k=3,sigmax=0,sigmay=0):
    if random.random()<0.5:
        degree_val=degree
        angle_factor=random.randint(max(0,angle-45),min(180,angle+45))
        #得到旋转的2D矩阵.
        M=cv2.getRotationMatrix2D((degree_val/2,degree_val/2),angle_factor,1)
        motion_blur_kernel=np.diag(np.ones(degree_val))
        motion_blur_kernel=cv2.warpAffine(motion_blur_kernel,M,(degree_val,degree_val))
        motion_blur_kernel=motion_blur_kernel/degree_val
        #use custom-user to graph convolution ,this funciton will any linear filter apply to graph.
        #when aperture location graph outer ,this function accordance assign border pattern insertion
        #abnormal pixels value.
        blurred=cv2.filter2D(img,-1,motion_blur_kernel)
        #convert to uint8
        cv2.normalize(blurred,blurred,0,255,cv2.NORM_MINMAX)
        blurred=cv2.filter2D(img,-1,motion_blur_kernel)
        return blurred
    else:
        image=cv2.GaussianBlur(img,ksize=(k,k),sigmaX=sigmax,sigmaY=sigmay)
        return image

def gaussian_noise(image,mean=0,std=0.1):
    imgtype=image.dtype
    gauss=np.random.normal(mean,std,image.shape).astype(np.float32)
    noisy=np.clip((1+gauss)*image.astype(np.float32),0,255)
    return noisy.astype(imgtype)

