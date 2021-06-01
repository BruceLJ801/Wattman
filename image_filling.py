#!/usr/bin/env python
#-*-coding:utf-8-*-
#@Author:lijia

# load packages
from PIL import Image
import matplotlib.pyplot as plt
import json
import numpy as np
#%matplotlib inline

# define function
def Picture_filling(file='./boxes.json', super_img='./accord.jpg', sub_img='./ackerman.jpg'):
    '''
    file：file path
    super_img：parent graph
    sub_img：subgraph
    '''
    
    # read file and load data
    f = open(file, 'r')
    content = f.read()
    data = json.loads(content)
    # load and copy image
    img1 = Image.open(super_img)
    img2 = Image.open(sub_img)
    img1_copy = img1.copy()
    img2_copy = img2.copy()
    img1_copy = img1_copy.convert("RGBA")
    img2_copy = img2_copy.convert("RGBA")
    
    # image resize
    box1 = data['boxes'][1]['rectangle']
    fill_box_size = (box1['left_top'],box1['right_bottom'])
    left_top = np.array(box1['left_top'])
    right_bottom = np.array(box1['right_bottom'])

    figure_size = right_bottom - left_top

    img2_resize = img2_copy.resize(figure_size, Image.ANTIALIAS)
    
    # image insertion
    img1_copy.paste(img2_resize, tuple(left_top))
    
    plt.imshow(img1_copy)
    plt.show()

# function call
Picture_filling(file='./boxes.json', super_img='./accord.jpg', sub_img='./ackerman.jpg')
