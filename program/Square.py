# coding:utf-8
import cv2
import math
import os
import gosen_bunkatu as gb
from decimal import Decimal, ROUND_HALF_UP
import onnkai
import cv2 as cv
import sys
import numpy as np
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
from PIL import Image
import matplotlib.pyplot as plt

Dp = []

#音符を四角で囲う
def draw_square(Up, img):
    template_width = 65
    template_height = 65
    for l in Up :
        cv2.rectangle(img, (l[0], l[1]), (l[0] + template_width, 
                            l[1] + template_height), (0, 0, 255), 3)
        Dp.append([int(l[0] + (template_width)),
                             int(l[1] + (template_height) )])

#画像の読み込み・加工
img = cv2.imread('image1025.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval, binarized = cv2.threshold(gray, 224, 255, 
                    cv2.THRESH_BINARY_INV)

#玉の検出座標データを読み込む
f = open("output2.dat","r")

#座標を入れるための配列を作る
Up = []

#データをすべて書き出してint型にする
for x in f:
    temp = x.replace('\n','')
    temp1 = temp.replace('\r','')
    temp2 = temp1.split(" ")
    Up.append( [ int(temp2[0]), int(temp2[1]) ] )

draw_square(Up, img)
cv2.imshow('score', img)
cv2.imwrite('sikakuhyouji.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()