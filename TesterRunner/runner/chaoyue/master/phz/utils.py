#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@ author: Hubery
@ create on: 2018/10/16 14:49
@ file: utils.py
@ site: 
@ purpose: 
"""
from runner.logger import *
import struct

default = ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                   '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                   '0', '0', '0', '0', '0', '0', '0', '0', '0']


runfast_default = ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0','0']
majiang_default = ['0','0','0', '0', '0', '0', '0', '0', '0', '0', '0', '0','0']
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
    23: "岳阳歪胡子",
    25: "跑得快15张",
    26: "跑得快16张",
    27: "红中麻将",
    28: "长沙麻将",
    29: "转转麻将",
    30: "衡阳麻将",
    31: "新宁麻将",
    32: "邵阳麻将",
    33: "靖州麻将",

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
        logging.info("暂未做此操作说明, 请说明该操作应用于哪个玩法, 进行添加!")
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
    logging.info("邵阳字牌玩法选项: %s" % _data)
    for k, v in _data.items():
        if v is not "":
            if k == "o_player":
                create_room_data["gamePlayer"] = v
            if k == "o_round":
                create_room_data["gameCiShu"] = v
            if k == "o_huyideng":
                if v == "5息1囤":
                    create_room_data["gameHuYiDeng"] = 0
                elif v == "3息1囤":
                    create_room_data["gameHuYiDeng"] = 1
            if k == "o_jiachui":
                if v is True:
                    jiachui = -10
                    wanfa = conversion_of_number_systems(jiachui)
                    jc_data = systemTow_transform(wanfa)  # 加锤参数
                    create_room_data["gameWanFa"] = jc_data
            if k == "o_card_num":
                if v == "抽牌20张":
                    create_room_data["gamePaiShu"] = 1
                elif v == "抽牌10张":
                    create_room_data["gamePaiShu"] = 2
                else:
                    create_room_data["gamePaiShu"] = 0
    create_room_data["gameRoomType"] = "1"

    return create_room_data

#   邵阳剥皮创建房间设置
def ShaoYaoBoPi(_data):
    logging.info("邵阳剥皮玩法选项: %s"%_data)
    create_room_data = {}
    option = None
    integral_double = 0
    double = 0
    for k, v in _data.items():
        if v is not "":
            if k == "o_player":
                create_room_data["gamePlayer"] = v
            if k == "o_card_num":
                if v == "抽牌20张":
                    create_room_data["gamePaiShu"] = 1
                elif v == "抽牌10张":
                    create_room_data["gamePaiShu"] = 2
                else:
                    create_room_data["gamePaiShu"] = 0
            if k == "o_RedAndBlack":
                if v is True:
                    red_black_index = -2
                    option = conversion_of_number_systems(red_black_index)
        if k == "o_lianzhuang":
            if v is True:
                create_room_data['gameBPLianZhuang'] = 0

            if k == "o_0fen":
                if v is True:
                    shanggao_index = -8
                    option = conversion_of_number_systems(shanggao_index)

        if k == "o_jiachui":
            if v is True:
                shanggao_index = -8
                option = conversion_of_number_systems(shanggao_index)

        if k == 'o_NoShow_dipai':
            if v is True:
                dipai_index = -28
                option = conversion_of_number_systems(dipai_index)
        if k == 'o_fengdinghuxi':
            if v == "100":
                create_room_data['gameFengDing'] = 100
            elif v == "150":
                create_room_data['gameFengDing'] = 150
            elif v == "200":
                create_room_data['gameFengDing'] = 200
            elif v == "250":
                create_room_data['gameFengDing'] = 250
            elif v == "300":
                create_room_data['gameFengDing'] = 300
            else:
                create_room_data['gameFengDing'] = 0

        if k == "o_double":
            if v == 1:
                if int(_data["o_double_score"]) < 25:  # 小于25分加倍
                    integral_double = 524288
                elif int(_data["o_double_score"]) < 50:
                    integral_double = 65536
                elif int(_data["o_double_score"]) < 75:
                    integral_double = 1048576
                elif int(_data["o_double_score"]) <= 100:
                    integral_double = 131072
                else:
                    integral_double = 0
            else:
                double = 0
        if k == "o_double_plus":
            if v == 2:
                double = 1
            elif v == 3:
                double = 2
            elif v == 4:
                double = 4

    if option is not None:
        gameWanfa = systemTow_transform(option)
        create_room_data['gameWanFa'] = gameWanfa

    create_room_data['gameVip'] = integral_double + double
    create_room_data["gameRoomType"] = "2"
    logging.info("邵阳剥皮创房data: %s" % create_room_data)
    return create_room_data
   

#   娄底放炮罚
def LouDiFangPaoFa(_data):
    try:
        integral_double = 0
        double = 0
        create_room_data = {}
        logging.info("娄底放炮罚创房原始数据: %s" % _data)
        for k, v in _data.items():
            if v is not "":
                if k == "o_player":
                    create_room_data["gamePlayer"] = v
                if k == "o_choupai":
                    if v == "抽牌20张":
                        create_room_data["gamePaiShu"] = 1
                    elif v == "抽牌10张":
                        create_room_data["gamePaiShu"] = 2


                if k == 'o_fengdinghuxi':
                    if v == "200":
                        create_room_data['gameFengDing'] = 0
                    elif v == "400":
                        create_room_data['gameFengDing'] = 1

                if k == "o_double":
                    if v == 1:
                        if int(_data["o_double_score"]) < 25:  # 小于25分加倍
                            integral_double = 524288
                        elif int(_data["o_double_score"]) < 50:
                            integral_double = 65536
                        elif int(_data["o_double_score"]) < 75:
                            integral_double = 1048576
                        elif int(_data["o_double_score"]) <= 100:
                            integral_double = 131072
                        else:
                            integral_double = 0
                    else:
                        double = 0
                if k == "o_double_plus":
                    if v == 2:
                        double = 1
                    elif v == 3:
                        double = 2
                    elif v == 4:
                        double = 4
                if k == 'o_piaohu':
                    if v is True:
                        create_room_data['gameMaoHu'] = 1
                if k == "o_qihu":
                    if int(v) == 15:
                        create_room_data['gameQiHu'] = 0
                    elif int(v) == 10:
                        create_room_data['gameQiHu'] = 1
        create_room_data['gameVip'] = integral_double + double
        create_room_data["gameRoomType"] = "3"
        return create_room_data
    except Exception as err:
        logging.info(err)

    # Tips = 0  # 总结算翻倍提示
    # double = 0  # 翻倍
    # integral_double = 0  # 积分加倍
    # for name, value in _data.items():
    #     if name == "人数":
    #         create_room_data["gamePlayer"] = value
    #     elif name == "名堂":
    #         for wanfa in value:
    #             if wanfa == "飘胡":
    #                 create_room_data['gameMaoHu'] = 1
    #
    #             elif wanfa == "总结算翻倍提示":
    #                 Tips = 134217728
    #
    #         if "总结算翻倍提示" not in value:
    #             Tips = 0
    #
    #         create_room_data['gameWanFa'] = Tips
    #
    #
    #     elif name == "封顶":
    #         if value == "200息":
    #             create_room_data['gameFengDing'] = 0
    #         elif value == "400息":
    #             create_room_data['gameFengDing'] = 1
    #
    #     elif name == "牌数":
    #         if value == "不抽底牌":
    #             create_room_data["gamePaiShu"] = 0
    #
    #         elif value == "抽牌20张":
    #             create_room_data["gamePaiShu"] = 1
    #
    #     elif name == "积分加倍":
    #         if value == "不加倍":
    #             integral_double = 0
    #         elif value == "大于50分不加倍":
    #             integral_double = 524288
    #         elif value == "大于100分不加倍":
    #             integral_double = 65536
    #         elif value == "大于150分不加倍":
    #             integral_double = 1048576
    #         elif value == "大于200分不加倍":
    #             integral_double = 131072
    #         elif value == "不限分加倍":
    #             integral_double = 131072
    #
    #     elif name == "翻倍":
    #         if value == "翻2倍":
    #             double = 1
    #         elif value == "翻3倍":
    #             double = 2
    #         elif value == "翻4倍":
    #             double = 4


#   衡阳六胡抢
def HengYangLiuHuQiang(_data):
    logging.info("衡阳六胡抢创房原始数据: %s" % _data)
    create_room_data = {}
    option = None
    integral_double = 0
    double = 0
    CardNum = 0
    for k, v in _data.items():
        if v is not "":
            if k == "o_player":
                create_room_data["gamePlayer"] = v
            if k == "o_round":
                create_room_data["gameCiShu"] = int(v)

            if create_room_data["gamePlayer"] is 2:
                if k == "o_chou_card":
                    if v == "20":
                        CardNum = 1
                    elif v == "10":
                        CardNum = 2

                if k == "o_double":
                    if v == 1:
                        if int(_data["o_double_score"]) < 25:  # 小于25分加倍
                            integral_double = 524288
                        elif int(_data["o_double_score"]) < 50:
                            integral_double = 65536
                        elif int(_data["o_double_score"]) < 75:
                            integral_double = 1048576
                        elif int(_data["o_double_score"]) <= 100:
                            integral_double = 131072
                        else:
                            integral_double = 0
                    else:
                        double = 0
                if k == "o_double_plus":
                    if v == 2:
                        double = 1
                    elif v == 3:
                        double = 2
                    elif v == 4:
                        double = 4

            if create_room_data["gamePlayer"] == 2 or create_room_data["gamePlayer"] == 3:
                if k == "o_cards_num":
                    if v == "21张":
                        create_room_data["gamePaiShu"] = CardNum + 16
                    elif v == "15张":
                        create_room_data["gamePaiShu"] = CardNum + 32

            if k == "o_fanxing":
                if v == "不带醒":
                    create_room_data["gameFanXing"] = 2
                elif v == "翻醒":
                    create_room_data["gameFanXing"] = 0
                elif v == "随醒":
                    create_room_data["gameFanXing"] = 1

            if k == "o_tunshu":
                if v == "3息1囤":
                    create_room_data["gameHuYiDeng"] = 0
                elif v == "1息1囤":
                    create_room_data["gameHuYiDeng"] = 1
            if k == "o_qihu":
                if v == "6息起胡":
                    create_room_data["gameQiHu"] = 0
                elif v == "9息起胡":
                    create_room_data["gameQiHu"] = 1
                elif v == "15息起胡":
                    create_room_data["gameQiHu"] = 2

            if k == "o_hu_pao":
                if v == "有胡必胡":
                    create_room_data["gameDianPaoBiHu"] = 1
                elif v == "点炮必胡":
                    create_room_data["gameDianPaoBiHu"] = 0

            if k == "o_fengding":
                if v == "单局30封顶":
                    create_room_data["gameFengDing"] = 30
                elif v == "单局60封顶":
                    create_room_data["gameFengDing"] = 60
                elif v == "单局90封顶":
                    create_room_data["gameFengDing"] = 90
                else:
                    create_room_data["gameFengDing"] = 0
            if k == "o_mingwei":
                if v is True:
                    create_room_data['gameZiMoFanBei'] = 0

            if k == "o_red_black":
                if v is True:
                    _index = -2
                    option = conversion_of_number_systems(_index)
            if k == "o_yiwushi":
                if v is True:
                    create_room_data['gameYiWuShi'] = 1
            if k == "o_difen":
                if v is True:
                    create_room_data['gameDiFen'] = 1
            if k == "o_hu_public":
                if v is True:
                    create_room_data['gameShiZhongPai'] = 1
            if k == "o_piaohu":
                if v is True:
                    create_room_data['gameMaoHu'] = 1
            if k == "o_tdhdh":
                if v is True:
                    create_room_data['gameBPLianZhuang'] = 1

    if option is not None:
        gameWanfa = systemTow_transform(option)
        create_room_data['gameWanFa'] = gameWanfa

    create_room_data['gameVip'] = integral_double + double
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
    logging.info("怀化红拐弯创房原始数据: %s"%_data)
    create_room_data = {}
    option = None
    integral_double = 0
    double = 0
    for k, v in _data.items():
        if v is not "":
            if k == "o_player":
                create_room_data["gamePlayer"] = v
            if k == "o_card_num":
                if v == "抽牌20张":
                    create_room_data["gamePaiShu"] = 1
                elif v == "抽牌10张":
                    create_room_data["gamePaiShu"] = 2
                else:
                    create_room_data["gamePaiShu"] = 0

            if k == "o_jushu":
                create_room_data["gameCiShu"] = int(v)

            if k == "o_hu_15":
                if v is True:
                    create_room_data['gameQiHu'] = 1
            if k == "o_qianghu":
                if v is True:
                    red_black_index = -26
                    option = conversion_of_number_systems(red_black_index)

            if k == "o_difen":
                value = int(v)
                if value == 1:
                    create_room_data['gameDiFen'] = 0
                elif value == 2:
                    create_room_data['gameDiFen'] = 1
                elif value == 3:
                    create_room_data['gameDiFen'] = 2
                elif value == 4:
                    create_room_data['gameDiFen'] = 3
                elif value == 5:
                    create_room_data['gameDiFen'] = 4

            if k == "o_double":
                if v == 1:
                    if int(_data["o_double_score"]) < 25:  # 小于25分加倍
                        integral_double = 524288
                    elif int(_data["o_double_score"]) < 50:
                        integral_double = 65536
                    elif int(_data["o_double_score"]) < 75:
                        integral_double = 1048576
                    elif int(_data["o_double_score"]) <= 100:
                        integral_double = 131072
                    else:
                        integral_double = 0
                else:
                    double = 0
            if k == "o_double_plus":
                if v == 2:
                    double = 1
                elif v == 3:
                    double = 2
                elif v == 4:
                    double = 4

        if k == 'o_fengdinghuxi':
            if v == "100":
                create_room_data['gameFengDing'] = 100
            elif v == "150":
                create_room_data['gameFengDing'] = 150
            elif v == "200":
                create_room_data['gameFengDing'] = 200
            elif v == "250":
                create_room_data['gameFengDing'] = 250
            elif v == "300":
                create_room_data['gameFengDing'] = 300
            else:
                create_room_data['gameFengDing'] = 0

    if option is not None:
        gameWanfa = systemTow_transform(option)
        create_room_data['gameWanFa'] = gameWanfa

    create_room_data['gameVip'] = integral_double + double
    create_room_data["gameRoomType"] = "9"
    return create_room_data

#   益阳歪胡子
def YiYangWaiHuZi(_data):
    logging.info("益阳歪胡子创房原始数据: %s" % _data)
    create_room_data = {}
    for k, v in _data.items():
        if v is not "":
            if k == "o_player":
                create_room_data["gamePlayer"] = v
            if k == "o_round":
                create_room_data["gameCiShu"] = int(v)

            if create_room_data["gamePlayer"] is 2:
                if k == "o_card_num":
                    if v == "抽牌20张":
                        create_room_data["gamePaiShu"] = 1
                    elif v == "抽牌10张":
                        create_room_data["gamePaiShu"] = 2

            if k == "o_fengding":
                create_room_data["gameFengDing"] = int(v)

            if k == "o_qihu":
                create_room_data["gameQiHu"] = int(v)

            create_room_data["gameWanFa"] = 25

    create_room_data["gameRoomType"] = "20"

    return create_room_data

#   衡阳百胡
def HengYangBaiHu(_data):
    create_room_data = {}
    for name, value in _data.items():
        if name == "o_huxi":
            if int(value) == 200:
                create_room_data['gameFengDing'] = 0
            elif int(value) == 400:
                create_room_data['gameFengDing'] = 1

    create_room_data["gameRoomType"] = "22"
    return create_room_data

#   四六八红拐弯
def SiLiuBaHongGuaiWan(_data):
    create_room_data = {}
    integral_double = 0
    double = 0
    for k, v in _data.items():
        if v is not "":
            if k == "o_player":
                create_room_data["gamePlayer"] = v
            if k == "o_round":
                create_room_data["gameCiShu"] = int(v)

            if create_room_data["gamePlayer"] is 3:
                break
            else:
                if k == "o_chou_card":
                    if v == "抽牌20张":
                        create_room_data["gamePaiShu"] = 1
                    elif v == "抽牌10张":
                        create_room_data["gamePaiShu"] = 2
                if k == "o_double":
                    if v == 1:
                        if int(_data["o_double_score"]) < 25:  # 小于25分加倍
                            integral_double = 524288
                        elif int(_data["o_double_score"]) < 50:
                            integral_double = 65536
                        elif int(_data["o_double_score"]) < 75:
                            integral_double = 1048576
                        elif int(_data["o_double_score"]) <= 100:
                            integral_double = 131072
                        else:
                            integral_double = 0
                    else:
                        double = 0
                if k == "o_double_plus":
                    if v == 2:
                        double = 1
                    elif v == 3:
                        double = 2
                    elif v == 4:
                        double = 4

    create_room_data['gameVip'] = integral_double + double
    create_room_data["gameRoomType"] = "19"
    return create_room_data

#   永丰跑胡子
def YongFengPaoHuZi(_data):
    create_room_data = {}
    create_room_data["gameRoomType"] = "14"
    return create_room_data

#   邵阳放炮罚
def ShaoYangFangPaoFa(_data):
    logging.info("邵阳放炮罚玩法选项: %s" % _data)
    create_room_data = {}
    option = None
    for k, v in _data.items():
        if v is not "":
            if k == "o_player":
                create_room_data["gamePlayer"] = v

            if k == "o_red_black":
                if v is True:
                    red_black_index = -2
                    option = conversion_of_number_systems(red_black_index)
            if k == "o_zimodouble":
                if int(v) == 2:
                    pass
                elif int(v) == 1:  # 自摸翻倍
                    zimo_index = -19
                    option = conversion_of_number_systems(zimo_index)
    if option is not None:
        gameWanfa = systemTow_transform(option)
        create_room_data['gameWanFa'] = gameWanfa
    create_room_data["gameRoomType"] = "13"
    return create_room_data

#   攸县碰胡子
def YouXianPengHuZi(_data):
    logging.info("攸县碰胡子玩法选项: %s" % _data)
    try:
        create_room_data = {}
        for name, value in _data.items():
            if name == "o_zhongzhuang":
                if int(value) == 1:
                    create_room_data['gameLianZhuang'] = 0
                elif int(value) == 2:
                    create_room_data['gameLianZhuang'] = 1
            elif name == "o_jushu":
                create_room_data['gameCiShu'] = value

            elif name == "o_player":
                create_room_data['gamePlayer'] = value

            elif name == "o_wanfa":
                if int(value) == 0:
                    create_room_data['gameDianPaoBiHu'] = 2
                elif int(value) == 1:
                    create_room_data['gameDianPaoBiHu'] = 0
                elif int(value) == 2:
                    create_room_data['gameDianPaoBiHu'] = 1

        create_room_data["gameRoomType"] = "11"
        return create_room_data
    except Exception as err:
        logging.info(err)


#   郴州字牌
def ChenZhouZiPai(_data):
    logging.info("郴州字牌玩法选项: %s" % _data)
    create_room_data = {}
    double = 0
    integral_double = 0
    for k, v in _data.items():
        if v is not "":
            if k == "o_player":
                create_room_data["gamePlayer"] = v
            if k == "o_round":
                create_room_data['gameCiShu'] = int(v)

            if k == "o_qihu":
                if int(v) == 6:
                    create_room_data['gameQiHu'] = 1
                else:
                    create_room_data['gameQiHu'] = 0
            if k == "o_tun":
                if int(v) == 3:
                    create_room_data['gameHuYiDeng'] = 0
                else:
                    create_room_data['gameHuYiDeng'] = 1
            if k == "o_redBlack":
                if v is True:
                    red_black_index = -2
                    option = conversion_of_number_systems(red_black_index)
                    readBlak = systemTow_transform(option)
                    create_room_data["gameWanFa"] = readBlak

            if k == "o_maohu":
                if v is True:
                    create_room_data['gameMaoHu'] = 1
                else:
                    create_room_data['gameMaoHu'] = 0

            if k == "o_dinapaobihu":
                if int(v) == 0:
                    create_room_data['gameDianPaoBiHu'] = 2
                elif int(v) == 2:
                    create_room_data['gameDianPaoBiHu'] = 1
                else:
                    create_room_data['gameDianPaoBiHu'] = 0

            if k == "o_zomoDouble":
                if v is True:
                    create_room_data['gameZiMoFanBei'] = 0
                else:
                    create_room_data['gameZiMoFanBei'] = 1

            if k == "o_difen":
                if int(v) == 2:
                    create_room_data['gameDiFen'] = 1
                elif int(v) == 3:
                    create_room_data['gameDiFen'] = 2
                elif int(v) == 4:
                    create_room_data['gameDiFen'] = 3
                elif int(v) == 5:
                    create_room_data['gameDiFen'] = 4
                else:
                    create_room_data['gameDiFen'] = 0

            if k == "o_double":
                if v == 1:
                    if int(_data["o_double_score"]) < 25:  # 小于25分加倍
                        integral_double = 524288
                    elif int(_data["o_double_score"]) < 50:
                        integral_double = 65536
                    elif int(_data["o_double_score"]) < 75:
                        integral_double = 1048576
                    elif int(_data["o_double_score"]) <= 100:
                        integral_double = 131072
                    else:
                        integral_double = 0
                else:
                    double = 0
            if k == "o_double_plus":
                if v == 2:
                    double = 1
                elif v == 3:
                    double = 2
                elif v == 4:
                    double = 4


    #     elif name == "积分加倍":
    #         if value == "不加倍":
    #             double = 0
    #         elif value == "低于10分加倍":
    #             integral_double = 65536
    #         elif value == "低于15分加倍":
    #             integral_double = 131072
    #         elif value == "低于20分加倍":
    #             integral_double = 262144
    #         elif value == "不限分加倍":
    #             integral_double = 0
    #
    #     elif name == "翻倍":
    #         if value == "翻2倍":
    #             double = 1
    #         elif value == "翻3倍":
    #             double = 2
    #         elif value == "翻4倍":
    #             double = 4
    create_room_data['gameVip'] = double + integral_double
    create_room_data["gameRoomType"] = "10"
    return create_room_data

#   祁东十五胡
def QiDongShiWuHu(_data):
    logging.info("祁东十五胡创房原始数据: %s"%_data)
    create_room_data = {}
    option = None
    for k, v in _data.items():
        if v is not "":
            if k == "o_player":
                create_room_data["gamePlayer"] = v
            if k == "o_jushu":
                create_room_data["gameCiShu"] = int(v)
            if k == "o_fanxing":
                if v == "翻醒":
                    create_room_data["gameFanXing"] = 0
                elif v == "随醒":
                    create_room_data["gameFanXing"] = 1
                elif v == "不带醒":
                    create_room_data["gameFanXing"] = 2

            if k == "o_zimodouble":
                if v is True:
                    create_room_data['gameZiMoFanBei'] = 0
            if k == "o_difen":
                if v is True:
                    create_room_data['gameDiFen'] = 1
            if k == "o_redBlack":
                if v is True:
                    red_black_index = -2
                    option = conversion_of_number_systems(red_black_index)

            if k == "o_bihu":
                if v == 2:
                    create_room_data['gameDianPaoBiHu'] = 0
                elif v == 1:
                    create_room_data['gameDianPaoBiHu'] = 1
                elif v == 0:
                    create_room_data['gameDianPaoBiHu'] = 2

            if k == "o_hu_15":
                if v is 1:
                    create_room_data['gameQiHu'] = 0

            if k == "o_tun_3":
                if v is 1:
                    create_room_data['gameHuYiDeng'] = 0
    if option is not None:
        gameWanfa = systemTow_transform(option)
        create_room_data['gameWanFa'] = gameWanfa

    create_room_data["gameRoomType"] = "21"
    return create_room_data

#   湘乡告胡子
def XiangXiangGaoHuZi(_data):
    try:
        logging.info("湘乡告胡子玩法选项: %s" % _data)
        create_room_data = {}
        double = 0
        integral_double = 0
        for k, v in _data.items():
            if v is not "":
                if k == "o_player":
                    create_room_data["gamePlayer"] = v
                if k == "o_card_num":
                    if v == "抽牌20张":
                        create_room_data["gamePaiShu"] = 1
                    else:
                        create_room_data["gamePaiShu"] = 0

                if k == "o_datuo":
                    if v is True:
                        create_room_data["gameJiaTuo"] = 1
                if k == "o_double":
                    if v == 1:
                        if int(_data["o_double_score"]) < 25:  # 小于25分加倍
                            integral_double = 524288
                        elif int(_data["o_double_score"]) < 50:
                            integral_double = 65536
                        elif int(_data["o_double_score"]) < 75:
                            integral_double = 1048576
                        elif int(_data["o_double_score"]) <= 100:
                            integral_double = 131072
                        else:
                            integral_double = 0
                    else:
                        double = 0
                if k == "o_double_plus":
                    if v == 2:
                        double = 1
                    elif v == 3:
                        double = 2
                    elif v == 4:
                        double = 4
        create_room_data['gameVip'] = double + integral_double
        create_room_data["gameRoomType"] = "7"
        return create_room_data
    except Exception as err:
        logging.info(err)

#   常德跑胡子
def ChangDePaoHuZi(_data):
    try:
        create_room_data = {}
        logging.info("常德跑胡子玩法选项: %s" % _data)
        option = None
        for name, value in _data.items():
            if name == "o_player":
                create_room_data['gamePlayer'] = value

            if name == "o_round":
                create_room_data['gameCiShu'] = value

            if name == "o_fengding":
                if value == "":
                    create_room_data['gameFengDing'] = 0
                elif value == "100":
                    create_room_data['gameFengDing'] = 100
                elif value == "200":
                    create_room_data['gameFengDing'] = 200
                elif value == "300":
                    create_room_data['gameFengDing'] = 300

            if name == "o_mingtang":
                if value == "全名堂":
                    _index = -1
                    option = conversion_of_number_systems(_index)

                elif value == "红黑点":
                    _index = -2
                    option = conversion_of_number_systems(_index)
                elif value == "多红对":
                    _index = -3
                    option = conversion_of_number_systems(_index)
            if name == "o_mingwei":
                if value is True:
                    create_room_data['gameZiMoFanBei'] = 0
            if name == "o_datuanyuan":
                if value is True:
                    _index = -6
                    option = conversion_of_number_systems(_index)
            if name == "o_xingxingxi":
                if value is True:
                    _index = -7
                    option = conversion_of_number_systems(_index)
            if name == "o_shuahou":
                if value is True:
                    _index = -9
                    option = conversion_of_number_systems(_index)
            if name == "o_huangfanDouble":
                if value is True:
                    _index = -23
                    option = conversion_of_number_systems(_index)
            if name == "o_jiaxingxing":
                if value is True:
                    _index = -24
                    option = conversion_of_number_systems(_index)
            if name == "o_siqihong":
                if value is True:
                    _index = -25
                    option = conversion_of_number_systems(_index)
            if name == "o_yikuaibian":
                if value is True:
                    _index = -25
                    option = conversion_of_number_systems(_index)

            if name == "o_card_num":
                if value == "不抽底牌":
                    create_room_data["gamePaiShu"] = 0
                elif value == "抽牌20张":
                    create_room_data["gamePaiShu"] = 1
                elif value == "抽牌10张":
                    create_room_data["gamePaiShu"] = 2

            if name == "o_difen":
                if int(value) == 1:
                    create_room_data['gameDiFen'] = 0
                elif int(value) == 2:
                    create_room_data['gameDiFen'] = 1
                elif int(value) == 3:
                    create_room_data['gameDiFen'] = 2
                elif int(value) == 4:
                    create_room_data['gameDiFen'] = 3
                elif int(value) == 5:
                    create_room_data['gameDiFen'] = 4

        if option is not None:
            gameWanfa = systemTow_transform(option)
            create_room_data['gameWanFa'] = gameWanfa
        create_room_data["gameRoomType"] = "4"
        return create_room_data
    except Exception as  err:
        logging.info(err)



#   长沙跑胡子
def ChangShaPaoHuZi(_data):
    Val = ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0',
               '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
               '0', '0', '0', '0', '0', '0', '0', '0', ]
    option = None

    try:
        create_room_data = {}
        logging.info("长沙跑胡子创房原始数据: %s" % _data)
        for k, v in _data.items():
            if v is not "":
                if k == "o_player":
                    create_room_data["gamePlayer"] = v
                if k == "o_round":
                    create_room_data["gameCiShu"] = int(v)

                if create_room_data["gamePlayer"] is 2:
                    if k == "o_qihu":
                        if v is 15:
                            create_room_data["gameQiHu"] = 0
                        else:
                            create_room_data["gameQiHu"] = 1

                if k == "o_shuahou":
                    if v is True:
                        index = -9
                        option = conversion_of_number_systems(index,value=Val)
                if k == "o_haidi":
                    if v is True:
                        _index = -10
                        option = conversion_of_number_systems(_index,value=Val)
                if k == "o_haidi":
                    if v is True:
                        _index = -10
                        option = conversion_of_number_systems(_index,value=Val)
                if k == "o_haidi":
                    if v is True:
                        _index = -10
                        option = conversion_of_number_systems(_index,value=Val)
                if k == "o_honghu":
                    if v == "红胡2加红加番":
                        _index = -11
                        option = conversion_of_number_systems(_index,value=Val)
                    elif v == "红胡2十三红5":
                        _index = -12
                        option = conversion_of_number_systems(_index,value=Val)
                if k == "o_shiba":
                    if v == "十八小5加小番":
                        _index = -13
                        option = conversion_of_number_systems(_index,value=Val)
                    if v == "十八小5":
                        _index = -14
                        option = conversion_of_number_systems(_index,value=Val)
                    if v == "无十八小":
                        _index = -15
                        option = conversion_of_number_systems(_index,value=Val)
                    if v == "十六小5":
                        _index = -21
                        option = conversion_of_number_systems(_index,value=Val)
                if k == "o_shibada":
                    if v == "十八大5大加番":
                        _index = -16
                        option = conversion_of_number_systems(_index,value=Val)
                    if v == "十八大5":
                        _index = -17
                        option = conversion_of_number_systems(_index,value=Val)
                    if v == "无十八大":
                        _index = -18
                        option = conversion_of_number_systems(_index,value=Val)

                if k == "o_zhaniao":
                    create_room_data['gameDaNiao'] = int(v)

                if k == "o_yiwushi":
                    if v is True:
                        create_room_data['gameYiWuShi'] = 1
                if k == "o_mingwei":
                    if v is True:
                        create_room_data['gameZiMoFanBei'] = 0

                if k == "o_fanshu":
                    if v == "单局300封顶":
                        create_room_data['gameFengDing'] = 300
                        create_room_data['gameFanShu'] = -1
                    elif v == "10番":
                        create_room_data['gameFanShu'] = 10
                    elif v == "5番":
                        create_room_data['gameFanShu'] = 5
                    elif v == "不限番":
                        create_room_data['gameFanShu'] = 0
                    elif v == "单局200封顶":
                        create_room_data['gameFanShu'] = 200
                        create_room_data['gameFanShu'] = -1

                if k == "o_difen":
                    if v is 1:
                        create_room_data['gameDiFen'] = 0
                    elif v is 2:
                        create_room_data['gameDiFen'] = 1
                    else:
                        create_room_data['gameDiFen'] = 2


                if k == "o_zimo":
                    if v is 3:
                        _index = -20
                        option = conversion_of_number_systems(_index,value=Val)
                        create_room_data['gameZiMoFanBei'] = 1
                    elif v is 2:
                        create_room_data['gameZiMoFanBei'] = 0
                    elif v is 1:
                        _index = -19
                        option = conversion_of_number_systems(_index,value=Val)
                        create_room_data['gameZiMoFanBei'] = 1

        if option is not None:
            gameWanfa = systemTow_transform(option)
            create_room_data['gameWanFa'] = gameWanfa
        create_room_data["gameRoomType"] = "6"
        return create_room_data
    except Exception as err:
        logging.info(err)




#   耒阳字牌
def LeiYangZiPai(_data):
    create_room_data = {}
    option = None
    for k, v in _data.items():
        if v is not "":
            if k == "o_player":
                create_room_data["gamePlayer"] = v
            if k == "o_round":
                create_room_data["gameJuShu"] = int(v)

            if k == "o_dianpao_hu":
                if v is 1:
                    create_room_data["gameDianPaoBiHu"] = 0

            if k == "o_jszs":
                if v is True:
                    create_room_data["gameWanFa"] = 134217750
            else:
                create_room_data["gameWanFa"] = 134221846
    create_room_data["gameRoomType"] = "12"
    return create_room_data


#   跑得快15张
def RunfastFifteen(_data):
    create_room_data = {}
    option = None
    for k, v in _data.items():
        if v is not "":
            if k == "o_player":
                create_room_data["gamePlayer"] = v
            if k == "o_round":
                create_room_data["gameCiShu"] = int(v)

            if k == "o_showCard":
                if v is True:
                    _index = -9
                    option = conversion_of_number_systems(_index, runfast_default)
            if k == "o_zhuaNiao":
                if v is True:
                    _index = -2
                    option = conversion_of_number_systems(_index, runfast_default)
            if k == "o_outBig":
                if v is True:
                    _index = -4
                    option = conversion_of_number_systems(_index, runfast_default)
            if k == "o_nonSeparability":
                if v is True:
                    _index = -5
                    option = conversion_of_number_systems(_index, runfast_default)
            if k == "o_gaiPai":
                if v is True:
                    _index = -10
                    option = conversion_of_number_systems(_index, runfast_default)
            if k == "o_outThree":
                if v is True:
                    _index = -3
                    option = conversion_of_number_systems(_index, runfast_default)

    if option is not None:
        gameWanfa = systemTow_transform(option)
        create_room_data['gameWanFa'] = gameWanfa

    create_room_data["gameRoomType"] = "25"
    return  create_room_data

#   跑得快16张
def RunfastSixteen(_data):
    create_room_data = {}
    option = None
    for k, v in _data.items():
        if v is not "":
            if k == "o_player":
                create_room_data["gamePlayer"] = v
            if k == "o_round":
                create_room_data["gameCiShu"] = int(v)

            if k == "o_showCard":
                if v is True:
                    _index = -9
                    option = conversion_of_number_systems(_index, runfast_default)
            if k == "o_zhuaNiao":
                if v is True:
                    _index = -2
                    option = conversion_of_number_systems(_index, runfast_default)
            if k == "o_outBig":
                if v is True:
                    _index = -4
                    option = conversion_of_number_systems(_index, runfast_default)
            if k == "o_nonSeparability":
                if v is True:
                    _index = -5
                    option = conversion_of_number_systems(_index, runfast_default)
            if k == "o_gaiPai":
                if v is True:
                    _index = -10
                    option = conversion_of_number_systems(_index, runfast_default)
            if k == "o_outThree":
                if v is True:
                    _index = -3
                    option = conversion_of_number_systems(_index, runfast_default)

    if option is not None:
        gameWanfa = systemTow_transform(option)
        create_room_data['gameWanFa'] = gameWanfa

    create_room_data["gameRoomType"] = "26"
    return  create_room_data

def ChangshaMajiang(_data):
    create_room_data = {}
    wanfa = None
    option = None
    xianjia = 0
    yizhihua = 1
    liuliushun = 2
    queyise = 3
    banbanhu = 4
    dasixi = 5
    bubugao = 6
    santong = 7
    zhongtusixi = 8
    zhongtuliuliushun = 9
    jiajianghu = 10
    menqing = 11
    mingtang = 0

    for k, v in _data.items():
        if v is not "":
            if k == "o_player":
                create_room_data["gamePlayer"] = v
            if k == "o_round":
                create_room_data["gameJuShu"] = int(v)
            if k == "o_fengding":
                if v == 21:
                    create_room_data["gamePlayType"] = 1
                elif v == 42:
                    create_room_data["gamePlayType"] = 2
            if k == "o_zhongNiaoJiaFen":
                if v is True:
                    option = conversion_of_number_systems(-12,majiang_default)

            if k == "o_zhongNiaoFanBei":
                if v is True:
                    option = conversion_of_number_systems(-13,majiang_default)

            if k == "o_xianjia":
                if v is True:
                    mingtang += 2 ** xianjia
            if k == "o_yizhihua":
                if v is True:
                    mingtang += 2 ** yizhihua
            if k == "o_liuliushun":
                if v is True:
                    mingtang += 2 ** liuliushun
            if k == "o_queyise":
                if v is True:
                    mingtang += 2 ** queyise
            if k == "o_banbanhu":
                if v is True:
                    mingtang += 2 ** banbanhu
            if k == "o_dasixi":
                if v is True:
                    mingtang += 2 ** dasixi
            if k == "o_bubugao":
                if v is True:
                    mingtang += 2 ** bubugao
            if k == "o_santong":
                if v is True:
                    mingtang += 2 ** santong
            if k == "o_zhongtusixi":
                if v is True:
                    mingtang += 2 ** zhongtusixi
            if k == "o_zhongtuliuliushun":
                if v is True:
                    mingtang += 2 ** zhongtuliuliushun
            if k == "o_jiajianghu":
                if v is True:
                    mingtang += 2 ** jiajianghu
            if k == "o_meiqing":
                if v is True:
                    mingtang += 2 ** menqing

            if k == "o_qieyimen":
                if v is True:
                    create_room_data['gameWanFa'] = 2048
                    create_room_data['gameZhaMa'] = 3
            if k == "o_chouforty":
                if v is True:
                    create_room_data['gameWanFa'] = 128
                    create_room_data['gameZhaMa'] = 3

    if option is not None:
        gameWanfa = systemTow_transform(option)
        zhaMa_data = gameWanfa + _data["o_Zhuaniao"]
        create_room_data['gameZhaMa'] = zhaMa_data
    else:
        if _data["o_qieyimen"] != True and _data["o_chouforty"] != True:
            zhaMa_data = _data["o_Zhuaniao"]
            create_room_data['gameZhaMa'] = zhaMa_data

    create_room_data['gameMingTang'] = mingtang
    create_room_data["gameRoomType"] = "28"
    return  create_room_data

def HongZhongMajiang(_data):
    create_room_data = {}
    wanfa = 0
    option = None
    mingtang = 0

    for k, v in _data.items():
        if v is not "":
            if k == "o_player":
                create_room_data["gamePlayer"] = v
            if k == "o_round":
                create_room_data["gameJuShu"] = int(v)
            if k == "o_zimohu":
                if v == "可抢杠胡":
                    create_room_data["gamePlayType"] = 0
                elif v == '不可抢杠胡':
                    create_room_data["gamePlayType"] = 1
                elif v == '点炮胡':
                    create_room_data["gamePlayType"] = 2

            if k == "o_jiama":
                if v == "不加码":
                    option = conversion_of_number_systems(-9)
                elif v == "加1码":
                    option = conversion_of_number_systems(-10)
                elif v == "加2码":
                    option = conversion_of_number_systems(-11)

            if k == "o_sevenPair":
                if v is True:
                    wanfa += 2 ** 1
            if k == "o_zhongMa":
                if v is True:
                    wanfa += 2 ** 2
            if k == "o_piaofen":
                if v is True:
                    wanfa += 2 ** 3
            if k == "o_eighthongzhong":
                if v is True:
                    wanfa += 2 ** 4
            if k == "o_kejiepao":
                if v is True:
                    wanfa += 2 ** 5

    create_room_data["gameWanFa"] = wanfa

    if option is not None:
        if (_data["o_zhuaMa"] != "all") and (_data["o_zhuaMa"] != "不扎"):
            gameWanfa = systemTow_transform(option)
            zhaMa_data = gameWanfa + _data["o_zhuaMa"]
            create_room_data['gameZhaMa'] = zhaMa_data
        else:
            if _data["o_zhuaMa"] == "all":
                create_room_data['gameZhaMa'] = 1
            elif _data["o_zhuaMa"] == "不扎":
                create_room_data['gameZhaMa'] = 0

    create_room_data['gameMingTang'] = mingtang
    create_room_data["gameRoomType"] = "27"
    return create_room_data
def ZhuanZhuanMajiang(_data):
    create_room_data = {}
    wanfa = 0
    for k, v in _data.items():
        if v is not "":
            if k == "o_player":
                create_room_data["gamePlayer"] = v
            if k == "o_round":
                create_room_data["gameJuShu"] = int(v)
            if k == "o_zimohu":
                if v == "可抢杠胡":
                    create_room_data["gamePlayType"] = 0
                elif v == '不可抢杠胡':
                    create_room_data["gamePlayType"] = 1
                elif v == '点炮胡':
                    create_room_data["gamePlayType"] = 2

            if k == "o_159zhongma":
                if v is True:
                    wanfa += 2 ** 2

            if k == "o_sevenPair":
                if v is True:
                    wanfa += 2 ** 1

            if k == "o_xianjia":
                if v is True:
                    wanfa += 2 ** 8
            if k == "o_hongzhonglaizi":
                if v is True:
                    wanfa += 2 ** 7

            if k == "o_youpaibihu":
                if v is True:
                    wanfa += 2 ** 10
            if k == "o_qigang":
                if v is True:
                    wanfa += 2 ** 9
            if k == "o_bankerzhongniao":
                if v is True:
                    wanfa += 2 ** 11

    create_room_data["gameWanFa"] = wanfa
    if _data["o_zhuaMa"] == "不扎":
        create_room_data['gameZhaMa'] = 0
    else:
        create_room_data['gameZhaMa'] = int(_data["o_zhuaMa"])
    create_room_data["gameRoomType"] = "29"
    return create_room_data
def XinNingMajiang(_data):
    create_room_data = {}
    wanfa = 0

    for k, v in _data.items():
        if v is not "":
            if k == "o_player":
                create_room_data["gamePlayer"] = v
            if k == "o_round":
                create_room_data["gameJuShu"] = int(v)

            if k == "o_daifeng":
                if v is True:
                    wanfa += 2 ** 8

            if k == "o_chi":
                if v is True:
                    wanfa += 2 ** 9

            if k == "o_choupai":
                if v is True:
                    wanfa += 2 ** 7

            if k == "o_jiachui":
                if v is True:
                    wanfa += 2 ** 10
            if k == "o_saizi":
                if v == 3:
                    wanfa += 2 ** 14
                elif v == 6:
                    wanfa += 2 ** 15
                elif v == 9:
                    wanfa += 2 ** 16
    if _data["o_jiachui"] is True:
        if _data["o_lianchui"] is True:
            wanfa += 2 ** 13
        elif _data["o_bankerchui"] is True:
            wanfa += 2 ** 11
        elif _data["o_bichui"] is True:
            wanfa += 2 ** 12
    create_room_data["gameWanFa"] = wanfa
    if _data["o_zhuaMa"] == "不扎":
        create_room_data['gameZhaMa'] = 0
    else:
        create_room_data['gameZhaMa'] = int(_data["o_zhuaMa"])
    create_room_data["gameRoomType"] = "31"
    return create_room_data
def HengYangMajiang(_data):
    create_room_data = {}
    wanfa = 0
    mingtang = 0
    for k, v in _data.items():
        if v is not "":
            if k == "o_player":
                create_room_data["gamePlayer"] = v
            if k == "o_round":
                create_room_data["gameJuShu"] = int(v)
            if k == "o_zhuaNiao":
                create_room_data['gameZhaMa'] = int(v)

            if k == "o_yao":
                if v == 1:
                    wanfa += 2 ** 9
                elif v == 2:
                    wanfa += 2 ** 8

            if k == "o_bankerZhuaNiao":
                if v is True:
                    wanfa += 2 ** 10
            if k == "o_choupai":
                if v is True:
                    wanfa += 2 ** 7

            if k == "o_quanrenqiu":
                if v is True:
                    mingtang += 2 ** 0
            if k == "o_douzhuang":
                if v == 3:
                    mingtang += 2 ** 1

    create_room_data["gamePlayType"] = 2
    create_room_data["gameWanFa"] = wanfa
    create_room_data["gameMingTang"] = mingtang
    create_room_data["gameRoomType"] = "30"
    return create_room_data
def ShaoYangMajiang(_data):
    create_room_data = {}
    wanfa = 0

    for k, v in _data.items():
        if v is not "":
            if k == "o_player":
                create_room_data["gamePlayer"] = v
            if k == "o_round":
                create_room_data["gameJuShu"] = int(v)
            if k == "o_zhuaMa":
                create_room_data['gameZhaMa'] = int(v)

            if k == "o_choupai":
                if v is True:
                    wanfa += 2 ** 7
            if k == "o_daifeng":
                if v is True:
                    wanfa += 2 ** 8
            if k == "o_chi":
                if v is True:
                    wanfa += 2 ** 9
            if k == "o_qingyisechi":
                if v is True:
                    wanfa += 2 ** 10
            if k == "o_jiachui":
                if v is True:
                    wanfa += 2 ** 11
            if k == "o_lianchui":
                if v is True:
                    wanfa += 2 ** 12

    create_room_data["gameWanFa"] = wanfa
    create_room_data["gameRoomType"] = "32"
    return create_room_data
def JingZhouMajiang(_data):
    val = ['0','0','0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    create_room_data = {}
    wanfa = 0
    zhama = None
    mingtang = 0
    for k, v in _data.items():
        if v is not "":
            if k == "o_player":
                create_room_data["gamePlayer"] = v
            if k == "o_round":
                create_room_data["gameJuShu"] = int(v)
            if k == "o_zhuaMa":
                create_room_data['gameZhaMa'] = int(v)

            if k == "o_chouforty":
                if v == 20:
                    wanfa += 2 ** 1
                elif v == 30:
                    wanfa += 2 ** 7
                elif v == 40:
                    wanfa += 2 ** 2
            if k == "o_youpaibihu":
                if v is True:
                    wanfa += 2 ** 3
            if k == "o_denghu":
                if v is True:
                    wanfa += 2 ** 5
            if k == "o_huDiejia":
                if v is True:
                    wanfa += 2 ** 4
            if k == "o_fengding":
                if v == 0:
                    create_room_data["gamePlayType"] = 0
                elif v == 3:
                    create_room_data["gamePlayType"] = 1
                elif v == 4:
                    create_room_data["gamePlayType"] = 2
                elif v == 5:
                    create_room_data["gamePlayType"] = 3

            if k == "o_zhongNiaoJiaFen":
                if v == "中鸟相加":
                    zhama = conversion_of_number_systems(-11,val)
                elif v == "中鸟翻倍":
                    zhama = conversion_of_number_systems(-12,val)
            if k == "o_zhuaniao":
                if v == "159中鸟":
                    zhama = conversion_of_number_systems(-10,val)
                elif v == "庄家159中鸟":
                    zhama = conversion_of_number_systems(-9,val)
            if k == "o_Zhuaniao":
                if v == 1:
                    zhama = conversion_of_number_systems(-1,val)
                elif v == 2:
                    zhama = conversion_of_number_systems(-2,val)
                elif v == 3:
                    for i in [1, 2]:
                        zhama = conversion_of_number_systems(i,val)
                elif v == 4:
                    zhama = conversion_of_number_systems(-3,val)
                elif v == 6:
                    for i in [2, 3]:
                        zhama = conversion_of_number_systems(i,val)

                elif v == 8:
                    zhama = conversion_of_number_systems(-4,val)

            if k == "o_hujiafen":
                if v == 1:
                    zhama = conversion_of_number_systems(-5,val)
                elif v == 2:
                    zhama = conversion_of_number_systems(-6,val)
                elif v == 3:
                    for i in [5, 6]:
                        zhama = conversion_of_number_systems(i,val)
                elif v == 4:
                    zhama = conversion_of_number_systems(-7,val)

            if k == "o_wujianghu":
                if v is True:
                    mingtang += 2 ** 0

            if k == "o_queyise":
                if v is True:
                    mingtang += 2 ** 1
            if k == "o_pengpenghu":
                if v is True:
                    mingtang += 2 ** 2

            if k == "o_qingyise":
                if v is True:
                    mingtang += 2 ** 3

            if k == "o_jiangjianghu":
                if v is True:
                    mingtang += 2 ** 4
            if k == "o_qixiaodui":
                if v is True:
                    mingtang += 2 ** 5
            if k == "o_dadiaoche":
                if v is True:
                    mingtang += 2 ** 6
            if k == "roomTypeVuale":
                if v == "俱乐部创房":
                    if _data["clubRoomTypeVuale"] == "金币创房":
                        create_room_data['gameClubId'] = int(_data["o_club_id"])
                        tlv_data = tlv_param()
                        create_room_data['gameTlvParam'] = str(tlv_data)

    if zhama is not None:
        zhaoma_data = systemTow_transform(zhama)
        create_room_data["gameZhaMa"] = zhaoma_data

    create_room_data["gameWanFa"] = wanfa
    create_room_data["gameMingTang"] = mingtang
    create_room_data["gameRoomType"] = "33"
    return  create_room_data

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
        "跑得快15张":RunfastFifteen,
        "跑得快16张": RunfastSixteen,
        "长沙麻将": ChangshaMajiang,
        "红中麻将": HongZhongMajiang,
        "转转麻将": ZhuanZhuanMajiang,
        "新宁麻将": XinNingMajiang,
        "衡阳麻将": HengYangMajiang,
        "邵阳麻将": ShaoYangMajiang,
        "靖州麻将": JingZhouMajiang,

        
    }
    try:
        return switcher[_type](_data)
    except Exception as e:
        logging.info("err: %s没有此玩法--> %s, 查看当前玩法名字是否正确." % (e,_type))
def tlv_param(tag=1,val=0):
    _tag = struct.pack('b', tag)
    _val_len = struct.pack('b', 4)
    _val = struct.pack("I", val)
    data = _tag+_val_len+_val
    return  bytes.decode(data)

if __name__ == "__main__":
    a = conversion_of_number_systems(-10)
