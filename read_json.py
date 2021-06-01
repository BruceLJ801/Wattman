#!/usr/bin/env python
#-*-coding:utf-8-*-
#@Author:lijia

# load packages
import json

# load file
f = open('./boxes.json', 'r')
content = f.read()
data = json.loads(content)

# print the 'rectangle' content of 'box_b'
for i in range(len(data['boxes'])):
    if data['boxes'][i]['name'] == 'box_b':    #when name is box_b, print rectangle
        print('The rectangle of box_b:', data['boxes'][i]['rectangle'])
