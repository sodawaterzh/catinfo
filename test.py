# -*- coding:utf-8 -*-
# from pymouse import PyMouse
# import time
# m = PyMouse()
# m.position()#获取当前坐标的位置
# time.sleep(3)
#
# for b in range(,1000):
# 	m.move(716,b)#鼠标移动到xy位置
# 	time.sleep(1)
# 	print(m.position())
# m.click(x,y)#移动并且在xy位置点击
# m.click(x,y,1|2)#移动并且在xy位置点击,左右键点击
# -*- coding=utf-8 -*-
import requests
import itchat
import random

KEY = '04f44290d4cf462aae8ac563ea7aac16'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    robots=['——By赵欢小助手','——By丸子','——By菠萝']
    reply = get_response(msg['Text'])+random.choice(robots)
    return reply or defaultReply


itchat.auto_login()
itchat.run()
