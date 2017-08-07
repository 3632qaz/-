# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 11:19:31 2017

@author: chen
"""
from sys import exit
import os
import pygame
from pygame.locals import *
pygame.mixer.init()
#使用eventend需要调出窗口才可使用
#screen = pygame.display.set_mode((40, 80))


#获取目录所在列表
lists=[]
files=os.listdir()
for i in files:
    # os.path.splitext():分离文件名与扩展名
    if os.path.splitext(i)[1] == '.mp3':
        lists.append(i)

music_num = 1
music_name=lists[music_num-1]
music_volume = 10
music_play=1
print("volum=%d" % music_volume)
print("当前曲目：%s"% music_name)
music_location=0
#设置播放位置秒数
music_setlo=30
#设置播放第n首音乐
lists_setnum=3
#记录是否被认为设置下一首
lists_set=False
#记录已经播放了多长时间，用来抵消设定位置时额外的时长
music_exlo=0
#模式1为单曲播放，模式2为单曲循环，模式3为列表播放，模式4为列表循环
playmode=1
pygame.mixer.music.load(music_name)

def music_play():
    global music_name
    pygame.mixer.music.load(music_name)
    pygame.mixer.music.play()

def volume_up():
    global music_volume
    music_volume += 10
    if (music_volume > 100):
        music_volume = 100
    #设置音量
    pygame.mixer.music.set_volume(music_volume / 100.0)
    #显示音量
    print('当前音量：%d' % music_volume)

def volume_down():
    global music_volume
    music_volume -= 10
    if (music_volume > 0):
        music_volume = 0
        #设置音量
    pygame.mixer.music.set_volume(music_volume / 100.0)
        #显示音量
    print('当前音量：%d' % music_volume)

def music_pause():
    pygame.mixer.music.pause()

def music_unpause():
    pygame.mixer.music.unpause()

def music_setpos():
    global music_setlo
    global music_exlo
    pygame.mixer.music.rewind()
    pygame.mixer.music.set_pos(music_setlo)
    music_exlo=(pygame.mixer.music.get_pos()/1000)-music_setlo

def music_getpos():
    global music_location
    global music_exlo
    music_location=(pygame.mixer.music.get_pos()/1000)-music_exlo
    print(music_location)

def music_stop():
    global music_exlo
    pygame.mixer.music.stop()
    music_exlo=pygame.mixer.music.get_pos()/1000

def lists_print():
    print (lists)

def lists_sort():
    lists.sort()

def lists_autonext():
    global music_num
    global music_name
    if music_num<len(lists):
        music_num+=1
    else:
        music_num=0
    music_name=lists[music_num]

def lists_setnext():
    global music_name
    global lists_set
    music_num=lists_setnum
    music_name=lists[lists_setnum-1]
    lists_set=True
    print("下一首曲目：%s"% music_name)

def music_next():
    global lists_set
    if lists_set==False:
        lists_autonext()
    lists_set=False
    music_stop()
    music_play()


def set_mode():
    global playmode
    first_select = raw_input("请输入1-4来表示模式")
    #这里也许可以用正则表达式来限制
    if (first_select=="1" or first_select=="2"or first_select=="3" or first_select=="4") :
        play_mode = int(first_select)
        print (play_mode)
    else:
        print("请重试")

#所有播放完成的函数暂时无法用
def endevent1():
    music_stop()
def endevent2():
    music_stop()
    music_play()
def endevent3():
    if music_num==len(lists):
        music_stop()
        music_num=1
    else:
        music_next()
def endevent4():
    music_next()
def endevent():
    #python貌似没有switch…case用法
    if playmode == 2 :
        endevent2()
    elif playmode == 3:
        endevent3()
    elif playmode == 4:
        endevent4()
    else :
        endevent1()

#使用while循环时无法控制
# ENDPLAY=USEREVENT
# pygame.mixer.music.set_endevent(ENDPLAY)
# while True:
#     for event in pygame.event.get():
#         if event.type==ENDPLAY:
#             endevent()
