#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'weihaoxuan'

import random,string
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import os
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "."))
#生成随机字符串
def getRandomChar():
    #string模块包含各种字符串，以下为小写字母加数字
    ran = string.ascii_lowercase+string.digits
    char = ''
    for i in range(4):
        char += random.choice(ran)
    return char

#返回一个随机的RGB颜色
def getRandomColor():
    return (random.randint(50,300),random.randint(50,150),random.randint(50,150))

def create_code():

    #创建图片，模式，大小，背景色
    img = Image.new('RGB', (120,30), (255,255,255))
    #创建画布
    draw = ImageDraw.Draw(img)
    #设置字体
    font = ImageFont.truetype(os.path.join(project_dir,'var','Arial.ttf'), 25)

    code = getRandomChar()
    #将生成的字符画在画布上
    for t in range(4):
        draw.text((30*t+5,0),code[t],getRandomColor(),font)

    #生成干扰点
    for _ in range(random.randint(0,500)):
        #位置，颜色
        draw.point((random.randint(0, 120), random.randint(0, 30)),fill=getRandomColor())

    #生成干扰线
    line_num = random.randint(1,5)  # 干扰线条数
    for i in range(line_num):
        # 起始点
        begin = (random.randint(0, 120), random.randint(0, 30))
        # 结束点
        end = (random.randint(0, 120), random.randint(0, 30))
        draw.line([begin, end], fill=(0, 0, 0))

    #使用模糊滤镜使图片模糊
    # img = img.filter(ImageFilter.BLUR)
    #保存
    # img.save(''.join(code)+'.jpg','jpeg')
    return img,code

if __name__ == '__main__':
    create_code()