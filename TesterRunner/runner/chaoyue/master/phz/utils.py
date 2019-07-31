#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@ author: Hubery
@ create on: 2018/10/16 14:49
@ file: utils.py
@ site: 
@ purpose: 
"""
default = ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                   '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                   '0', '0', '0', '0', '0', '0', '0', '0', '0']

def conversion_of_number_systems(index,value=default):
    #玩法进制转换
    value[index] = "1"
    return value

def systemTow_transform(arg):
    #2进制转换整数
    str_arg = "".join(arg)
    return int(str_arg,2)

GameTypes = {
    1: "邵阳字牌",
    2: "邵阳剥皮",
    3: "娄底放罚炮",
    4: "常德跑胡子",
    5: "衡阳六抢胡",
    6: "长沙跑胡子",
    7: "湘乡告胡子",
    8: "永州扯胡子",
    9: "怀化红拐弯",
    10: "郴州字牌",
    11: "攸县碰胡子",
    12: "耒阳字牌",
    13: "邵阳放炮罚",
    14: "永丰跑胡子",
    18: "衡阳十胡卡",
    19: "四六八红拐弯",
    20: "益阳歪胡子",
    21: "祁东十五胡",
    22: "衡阳百胡",
    23: "岳阳歪胡子"
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


#   邵阳字牌创建房间设置
def ShaoYangZiPai(_data):
    create_room_data = {}
    for name, value in _data.items():
        if name == "人数":
            create_room_data["gamePlayer"] = value

        elif name == "胡一等":
            if value == "5息1囤":
                create_room_data["gameHuYiDeng"] = 0
            elif value == "3息1囤":
                create_room_data["gameHuYiDeng"] = 1

        elif name == "局数":
            create_room_data["gameCiShu"] = value

        elif name == "牌数":
            if value == "不抽底牌":
                create_room_data["gamePaiShu"] = 0

            elif value == "抽牌20张":
                create_room_data["gamePaiShu"] = 1
        elif name == "玩法选项":
            for k,v in value.items():  #玩法选项是一个字典类型
                if k == "o_jiachui":   #加锤选项
                    if v == True:
                        jiachui = -10
                        wanfa = conversion_of_number_systems(jiachui)
                        jc_data = systemTow_transform(wanfa) #加锤参数
                        create_room_data["gameWanFa"] = jc_data





    create_room_data["gameRoomType"] = "1"

    return create_room_data

#   邵阳剥皮创建房间设置
def ShaoYaoBoPi(_data):
    create_room_data = {}
    integral_double = 0 # 积分加倍
    option = None
    print("玩法选项: %s"%_data)
    for name, value in _data.items():
        if name == "人数":
            create_room_data["gamePlayer"] = value
        elif name == "玩法选项":
            for k,v in value.items():
                if k == 'o_RedAndBlack': #红黑点
                    if v is True:
                        red_black_index = -2
                        option = conversion_of_number_systems(red_black_index)
                elif k == 'o_lianzhuang':
                    if v is True:
                        create_room_data['gameBPLianZhuang'] = 0
                elif k == "o_0fen": #0分上告
                    if v is True:
                        shanggao_index =  -8
                        option = conversion_of_number_systems(shanggao_index)
                elif k == 'o_jiachui':  # 加锤
                    if v is True:
                        jiachui_index = -10
                        option = conversion_of_number_systems(jiachui_index)
                elif k == 'o_NoShow_dipai':  #不显示底牌
                    if v is True:
                        dipai_index = -28
                        option = conversion_of_number_systems(dipai_index)

            if option is not None:
                gameWanfa = systemTow_transform(option)
                create_room_data['gameWanFa'] = gameWanfa


        elif name == "封顶":
            if value == "不封顶":
                create_room_data['gameFengDing'] = 0
            elif value == "150息":
                create_room_data['gameFengDing'] = 150
            elif value == "200息":
                create_room_data['gameFengDing'] = 200
            elif value == "300息":
                create_room_data['gameFengDing'] = 300

        elif name == "牌数":
            if value == "不抽底牌":
                create_room_data["gamePaiShu"] = 0

            elif value == "抽牌10张":
                create_room_data["gamePaiShu"] = 2

            elif value == "抽牌20张":
                create_room_data["gamePaiShu"] = 1

        elif name == "积分加倍":
            if value == "不加倍":
                double = 0
            elif value == "低于25分加倍":
                integral_double = 524288
            elif value == "低于50分加倍":
                integral_double = 65536
            elif value == "低于75分加倍":
                integral_double = 1048576
            elif value == "低于100分加倍":
                integral_double = 131072
            elif value == "不限分加倍":
                integral_double = 0

        elif name == "翻倍":
            if value == "翻2倍":
                double = 1
            elif value == "翻3倍":
                double = 2
            elif value == "翻4倍":
                double = 4

    create_room_data['gameVip'] = integral_double + double
    create_room_data["gameRoomType"] = "2"

    return create_room_data

#   娄底放炮罚
def LouDiFangPaoFa(_data):
    create_room_data = {}
    Tips = 0  # 总结算翻倍提示
    double = 0  # 翻倍
    integral_double = 0  # 积分加倍
    for name, value in _data.items():
        if name == "人数":
            create_room_data["gamePlayer"] = value
        elif name == "名堂":
            for wanfa in value:
                if wanfa == "飘胡":
                    create_room_data['gameMaoHu'] = 1

                elif wanfa == "总结算翻倍提示":
                    Tips = 134217728

            if "总结算翻倍提示" not in value:
                Tips = 0

            create_room_data['gameWanFa'] = Tips


        elif name == "封顶":
            if value == "200息":
                create_room_data['gameFengDing'] = 0
            elif value == "400息":
                create_room_data['gameFengDing'] = 1

        elif name == "牌数":
            if value == "不抽底牌":
                create_room_data["gamePaiShu"] = 0

            elif value == "抽牌20张":
                create_room_data["gamePaiShu"] = 1

        elif name == "积分加倍":
            if value == "不加倍":
                integral_double = 0
            elif value == "大于50分不加倍":
                integral_double = 524288
            elif value == "大于100分不加倍":
                integral_double = 65536
            elif value == "大于150分不加倍":
                integral_double = 1048576
            elif value == "大于200分不加倍":
                integral_double = 131072
            elif value == "不限分加倍":
                integral_double = 131072

        elif name == "翻倍":
            if value == "翻2倍":
                double = 1
            elif value == "翻3倍":
                double = 2
            elif value == "翻4倍":
                double = 4

    create_room_data['gameVip'] = integral_double + double
    create_room_data["gameRoomType"] = "3"

    print(create_room_data)

    return create_room_data

#   衡阳六胡抢
def HengYangLiuHuQiang(_data):
    create_room_data = {}
    CardNum = 0
    ZhangNum = 0
    double = 0
    integral_double = 0
    HaiDiHu = 0
    HongHeiDian = 0
    for name, value in _data.items():
        if name == "人数":
            create_room_data["gamePlayer"] = value

        elif name == "名堂":
            for i in value:
                if i == "明偎":
                    create_room_data['gameZiMoFanBei'] = 0

                elif i == "红黑点":
                    HongHeiDian = 2
                elif i == "可胡示众牌":
                    create_room_data['gameShiZhongPai'] = 1
                elif i == "飘胡":
                    create_room_data['gameMaoHu'] = 1
                elif i == "天地海底胡":
                    HaiDiHu = 512
            create_room_data['gameWanFa'] = HongHeiDian + HaiDiHu

        elif name == "一五十":
            if value == "一五十":
                create_room_data['gameYiWuShi'] = 1

        elif name == "底分":
            if value == "底分2分":
                create_room_data['gameDiFen'] = 1

        elif name == "局数":
            create_room_data["gameCiShu"] = value

        elif name == "牌数":
            if value == "不抽底牌":
                CardNum = 0

            elif value == "抽牌20张":
                CardNum = 1

        elif name == "张数":
            if value == "21张":
                ZhangNum = 16

            elif value == "抽牌20张":
                ZhangNum = 32

        elif name == "翻醒":
            if value == "不带醒":
                create_room_data["gameFanXing"] = 2

            elif value == "翻醒":
                create_room_data["gameFanXing"] = 0

            elif value == "随醒":
                create_room_data["gameFanXing"] = 1

        elif name == "胡一等":
            if value == "1息1囤":
                create_room_data["gameHuYiDeng"] = 1
            elif value == "3息1囤":
                create_room_data["gameHuYiDeng"] = 0

        elif name == "起胡":
            if value == "6息起胡":
                create_room_data["gameQiHu"] = 0

            elif value == "9息起胡":
                create_room_data["gameQiHu"] = 1

            elif value == "15息起胡":
                create_room_data["gameQiHu"] = 2

        elif name == "必胡":
            if value == "点炮必胡":
                create_room_data["gameDianPaoBiHu"] = 0

            elif value == "有胡必胡":
                create_room_data["gameDianPaoBiHu"] = 1

        elif name == "积分加倍":
            if value == "不加倍":
                double = 0
            elif value == "低于10分加倍":
                integral_double = 65536
            elif value == "低于20分加倍":
                integral_double = 131072
            elif value == "低于30分加倍":
                integral_double = 262144
            elif value == "不限分加倍":
                integral_double = 0

        elif name == "翻倍":
            if value == "翻2倍":
                double = 1
            elif value == "翻3倍":
                double = 2
            elif value == "翻4倍":
                double = 4


    create_room_data['gameVip'] = integral_double + double
    create_room_data["gamePaiShu"] = CardNum + ZhangNum
    create_room_data["gameRoomType"] = "5"
    return create_room_data

#   衡阳十胡卡
def HengYangShiHuKa(_data):
    create_room_data = {}
    HongHeiDian = 0
    HaiDiHu = 0
    double = 0
    integral_double = 0
    for name, value in _data.items():
        if name == "人数":
            create_room_data["gamePlayer"] = value

        elif name == "名堂":
            for i in value:
                if i == "自摸翻倍":
                    create_room_data['gameZiMoFanBei'] = 0
                elif i == "红黑点":
                    HongHeiDian = 2
                elif i == "可胡示众牌":
                    create_room_data['gameShiZhongPai'] = 1
                elif i == "飘胡":
                    create_room_data['gameMaoHu'] = 1
                elif i == "天地海底胡":
                    HaiDiHu = 512

            create_room_data['gameWanFa'] = HongHeiDian + HaiDiHu

        elif name == "底分":
            if value == "底分2分":
                create_room_data['gameDiFen'] = 1

        elif name == "一五十":
            if value == "一五十":
                create_room_data['gameYiWuShi'] = 1

        elif name == "局数":
            create_room_data["gameCiShu"] = value

        elif name == "翻醒":
            if value == "不带醒":
                create_room_data["gameFanXing"] = 2

            elif value == "翻醒":
                create_room_data["gameFanXing"] = 0

            elif value == "随醒":
                create_room_data["gameFanXing"] = 1

        elif name == "胡一等":
            if value == "1息1囤":
                create_room_data["gameHuYiDeng"] = 1
            elif value == "3息1囤":
                create_room_data["gameHuYiDeng"] = 0

        elif name == "必胡":
            if value == "点炮必胡":
                create_room_data["gameDianPaoBiHu"] = 0

            elif value == "有胡必胡":
                create_room_data["gameDianPaoBiHu"] = 1

            elif value == "无":
                create_room_data['gameDianPaoBiHu'] = 2

        elif name == "积分加倍":
            if value == "不加倍":
                double = 0
            elif value == "低于10分加倍":
                integral_double = 65536
            elif value == "低于15分加倍":
                integral_double = 524288
            elif value == "低于20分加倍":
                integral_double = 131072
            elif value == "低于30分加倍":
                integral_double = 262144
            elif value == "不限分加倍":
                integral_double = 0

        elif name == "翻倍":
            if value == "翻2倍":
                double = 1
            elif value == "翻3倍":
                double = 2
            elif value == "翻4倍":
                double = 4

    create_room_data['gameVip'] = integral_double + double
    create_room_data["gameRoomType"] = "18"
    return create_room_data

#   怀化红拐弯
def HuaiHuaHongGuaiWan(_data):
    create_room_data = {}
    double = 0
    integral_double = 0
    for name, value in _data.items():
        if name == "人数":
            create_room_data["gamePlayer"] = value

        elif name == "局数":
            create_room_data["gameCiShu"] = value

        elif name == "名堂":
            for wanfa in value:
                if wanfa == "总结算翻倍提示":
                    create_room_data['gameWanFa'] = 134217728

        elif name == "底分":
            if value == "底分1分":
                create_room_data['gameDiFen'] = 0
            elif value == "底分2分":
                create_room_data['gameDiFen'] = 1
            elif value == "底分3分":
                create_room_data['gameDiFen'] = 2
            elif value == "底分4分":
                create_room_data['gameDiFen'] = 3
            elif value == "底分5分":
                create_room_data['gameDiFen'] = 4

        elif name == "名堂":
            for wanfa in value:
                if wanfa == "抢胡":
                    create_room_data['gameWanFa'] = 33554432

        elif name == "起胡":
            create_room_data['gameQiHu'] = 1

        elif name == "牌数":
            if value == "不抽底牌":
                create_room_data["gamePaiShu"] = 0

            elif value == "抽牌20张":
                create_room_data["gamePaiShu"]  = 1

        elif name == "积分加倍":
            if value == "不加倍":
                double = 0
            elif value == "低于25分加倍":
                integral_double = 524288
            elif value == "低于50分加倍":
                integral_double = 65536
            elif value == "低于75分加倍":
                integral_double = 1048576
            elif value == "低于100分加倍":
                integral_double = 131072
            elif value == "不限分加倍":
                integral_double = 0

        elif name == "翻倍":
            if value == "翻2倍":
                double = 1
            elif value == "翻3倍":
                double = 2
            elif value == "翻4倍":
                double = 4

    create_room_data['gameVip'] = integral_double + double
    create_room_data["gameRoomType"] = "9"
    return create_room_data

#   益阳歪胡子
def YiYangWaiHuZi(_data):
    create_room_data = {}
    QuanMingTang = 0
    BigSmall = 0
    TianHu = 0
    for name, value in _data.items():
        if name == "人数":
            create_room_data["gamePlayer"] = value
        elif name == "局数":
            create_room_data["gameCiShu"] = value
        elif name == "牌数":
            if value == "不抽底牌":
                create_room_data["gamePaiShu"] = 0

            elif value == "抽牌20张":
                create_room_data["gamePaiShu"] = 1

        elif name == "封顶":
            if value == "100胡":
                create_room_data['gameFengDing'] = 100
            elif value == "200胡":
                create_room_data['gameFengDing'] = 200
            elif value == "300胡":
                create_room_data['gameFengDing'] = 300

        elif name == "名堂":
            for wanfa in value:
                if wanfa == "全名堂":
                    QuanMingTang = 1
                elif wanfa == "大小字胡":
                    BigSmall = 2
                elif wanfa == "天胡报听":
                    TianHu = 4

            create_room_data['gameWanFa'] = QuanMingTang + BigSmall + TianHu

        elif name == "起胡":
            if value == "6胡起胡":
                create_room_data["gameQiHu"] = 6

            elif value == "7胡起胡":
                create_room_data["gameQiHu"] = 7


    create_room_data["gameRoomType"] = "20"

    print("益阳: %s" % create_room_data)

    return create_room_data

#   衡阳百胡
def HengYangBaiHu(_data):
    create_room_data = {}
    for name, value in _data.items():
        if name == "封顶":
            if value == "200息":
                create_room_data['gameFengDing'] = 0
            elif value == "400息":
                create_room_data['gameFengDing'] = 1

    create_room_data["gameRoomType"] = "22"
    return create_room_data

#   四六八红拐弯
def SiLiuBaHongGuaiWan(_data):
    create_room_data = {}
    for name, value in _data.items():
        if name == "局数":
            create_room_data['gameCiShu'] = value

    create_room_data["gameRoomType"] = "19"
    return create_room_data

#   永丰跑胡子
def YongFengPaoHuZi(_data):
    create_room_data = {}
    create_room_data["gameRoomType"] = "14"
    return create_room_data

#   邵阳放炮罚
def ShaoYangFangPaoFa(_data):
    create_room_data = {}
    hongheidian = 0
    zimo = 0
    for name, value in _data.items():
        if name == "人数":
            create_room_data['gamePlayer'] = value

        elif name == "名堂":
            if value == "红黑点":
                hongheidian = 2

        elif name == "自摸":
            if value == "自摸翻倍":
                create_room_data['gameZiMoFanBei'] = 0
            elif value == "自摸加10胡":
                zimo = 262144

    create_room_data['gameWanFa'] = hongheidian + zimo
    create_room_data["gameRoomType"] = "13"
    return create_room_data

#   攸县碰胡子
def YouXianPengHuZi(_data):
    create_room_data = {}
    for name, value in _data.items():
        if name == "连中":
            if value == "连中":
                create_room_data['gameLianZhuang'] = 0
            elif value == "中庄":
                create_room_data['gameLianZhuang'] = 1
        elif name == "局数":
            create_room_data['gameCiShu'] = value

        elif name == "人数":
            create_room_data['gamePlayer'] = value

        elif name == "必胡":
            if value == "无":
                create_room_data['gameDianPaoBiHu'] = 2
            elif value == "点炮必胡":
                create_room_data['gameDianPaoBiHu'] = 0
            elif value == "有胡必胡":
                create_room_data['gameDianPaoBiHu'] = 1

    create_room_data["gameRoomType"] = "11"
    return create_room_data

#   郴州字牌
def ChenZhouZiPai(_data):
    create_room_data = {}
    double = 0
    integral_double = 0
    for name, value in _data.items():
        if name == "人数":
            create_room_data['gamePlayer'] = value

        elif name == "起胡":
            if value == "3息起胡":
                create_room_data['gameQiHu'] = 0
            elif value == "6息起胡":
                create_room_data['gameQiHu'] = 1
            elif value == "9息起胡":
                create_room_data['gameQiHu'] = 0

        elif name == "胡一等":
            if value == "1息1囤":
                create_room_data["gameHuYiDeng"] = 1
            elif value == "3息1囤":
                create_room_data["gameHuYiDeng"] = 0

        elif name == "局数":
            create_room_data['gameCiShu'] = value

        elif name == "名堂":
            for wanfa in value:
                if wanfa == "自摸翻倍":
                    create_room_data['gameZiMoFanBei'] = 0
                elif wanfa == "红黑点":
                    create_room_data['gameWanFa'] = 2
                elif wanfa == "毛胡":
                    create_room_data['gameMaoHu'] = 1

        elif name == "必胡":
            if value == "无":
                create_room_data['gameDianPaoBiHu'] = 2
            elif value == "点炮必胡":
                create_room_data['gameDianPaoBiHu'] = 0
            elif value == "有胡必胡":
                create_room_data['gameDianPaoBiHu'] = 1

        elif name == "底分":
            if value == "底分1分":
                create_room_data['gameDiFen'] = 0
            elif value == "底分2分":
                create_room_data['gameDiFen'] = 1
            elif value == "底分3分":
                create_room_data['gameDiFen'] = 2
            elif value == "底分4分":
                create_room_data['gameDiFen'] = 3
            elif value == "底分5分":
                create_room_data['gameDiFen'] = 4

        elif name == "积分加倍":
            if value == "不加倍":
                double = 0
            elif value == "低于10分加倍":
                integral_double = 65536
            elif value == "低于15分加倍":
                integral_double = 131072
            elif value == "低于20分加倍":
                integral_double = 262144
            elif value == "不限分加倍":
                integral_double = 0

        elif name == "翻倍":
            if value == "翻2倍":
                double = 1
            elif value == "翻3倍":
                double = 2
            elif value == "翻4倍":
                double = 4
    create_room_data['gameVip'] = double + integral_double
    create_room_data["gameRoomType"] = "10"
    return create_room_data

#   祁东十五胡
def QiDongShiWuHu(_data):
    create_room_data = {}
    HongHeiDian = 0
    TingHu = 0
    for name, value in _data.items():
        if name == "人数":
            create_room_data['gamePlayer'] = value

        elif name == "局数":
            create_room_data['gameCiShu'] = value

        elif name == "起胡":
            if value == "15息起胡":
                create_room_data['gameQiHu'] = 0

        elif name == "胡一等":
            if value == "3息1囤":
                create_room_data['gameHuYiDeng'] = 0

        elif name == "翻醒":
            if value == "不带醒":
                create_room_data["gameFanXing"] = 2

            elif value == "翻醒":
                create_room_data["gameFanXing"] = 0

            elif value == "随醒":
                create_room_data["gameFanXing"] = 1

        elif name == "必胡":
            if value == "无":
                create_room_data['gameDianPaoBiHu'] = 2
            elif value == "点炮必胡":
                create_room_data['gameDianPaoBiHu'] = 0
            elif value == "有胡必胡":
                create_room_data['gameDianPaoBiHu'] = 1

        elif name == "底分":
            if value == "底分2分":
                create_room_data['gameDiFen'] = 1

        elif name == "名堂":
            for wanfa in value:
                if wanfa == "红黑点":
                    HongHeiDian = 2

            if "听胡" not in value:
                TingHu = 2097152

            create_room_data['gameWanFa'] = TingHu + HongHeiDian

        elif name == "自摸":
            if value == "自摸翻倍":
                    create_room_data['gameZiMoFanBei'] = 0

    create_room_data["gameRoomType"] = "21"
    return create_room_data

#   湘乡告胡子
def XiangXiangGaoHuZi(_data):
    create_room_data = {}
    Tips = 0
    double = 0
    integral_double = 0
    for name, value in _data.items():
        if name == "人数":
            create_room_data['gamePlayer'] = value

        elif name == "名堂":
            for wanfa in value:
                if wanfa == "总结算翻倍提示":
                    Tips = 134217728

            create_room_data['gameWanFa'] =Tips

        elif name == "牌数":
            if value == "不抽底牌":
                create_room_data["gamePaiShu"] = 0
            elif value == "抽牌20张":
                create_room_data["gamePaiShu"] = 1

        elif name == "加坨":
            if value == "打坨":
                create_room_data['gameJiaTuo'] = 1

        elif name == "积分加倍":
            if value == "不加倍":
                double = 0
            elif value == "低于50分加倍":
                integral_double = 65536
            elif value == "低于100分加倍":
                integral_double = 131072
            elif value == "低于150分加倍":
                integral_double = 262144
            elif value == "不限分加倍":
                integral_double = 0

        elif name == "翻倍":
            if value == "翻2倍":
                double = 1
            elif value == "翻3倍":
                double = 2
            elif value == "翻4倍":
                double = 4
    create_room_data['gameVip'] = double + integral_double

    create_room_data["gameRoomType"] = "7"
    return create_room_data

#   常德跑胡子
def ChangDePaoHuZi(_data):
    create_room_data = {}
    HongHeiDian = 0
    QuanMingTang = 0
    DuoHongDui = 0
    DaTuanYuan = 0
    HangHangXi = 0
    ShuaHou = 0
    TingHu = 0
    HuangFan = 0
    JiaHangHang = 0
    SiQiHong = 0
    for name, value in _data.items():
        if name == "人数":
            create_room_data['gamePlayer'] = value

        elif name == "局数":
            create_room_data['gameCiShu'] = value

        elif name == "封顶":
            if value == "不封顶":
                create_room_data['gameFengDing'] = 0
            elif value == "100封顶":
                create_room_data['gameFengDing'] = 100
            elif value == "200封顶":
                create_room_data['gameFengDing'] = 200
            elif value == "300封顶":
                create_room_data['gameFengDing'] = 300

        elif name == "名堂":
            for wanfa in value:
                if wanfa == "大团圆":
                    DaTuanYuan = 32
                elif wanfa == "行行息":
                    HangHangXi = 64
                elif wanfa == "耍猴":
                    ShuaHou = 256
                elif wanfa == "听胡":
                    TingHu = 0
                elif wanfa == "黄番2倍":
                    HuangFan = 4194304
                elif wanfa == "假行行":
                    JiaHangHang = 8388608
                elif wanfa == "四七红":
                    SiQiHong = 16777216
                elif wanfa == "全名堂":
                    QuanMingTang = 1
                elif wanfa == "红黑点":
                    HongHeiDian = 2
                elif wanfa == "多红对":
                    DuoHongDui = 4

            if "听胡" not in value:
                TingHu = 2097152

            create_room_data['gameWanFa'] =TingHu + HuangFan + JiaHangHang + SiQiHong + ShuaHou + HangHangXi +  DaTuanYuan + QuanMingTang + HongHeiDian + DuoHongDui

        elif name == "牌数":
            if value == "不抽底牌":
                create_room_data["gamePaiShu"] = 0
            elif value == "抽牌20张":
                create_room_data["gamePaiShu"] = 1

        elif name == "底分":
            if value == "底分1分":
                create_room_data['gameDiFen'] = 0
            elif value == "底分2分":
                create_room_data['gameDiFen'] = 1
            elif value == "底分3分":
                create_room_data['gameDiFen'] = 2
            elif value == "底分4分":
                create_room_data['gameDiFen'] = 3
            elif value == "底分5分":
                create_room_data['gameDiFen'] = 4

    create_room_data["gameRoomType"] = "4"

    print("常德: %s" % create_room_data)

    return create_room_data

#   长沙跑胡子
def ChangShaPaoHuZi(_data):
    create_room_data = {}
    JiaHong = 0
    ShiSanHong = 0
    JiaXiao = 0
    ShiBaXiao = 0
    WuShiBaXiao = 0
    ShiLiuXiao = 0
    JiaDa = 0
    ShiBaDa = 0
    WuShiBaDa = 0
    ShuaHou = 0
    HaiDi = 0
    TwoFan = 0
    TwoFen = 0
    for name, value in _data.items():
        if name == "人数":
            create_room_data['gamePlayer'] = value

        elif name == "局数":
            create_room_data['gameCiShu'] = value

        elif name == "底分":
            if value == "底分1分":
                create_room_data['gameDiFen'] = 0
            elif value == "底分2分":
                create_room_data['gameDiFen'] = 1
            elif value == "底分3分":
                create_room_data['gameDiFen'] = 2

        elif name == "起胡":
            if value == "15息起胡":
                create_room_data['gameQiHu'] = 0
            elif value == "9息起胡":
                create_room_data['gameQiHu'] = 1

        elif name == "扎鸟":
            if value == "扎鸟2分":
                create_room_data['gameDaNiao'] = 1
            elif value == "扎鸟3分":
                create_room_data['gameDaNiao'] = 2
            elif value == "扎鸟5分":
                create_room_data['gameDaNiao'] = 3
            elif value == "无":
                create_room_data['gameDaNiao'] = 0

        elif name == "封顶":
            if value == "单局200封顶":
                create_room_data['gameFengDing'] = 200
            elif value == "单局300封顶":
                create_room_data['gameFengDing'] = 300

        elif name == "番数":
            if value == "不限番":
                create_room_data['gameFanShu'] = 0
            elif value == "5番":
                create_room_data['gameFanShu'] = 5
            elif value == "10番":
                create_room_data['gameFanShu'] = 10

        elif name == "名堂":
            for wanfa in value:
                if wanfa == "红胡2加红加番":
                    JiaHong = 1024
                elif wanfa == "红胡2十三红5":
                    ShiSanHong = 2045

                elif wanfa == "十八小5加小加番":
                    JiaXiao = 4096

                elif wanfa == "十八小5":
                    ShiBaXiao = 8192

                elif wanfa == "无十八小":
                    WuShiBaXiao = 16384

                elif wanfa == "十六小5":
                    ShiLiuXiao = 1048576

                elif wanfa == "十八大5加大加番":
                    JiaDa = 32768

                elif wanfa == "十八大5":
                    ShiBaDa = 65536

                elif wanfa == "无十八大":
                    WuShiBaDa = 131072

                elif wanfa == "明偎":
                    create_room_data['gameZiMoFanBei'] = 0

                elif wanfa == "耍猴":
                    ShuaHou = 256

                elif wanfa == "海底":
                    HaiDi = 512

                elif wanfa == "自摸翻倍":
                    TwoFan = 262144
                    create_room_data['gameZiMoFanBei'] = 1


                elif wanfa == "自摸2分":
                    TwoFen = 524288

            create_room_data['gameWanFa'] =JiaHong + ShiSanHong + JiaXiao + ShiBaXiao + WuShiBaXiao + ShiLiuXiao + JiaDa + ShiBaDa + WuShiBaDa + ShuaHou + HaiDi + TwoFan + TwoFen


        elif name == "一五十":
            if value == "一五十":
                create_room_data['gameYiWuShi'] = 1


    create_room_data["gameRoomType"] = "6"

    print("长沙: %s" % create_room_data)

    return create_room_data

#   耒阳字牌
def LeiYangZiPai(_data):
    create_room_data = {}
    option = None
    for name, value in _data.items():
        if name == 'o_round':
            create_room_data['gameCiShu'] = value

        elif name == "o_jszs":#举手做声
            js = -1
            option = conversion_of_number_systems(js)

        elif name == "o_bdwh":#不带无胡
            wuhuIndex = -2
            option = conversion_of_number_systems(wuhuIndex)
        elif name == "o_bdydh":#不带一点红
            wuHongIndex = -3
            option = conversion_of_number_systems(wuHongIndex)
        elif name == "o_yxqp":#运行弃牌
            qiPaiIndex = -5
            option = conversion_of_number_systems(qiPaiIndex)
        elif name == 'o_dianpao_hu': #点炮必胡
            if value is 1:
                create_room_data["gameDianPaoBiHu"] = 0     #点炮必胡
            else:
                create_room_data["gameDianPaoBiHu"] = 2     #无


    if option is not None:
        gameWanfa = systemTow_transform(option)
        create_room_data['gameWanFa'] = gameWanfa

    create_room_data["gameRoomType"] = "12"
    return create_room_data


def RoomDataReplace(_type, _data):
    switcher = {
        "邵阳字牌": ShaoYangZiPai,
        "邵阳剥皮": ShaoYaoBoPi,
        "娄底放炮罚": LouDiFangPaoFa,
        "衡阳六胡抢": HengYangLiuHuQiang,
        "衡阳十胡卡": HengYangShiHuKa,
        "怀化红拐弯": HuaiHuaHongGuaiWan,
        "衡阳百胡": HengYangBaiHu,
        "四六八红拐弯": SiLiuBaHongGuaiWan,
        "邵阳放炮罚": ShaoYangFangPaoFa,
        "攸县碰胡子": YouXianPengHuZi,
        "祁东十五胡": QiDongShiWuHu,
        "郴州字牌": ChenZhouZiPai,
        "湘乡告胡子": XiangXiangGaoHuZi,
        "常德跑胡子": ChangDePaoHuZi,
        "长沙跑胡子": ChangShaPaoHuZi,
        "耒阳字牌": LeiYangZiPai,
        "永丰跑胡子": YongFengPaoHuZi,
        "益阳歪胡子": YiYangWaiHuZi,
    }

    try:
        print(111, _type)
        return switcher[_type](_data)

    except Exception as e:
        print("没有此玩法--> %s, 查看当前玩法名字是否正确." % _type)


if __name__ == "__main__":
    a = conversion_of_number_systems(-10)
