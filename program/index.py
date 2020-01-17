# coding:utf-8
import cv2
import math
import os
#gosen_bunkatu.pyを呼び出している
import gosen_bunkatu as gb
#四捨五入するためのライブラリ
from decimal import Decimal, ROUND_HALF_UP
#onnkai.pyを呼び出している
import onnkai
import cv2 as cv
import sys
#以下日本語を表示するために必要なライブラリ
import numpy as np
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
from PIL import Image
import matplotlib.pyplot as plt

#楕円の中央の座標を入れるための配列を作る
Dp = []

#音符の中央に円を描画
def draw_circle(Up, img):    
    template_width = 50
    template_height = 80
    for l in Up:
        Dp.append([int(l[0] + (template_width / 2)), 
                            int(l[1] + (template_height / 2) )])

#画像の読み込み・加工
img = cv2.imread('image1025.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval, binarized = cv2.threshold(gray, 224, 255, 
                                    cv2.THRESH_BINARY_INV)

#玉の検出座標データを読み込む
f = open("output2.dat","r")

#楕円の座標を入れるための配列を作る
Up = []

#音符の座標のデータをすべて書き出してint型にする
for x in f:
    temp = x.replace('\n','')
    temp1 = temp.replace('\r','')
    temp2 = temp1.split(" ")
    Up.append( [ int(temp2[0]), int(temp2[1]) ] )


#空の配列を作る
hist = []

#3本ずつ見ていく
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
    #黒点の数をカウント
    hist = hist + [h]

y_line =[]

#黒点の数に合わせて線を塗る
for y in range( 1, binarized.shape[0]-3 ):
        if( hist[y] > 500 ):
                if (len(y_line) is 0):
                        y_line.append(y)
                elif (y_line[len(y_line) - 1] + 10  < y):
                        y_line.append(y)


def scaleFunction(gosen, onnpu):
    # ある音階から次の音階までの距離の計算
    DIFF = (gosen[1] - gosen[0]) / 2 - 0.1

    #gosen_bunkatu.pyの関数を呼び出して5線を5本ずつに分割する
    gosen_d = gb.splitStaff(gosen)

    #五線の中央の線(上から3番めの線)を配列に格納する
    gosen_dd = []
    for g in gosen_d:
        gosen_dd.append(g[2])

    #onnkai.pyの関数を呼び出して五線譜に対する五線上の音符を分ける
    onnkai_d = onnkai.makeScore(gosen_dd, onnpu)

    #割り振った音階を格納する配列
    assignment = []
 
    ret_data = []
    for i, od in enumerate(onnkai_d):
        #五線のy座標の配列を代入する
        gosen_y = od["gosen"]
        #へ音記号とト音記号の切り替えを行う
        cases = None
        if i % 2 is 0:
            __format = ["シ", "ド", "レ", "ミ", "ファ", "ソ", "ラ"] #表示する音階のデータ
        else:
            __format = ["レ", "ミ", "ファ", "ソ", "ラ", "シ", "ド"] #表示する音階のデータ

        for note in od["note"]:
            #音符のｙ軸取得
            note_y = note[1]
            #音符を取るときの誤差の調整
            normalize = -1
            #ｙ軸から見て音符が何段階ずれているか
            n = (gosen_y - note_y - normalize) / DIFF
            #以下２行で上の値を四捨五入
            dec = Decimal(str(n))
            n = int(dec.quantize(Decimal('0'), rounding=ROUND_HALF_UP)) 
            #以下でassignmentにpythonオブジェクトを格納する
            data = {"score_line": gosen_y,"n": note} 
            #四捨五入した値が自然数なら__format[scale]番目をdata["scale"]に代入
            if n >= 0:
                scale = n % len(__format)
            #自然数でなければ__formatの(7 - ((絶対値n mod 7)+ 1) mod 7番目の値をdata["scale"]に代入
            else:
                scale = (abs(n) % len(__format)) + 1
                scale = (len(__format) - scale + 1) % len(__format)

            data["scale"] = __format[scale]
            #dataの値をそれぞれの変数に格納する
            assignment.append(data)
            ret_data.append(data)       
    return ret_data

#OpenCVが日本語対応していないため，Pillowというライブラリを利用する
def draw_text_by_jp(CV2PIL_normalize, coordinate, scale):
    #色置換をした画像を変数drawに代入する
    draw = PIL.ImageDraw.Draw(CV2PIL_normalize)
    #フォント指定
    font_ttf = '/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc'
    #フォントサイズ指定，変数fontに代入する
    font = PIL.ImageFont.truetype(font_ttf, 40)
    #テキスト表示
    draw.text((coordinate[0], coordinate[1]), scale.decode('utf_8'),
                         font=font, fill=(0, 0, 0))
    return CV2PIL_normalize


if __name__=='__main__':
        #五線のy座標をgosenに代入している
        gosen = (y_line)
        #音符の楕円の関数を呼び出している
        draw_circle(Up, img)
        #音符の座標をonnpuに代入している
        onnpu = (Dp)
        #scaleFunctiomという関数を呼び出している
        ret = scaleFunction(gosen, onnpu)
        #OpenCVの色の置換を行っている
        CV_im_RGB = img[:, :, ::-1].copy()
        CV2PIL_normalize=Image.fromarray(CV_im_RGB)
        #英語を日本語に置換している
        covert = {"A": "ラ","B": "シ","C": "ド","D": 
                "レ","E": "ミ","F": "ファ","G": "ソ"}

        #配列がある限り繰り返す
        for i, r in enumerate(ret):
                output = []
                for key, value in r.items():
                        output.append(value)

        #音階データがある限り音階表示をする
        for r in ret:
            x = r["n"][0]
            y = r["score_line"]
            scale = r["scale"]
            #楽譜の指定の位置に音階を表示している
            coordinate = (x - 20, y + 140)
            draw_text_by_jp(CV2PIL_normalize, coordinate, scale)

#画像を表示する
plt.imshow(CV2PIL_normalize)
plt.show()
#画像を保存している
CV2PIL_normalize.save('gazou5.png')
