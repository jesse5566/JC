# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:54:14 2019

@author: Jesse
"""

import twstock
import time
#import requests
import os

counterclean=0

while True:
    realdata=twstock.realtime.get('6535')
    if realdata['success']:
        realprice=float(realdata['realtime']['latest_trade_price']) #formate為str->float
        realvolume=realdata['realtime']['accumulate_trade_volume']
        tw6535=twstock.Stock('6535')
        
        #成交量
        tw6535v=tw6535.capacity #單位:股
        tw6535v=list(map(lambda i:i/1000,tw6535v)) #單位:張
        
        #五日平均成交量
        tw6535ma5=tw6535.moving_average(tw6535v,5) 
        
        #漲跌
        goup=realprice-tw6535.price[-1]
       
        
        if realprice>=20: #如果股價大於20的話 
            time.sleep(1) # 1秒印一次
            counterclean=counterclean+1
            #url_ifttt='https://maker.ifttt.com/trigger/stockLINE/with/key/bpizopEw9R9n-_QKeqfB3q?value1='+realprice
            #res1=requests.get(url_ifttt)
            if counterclean%7                                                                                                                                                                                                                                                            ==0:
                os.system("cls")
                print('<<<順藥6535>>>')
                print('七筆五日平均成交量:')
                print(tw6535ma5[-7:])
                print('近七日成交量:')
                print(tw6535v[-7:])
                print('========================')
                print('  目前成交量: '+realvolume)
                print('========================')
            else:
                print('now price:'+'%.2f'%realprice+'  '+'go_up:''%.2f'%goup)
            