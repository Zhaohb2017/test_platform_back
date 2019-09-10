#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@ author: Hubery
@ create on: 2019/8/19 17:59
@ file: set_cardtype_utils.py
@ site:
@ purpose:
"""

cards = {
    "1":["2W","2W","3T","4T","5T","5S","6S","7S","6W","6W","6W","8W","8W","8W"],
    "2":["1W","1W","1S","4W","5W","6W","5T","5T","7W","7W","7W","9W","9W"],
    "3":["2S","2S","2T","2T","9S","9S","9S","4W","4W","4W","3S","2W","3W"],
    "4":["2S","6S","1W","6W","2T","3W","3T","9W","5T","4S","7S","6W","6T"],
    "5":["8W","5W","7W","8W","3W","3S","9S","9S","9S","3S","8S","8S","8S","8S","8S","8S","8S","8S","8S","8S","8S","8S","8S","8S","8S"]}

import time
import json
import struct
import socket


#   打包数据
def pack_data(account_data):
    head_data = b"QS"
    body_data = b""
    package_len = 0

    format = "<i"

    proto_data = struct.pack('<h', account_data['protocol'])
    package_len += struct.calcsize('<h')
    # body_data += struct.pack('<h', account_data['protocol'])



    body_data += struct.pack(format, account_data['sever_type'])
    package_len += struct.calcsize(format)



    body_data += struct.pack(format, account_data['sever_id'])
    package_len += struct.calcsize(format)



    body_data += struct.pack('<H', account_data['subcmd'])
    package_len += struct.calcsize(format)


    format = '<%ds' % (len(account_data['card_type']) + 1)
    body_data += struct.pack("<i", len(account_data['card_type']) + 1)
    body_data += struct.pack(format, account_data['card_type'].encode())
    package_len += struct.calcsize(format)



    format = "<i"
    body_data += struct.pack("<i", account_data['room_id'])
    package_len += struct.calcsize(format)


    pack_len = struct.pack("<h", package_len)
    finnal_data = head_data + pack_len + proto_data + body_data

    return finnal_data



class TestLoginPerfor(object):
    #	初始化socket对象, 连接服务器
    def __init__(self, ip, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = port
        self.login_suc = True

        self.socket.connect((self.ip, self.port))
        time.sleep(2)

    #   发送数据
    def send_data(self, _data):
        start = time.time()

        self.socket.send(_data)


    #   关闭连接
    def connect_close(self):
        self.socket.close()

def put_in_the_room(ip,port,cards,roomID,sever_id=1400):
    try:
        config_card_data = {'protocol': 10002, 'sever_type': 2, 'sever_id':0, 'subcmd': 65534,
                            'card_type': json.dumps(cards), 'room_id': int(roomID)}
        card_data = pack_data(config_card_data)
        test = TestLoginPerfor(ip, int(port))
        test.send_data(card_data)
        time.sleep(2)
        test.connect_close()
        return True
    except Exception as err:
        return  err





