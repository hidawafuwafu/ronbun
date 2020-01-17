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

#音符の中央に円を描画
def draw_circle(Up, img):    
    template_width = 50
    template_height = 80
    for l in Up:
        cv2.circle(img, (l[0] + (template_width / 2), 
                    l[1] + (template_height / 2) ), 12, 
                                (255, 255, 0), thickness = -1)
        Dp.append([int(l[0] + (template_width / 2)), 
                     int(l[1] + (template_height / 2) )])

#画像の読み込み・加工
img = cv2.imread('image1025.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval, binarized = cv2.threshold(gray, 224, 255, cv2.THRESH_BINARY_INV)

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

draw_circle(Up, img)
cv2.imshow('score', img)
cv2.imwrite('maruhyouji.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()