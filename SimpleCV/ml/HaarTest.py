from numpy import *
import Orange
import os
import glob
import pickle

from SimpleCV.Display import Display, pg
from SimpleCV.EdgeHistogramFeatureExtractor import *
from SimpleCV.HueHistogramFeatureExtractor import *
from SimpleCV.HaarLikeFeatureExtractor import *
from SimpleCV.BOFFeatureExtractor import *
from SVMClassifier import *
from NaiveBayesClassifier import *
from KNNClassifier import *
from TreeClassifier import *

img = Image("..//sampleimages//aerospace.jpg")
haar = HaarLikeFeatureExtractor(fname="haar.txt")
w = 800
h = 600
n=-1
print(haar.extract(img))
print(haar.getFieldNames())
display = Display(resolution = (w,h))

nut_path = "./data/take2/nuts/"
bolt_path = "./data/take2/bolts/"
train_path = [nut_path,bolt_path]
classes = ['nut','bolt']
print('Boosted Tree')
classifierBoostedTree = TreeClassifier([haar],flavor='Boosted')#
print('Train')
classifierBoostedTree.train(train_path,classes,disp=display,subset=25) #train
print('Test')
[pos,neg,confuse] = classifierBoostedTree.test(train_path,classes,disp=display,subset=n)

haar.saveWavelets('derp.txt')