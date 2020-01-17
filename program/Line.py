# coding:utf-8
import cv2
import math
import numpy
import os

image = cv2.imread('image1025.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
retval, binarized = 
        cv2.threshold(gray, 224, 255, cv2.THRESH_BINARY_INV)

# 空の配列を作る
hist = []

# 3本ずつ見ていく
for y in range( 1, binarized.shape[0] - 1 ):
    h = 0
    pu = binarized[y-1]
    pc = binarized[y]
    pd = binarized[y+1]
    for x in range( 1, binarized.shape[1]-1 ):
        dx = max( abs( int(pc[x]) - int(pc[x-1])), 
                            abs( int(pc[x]) - int(pc[x+1])) )
        dy = max( abs( int(pc[x]) - int(pu[x]) ),
                             int(pc[x]) - int(pd[x]) )
        if( dy>32 and dy > dx*4 ):
            h=h+1
    # 黒の点の数をカウント
    hist = hist + [h]

y_line =[]

# 黒の点の数に合わせて線を塗る
for y in range( 1, binarized.shape[0]-3 ):
        #print( "y=" , y , ":" , hist[y] )
        if( hist[y] > 500 ):
                if (len(y_line) is 0):
                        y_line.append(y)
                        cv2.line(image, (0,y),(binarized.shape[1],y), 
                                            (0,32,224), 5)
                elif (y_line[len(y_line) - 1] + 10  < y):
                        y_line.append(y)
                        cv2.line(image, (0,y), (binarized.shape[1],y), 
                                            (0,32,224), 5)
                        
print ( y_line )       
cv2.imshow('image', image )
cv2.imwrite('line2.png', image)
cv2.waitKey(0)
cv2.destroyAllWindows()