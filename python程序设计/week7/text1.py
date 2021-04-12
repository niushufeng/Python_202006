# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 21:47:03 2021

@author: NSF
"""

import json
# 一个列表，里面包含很多个字典
information = [{'小区名称':'小区A','均价':8000,'月交易量':20},
               {'小区名称':'小区B','均价':8500,'月交易量':35},
               {'小区名称':'小区C','均价':7800,'月交易量':50},
               {'小区名称':'小区D','均价':12000,'月交易量':18}]
with open('房屋信息.json','w') as fp: 
    json:dump(information,fp,indent =4,separators = [',',':'])
with open('房屋信息.json') as fp:
    information = json.load(fp)
    for info in information:
        print(info)
        
