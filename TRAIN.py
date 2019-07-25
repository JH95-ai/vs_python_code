import argparse
import os 
import shutil
import time 
import torch.optim
import torch.nn as nn
import torch.nn.parallel
from datasets import IrisDataset
from ShuffleNetV2 import shufflenetv2
from torch.utils.data import DataLoader

os.environ["CUDA_VISIBLE_DEVICES"]="-1"
parser=argparse.ArgumentParser(description="Pytorch Iris Training")
parser.add_argument('data',metavar='DIR',
                    help='path to dataset')
parser.add_argument('--epochs',default=90,type=int,metavar='N',
                    help="number of total epochs to run")
parser.add_argument('--start--epoch',default=0,type=int,metavar='N',
                    help="manual epoch number (useful on restarts)")
parser.add_argument('-b','-batch-size',default=256,type=int,
                    metavar='N',help='mini-batch size (default:256)')
parser.add_argument('--lr','--learning-rate',default=1e-4,type=float,
                    metavar='W',help='weight decay (default:1e-4)')
parser.add_argument('--decay','--wd',default=1e-4,type=float,
                    metavar='W',help='weight decay (default:1e-4)')
parser.add_argument('--resume',default='',type=str,metavar='PATH',
                    help='path to latest check point (default:none)')
parser.add_argument('--evaluate',default='',type=str,metavar='PATH',
                    help='path to evalute model(default:none)')
parser.add_argument('--pretrained',default='',type=str,metavar='PATH',
                    help='path to pre-trained model (default:none)')
parser.add_argument('--world-size',default=1,type=int,
                    help='number of distributed processes')

best_prec1=0

def main():
    global args,best_prec1
    args=parser.parse_args()
    if args.pretrained:
        print('=>using pre-trained model"{}" '.format('shufflenet'))
        model=shufflenetv2(width_size)
