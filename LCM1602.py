#!/usr/bin/env python
#-*- coding:utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep

###############################################
# author: onionys
# email: onionys@ittraining.com.tw
# blog: http://blog.ittraining.com.tw/
# company: ittraining
# date: 2015/03/26
# description:
#     The python example code for controlling 
#     LCM module for the article on the blog:
#     http://blog.ittraining.com.tw/2014/12/raspberry-pi-b-python-lcd-16x2-hd44780.html
###############################################

RS = 20
RW = 21
EN = 26
D4 = 19
D5 = 13
D6 = 6
D7 = 5

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(EN,  GPIO.OUT)
    GPIO.setup(RS, GPIO.OUT)
    GPIO.setup(RW, GPIO.OUT)
    GPIO.setup(D4, GPIO.OUT)
    GPIO.setup(D5, GPIO.OUT)
    GPIO.setup(D6, GPIO.OUT)
    GPIO.setup(D7, GPIO.OUT)
    GPIO.output(D4,0)
    GPIO.output(D5,0)
    GPIO.output(D6,0)
    GPIO.output(D7,0)
    GPIO.output(RS,0)
    GPIO.output(RW,0)
    GPIO.output(EN,0)

    sleep(0.1)
    GPIO.output(EN,1)
    sleep(0.000001)
    GPIO.output(EN,0)
    sleep(0.002)

    GPIO.output(D5,1)

    GPIO.output(EN,1)
    sleep(0.000001)
    GPIO.output(EN,0)
    sleep(0.005)

    GPIO.output(EN,1)
    sleep(0.000001)
    GPIO.output(EN,0)
    sleep(0.0002)

    GPIO.output(EN,1)
    sleep(0.000001)
    GPIO.output(EN,0)
    sleep(0.0002)

    write_command(0x28)
    sleep(0.0001)
    write_command(0x0c)
    sleep(0.0001)
    write_command(0x01)
    sleep(0.002)


def write_command(cmd):
    GPIO.output(EN,0)
    GPIO.output(RW,0)
    GPIO.output(RS,0)
    GPIO.output(D7, 1 if (0x80 & cmd) else 0)
    GPIO.output(D6, 1 if (0x40 & cmd) else 0)
    GPIO.output(D5, 1 if (0x20 & cmd) else 0)
    GPIO.output(D4, 1 if (0x10 & cmd) else 0)

    GPIO.output(EN,1)
    sleep(0.000001)
    GPIO.output(EN,0)
    sleep(0.000001)

    GPIO.output(D7, 1 if (0x08 & cmd) else 0)
    GPIO.output(D6, 1 if (0x04 & cmd) else 0)
    GPIO.output(D5, 1 if (0x02 & cmd) else 0)
    GPIO.output(D4, 1 if (0x01 & cmd) else 0)

    GPIO.output(EN,1)
    sleep(0.000001)
    GPIO.output(EN,0)
    sleep(0.00005)


def write_data(data):
    GPIO.output(EN,0)
    GPIO.output(RW,0)
    GPIO.output(RS,1)
    GPIO.output(D7, 1 if (0x80 & data) else 0)
    GPIO.output(D6, 1 if (0x40 & data) else 0)
    GPIO.output(D5, 1 if (0x20 & data) else 0)
    GPIO.output(D4, 1 if (0x10 & data) else 0)

    GPIO.output(EN,1)
    sleep(0.000001)
    GPIO.output(EN,0)
    sleep(0.000001)

    GPIO.output(D7, 1 if (0x08 & data) else 0)
    GPIO.output(D6, 1 if (0x04 & data) else 0)
    GPIO.output(D5, 1 if (0x02 & data) else 0)
    GPIO.output(D4, 1 if (0x01 & data) else 0)

    GPIO.output(EN,1)
    sleep(0.000001)
    GPIO.output(EN,0)
    sleep(0.00005)

if __name__=="__main__":
    init()
    myWord = [
        0b00000100,
        0b00001010,
        0b00010001,
        0b00010001,
        0b00010001,
        0b00011111,
        0b00010001,
        0b00010001]

    command_set_CGRAM = 0x40

    CGRAM_addr = 0x08

    write_command(command_set_CGRAM + CGRAM_addr)

    write_data(myWord[0])  # <== 寫資料到CGRAM:0x00+0x08
    write_data(myWord[1])  # <== 寫資料到CGRAM:0x01+0x08
    write_data(myWord[2])  # <== 寫資料到CGRAM:0x02+0x08
    write_data(myWord[3])  # <== 寫資料到CGRAM:0x03+0x08
    write_data(myWord[4])  # <== 寫資料到CGRAM:0x04+0x08
    write_data(myWord[5])  # <== 寫資料到CGRAM:0x05+0x08
    write_data(myWord[6])  # <== 寫資料到CGRAM:0x06+0x08
    write_data(myWord[7])  # <== 寫資料到CGRAM:0x07+0x08

    # 第二個自訂字形寫入完畢
    # 把第二個自定字顯示到LCM螢幕的第一行第一個字

    write_command(0x80 + 0x00)  # 移動到LCM顯示螢幕的第一行第一個字的位置
    write_data(0x01)       # 顯示第二個字定字

    myWord = [
        0b00011011,
        0b00011011,
        0b00000000,
        0b00011011,
        0b00011011,
        0b00000000,
        0b00011011,
        0b00011011]


    command_set_CGRAM = 0x40

    CGRAM_addr = 0x10

    write_command(command_set_CGRAM + CGRAM_addr)


    write_data(myWord[0])  # <== 寫資料到CGRAM:0x00+0x08
    write_data(myWord[1])  # <== 寫資料到CGRAM:0x01+0x08
    write_data(myWord[2])  # <== 寫資料到CGRAM:0x02+0x08
    write_data(myWord[3])  # <== 寫資料到CGRAM:0x03+0x08
    write_data(myWord[4])  # <== 寫資料到CGRAM:0x04+0x08
    write_data(myWord[5])  # <== 寫資料到CGRAM:0x05+0x08
    write_data(myWord[6])  # <== 寫資料到CGRAM:0x06+0x08
    write_data(myWord[7])  # <== 寫資料到CGRAM:0x07+0x08

    # 第二個自訂字形寫入完畢
    # 把第二個自定字顯示到LCM螢幕的第一行第一個字

    write_command(0x80 + 0x01)  # 移動到LCM顯示螢幕的第一行第二個字的位置
    write_data(0x02)       # 顯示第三個自定字
