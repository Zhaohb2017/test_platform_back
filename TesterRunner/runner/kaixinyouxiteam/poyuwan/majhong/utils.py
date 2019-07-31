#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@ author: Hubery
@ create on: 2018/10/16 14:49
@ file: utils.py
@ site: 
@ purpose: 
"""
GameTypes = {
    1: "余干麻将",
    2: "xx麻将",

}


def GetGameType(_type):
    return GameTypes[_type]


def GetOperateCH(_type):
    OperateName = None
    if _type == 1:
        OperateName = "吃"
    elif _type == 2:
        OperateName = "碰"
    elif _type == 3:
        OperateName = "跑"
    elif _type == 6:
        OperateName = "偎"
    elif _type == 7:
        OperateName = "该牌无人需要"
    elif _type == 8:
        OperateName = "提"
    elif _type == 9:
        OperateName = "胡"
    elif _type == 10:
        OperateName = "过"
    elif _type == 11:
        OperateName = "出"
    elif _type == 16:
        OperateName = "臭偎"
    elif _type == 18:
        OperateName = "歪"
    elif _type == 19:
        OperateName = "溜"
    else:
        print("暂未做此操作说明, 请说明该操作应用于哪个玩法, 进行添加!")
    return OperateName


def GetOperateID(_type):
    operate = None
    if _type == "吃":
        operate = 1
    elif _type == "碰":
        operate = 2
    elif _type == "跑":
        operate = 3
    elif _type == "偎":
        operate = 6
    elif _type == "提":
        operate = 8
    elif _type == "胡":
        operate = 9
    elif _type == "过":
        operate = 10
    elif _type == "出":
        operate = 11
    elif _type == "歪":
        operate = 18
    elif _type == "溜":
        operate = 19
    else:
        print("暂未做此操作ID接口, 请说明该操作应用于哪个玩法, 进行添加!")
    return operate


#   余干麻将创建房间设置
def YuganMajiang(_data):
    create_room_data = {}
    for name, value in _data.items():
        if name == "玩法1":
            if value == "翻宝":
                create_room_data["type"] = 64
            elif value == "夹子":
                create_room_data["type"] = 65
            elif value == "索胡":
                create_room_data["type"] = 66
            else:
                print("未知玩法1" + name)
                return None
        elif name == "局数":
            create_room_data["ju"] = value
        elif name == "人数":
            create_room_data["players"] = value
        elif name == "玩法2":
            if value == "带宝胡":
                create_room_data["operation"] = 1
            elif value == "见宝飞":
                create_room_data["operation"] = 2
            elif value == "宝飞尽":
                create_room_data["operation"] = 4
            else:
                print("未知玩法2" + name)
                return None
        # elif name == "封顶":
        #     if value == "两宝封顶":
        #         create_room_data["type"] = 1
        #     elif value == "三宝封顶":
        #         create_room_data["type"] = 2
        #     else value == "不宝封顶":
        #         create_room_data["type"] = 4
        # 荒庄
        # 首局坐庄
        # 宝分
        # 玩法3
        elif name == "防作弊":
            create_room_data["fang_zuobi"] = value
    create_room_data["gameRoomType"] = "60"
    return create_room_data


def RoomDataReplace(_type, _data):
    if _type == "余干麻将":
        return YuganMajiang(_data)
    else:
        print("没有此玩法--> %s, 查看当前玩法名字是否正确." % _type)
    return None
