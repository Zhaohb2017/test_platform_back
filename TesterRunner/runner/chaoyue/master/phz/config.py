#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@ author: Hubery
@ create on: 2018/10/9 16:56
@ file: config.py
@ site: 
@ purpose: server configuration, player configuration, php interface
"""
#   益阳端口: 9089
#   主版本: 9007
SERVER_CONFIG = dict(site_id=2, channel_id=2024, gp_id=101, server_ip="192.168.1.153", server_port=9007)

#   宗安: 益阳、耒阳
# SERVER_CONFIG = dict(site_id=2, channel_id=2024, gp_id=101, server_ip="192.168.1.152", server_port=9089)

bread_base_url = "http://192.168.1.111:81/beard/api/mobile/api.php?api="



#   线上 - 打筒子线上
SERVER_CONFIG_ONLINE = dict(site_id=2, channel_id=2024, gp_id=101, server_ip="PHZLOW0.I2Syqjkc95.aliyungf.com", server_port=20400)


#   线上php接口
online_base_url = 'https://phz.jiaheyx.com/beard/api/mobile/api.php?api='