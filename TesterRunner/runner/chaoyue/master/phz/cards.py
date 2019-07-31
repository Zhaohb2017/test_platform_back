#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@ author: Hubery
@ create on: 2018/10/9 16:56
@ file: cards.py
@ site: 
@ purpose: define the card type
"""

#   连牌概况
class CardTypeInfo:
    def __init__(self):
        self.had_huxi_list = ['1s\x00', '1b\x00', '2s\x00', '2b\x00', '3s\x00', '3b\x00', '7s\x00', '7b\x00', 'Ts\x00',
                              'Tb\x00']

        self.red_word = ['2s\x00', '7s\x00', 'Ts\x00', '2b\x00', '7b\x00', 'Tb\x00']
        # 有息
        # 判断是否有123  益阳玩法无息
        self.ONE_TOW_THREE_s = ['1s\x00', '2s\x00', '3s\x00']
        self.ONE_TOW_THREE_b = ['1b\x00', '2b\x00', '3b\x00']

        # 判断是否有2710
        self.TWO_SEVEN_TEN_s = ['2s\x00', '7s\x00', 'Ts\x00']
        self.TWO_SEVEN_TEN_b = ['2b\x00', '7b\x00', 'Tb\x00']

        # 判断是否有1510
        self.ONE_FIVE_TEN_s = ['1s\x00', '5s\x00', 'Ts\x00']
        self.ONE_FIVE_TEN_b = ['1b\x00', '5b\x00', 'Tb\x00']

        # 无息
        # 234
        self.TWO_THREE_FOUR_s = ['2s\x00', '3s\x00', '4s\x00']
        self.TWO_THREE_FOUR_b = ['2b\x00', '3b\x00', '4b\x00']

        # 345
        self.THREE_FOUR_FIVE_s = ['3s\x00', '4s\x00', '5s\x00']
        self.THREE_FOUR_FIVE_b = ['3b\x00', '4b\x00', '5b\x00']

        # 456
        self.FOUR_FIVE_SIX_s = ['4s\x00', '5s\x00', '6s\x00']
        self.FOUR_FIVE_SIX_b = ['4b\x00', '5b\x00', '6b\x00']

        # 567
        self.FIVE_SIX_SEVEN_s = ['5s\x00', '6s\x00', '7s\x00']
        self.FIVE_SIX_SEVEN_b = ['5b\x00', '6b\x00', '7b\x00']

        # 678
        self.SIX_SEVEN_EIGHT_s = ['6s\x00', '7s\x00', '8s\x00']
        self.SIX_SEVEN_EIGHT_b = ['6b\x00', '7b\x00', '8b\x00']

        # 789
        self.SEVEN_EIGHT_NINE_s = ['7s\x00', '8s\x00', '9s\x00']
        self.SEVEN_EIGHT_NINE_b = ['7b\x00', '8b\x00', '9b\x00']

        # 8910
        self.EIGHT_NINE_TEN_s = ['8s\x00', '9s\x00', 'Ts\x00']
        self.EIGHT_NINE_TEN_b = ['8b\x00', '9b\x00', 'Tb\x00']

        # 全部连牌牌型
        self.init_card = [self.ONE_TOW_THREE_s, self.ONE_TOW_THREE_b, self.TWO_SEVEN_TEN_s, self.TWO_SEVEN_TEN_b,
                          self.ONE_FIVE_TEN_s, self.ONE_FIVE_TEN_b, self.TWO_THREE_FOUR_s, self.TWO_THREE_FOUR_b,
                          self.THREE_FOUR_FIVE_s, self.THREE_FOUR_FIVE_b, self.FOUR_FIVE_SIX_s, self.FOUR_FIVE_SIX_b,
                          self.FIVE_SIX_SEVEN_s, self.FIVE_SIX_SEVEN_b, self.SIX_SEVEN_EIGHT_s, self.SIX_SEVEN_EIGHT_b,
                          self.SEVEN_EIGHT_NINE_s, self.SEVEN_EIGHT_NINE_b, self.EIGHT_NINE_TEN_s,
                          self.EIGHT_NINE_TEN_b]

        # 除了15T的连牌
        self.normal_card_data = [self.ONE_TOW_THREE_s, self.ONE_TOW_THREE_b, self.TWO_SEVEN_TEN_s, self.TWO_SEVEN_TEN_b,
                                 self.TWO_THREE_FOUR_s, self.TWO_THREE_FOUR_b, self.THREE_FOUR_FIVE_s,
                                 self.THREE_FOUR_FIVE_b, self.FOUR_FIVE_SIX_s, self.FOUR_FIVE_SIX_b,
                                 self.FIVE_SIX_SEVEN_s, self.FIVE_SIX_SEVEN_b, self.SIX_SEVEN_EIGHT_s,
                                 self.SIX_SEVEN_EIGHT_b, self.SEVEN_EIGHT_NINE_s, self.SEVEN_EIGHT_NINE_b,
                                 self.EIGHT_NINE_TEN_s, self.EIGHT_NINE_TEN_b]

        #   特殊牌型15T
        self.special_15T_cards = [self.ONE_FIVE_TEN_s, self.ONE_FIVE_TEN_b]

        # 大字牌型
        self.card_big_word = [self.ONE_TOW_THREE_b, self.TWO_SEVEN_TEN_b, self.ONE_FIVE_TEN_b, self.TWO_THREE_FOUR_b,
                              self.THREE_FOUR_FIVE_b, self.FOUR_FIVE_SIX_b, self.FIVE_SIX_SEVEN_b,
                              self.SIX_SEVEN_EIGHT_b, self.SEVEN_EIGHT_NINE_b, self.EIGHT_NINE_TEN_b]

        # 小字牌型
        self.card_fine_print = [self.ONE_TOW_THREE_s, self.TWO_SEVEN_TEN_s, self.ONE_FIVE_TEN_s, self.TWO_THREE_FOUR_s,
                                self.THREE_FOUR_FIVE_s, self.FOUR_FIVE_SIX_s, self.FIVE_SIX_SEVEN_s,
                                self.SIX_SEVEN_EIGHT_s, self.SEVEN_EIGHT_NINE_s, self.EIGHT_NINE_TEN_s]

        # 连牌有息牌型
        self.had_xi_lian_cards = [self.ONE_TOW_THREE_s, self.ONE_TOW_THREE_b, self.TWO_SEVEN_TEN_s,
                                  self.TWO_SEVEN_TEN_b, self.ONE_FIVE_TEN_s, self.ONE_FIVE_TEN_b]

        # 纯红字连牌
        self.red_lian_cards = [self.TWO_SEVEN_TEN_s, self.TWO_SEVEN_TEN_b]

        # 含有红字
        self.had_red_lian_cards = [self.ONE_TOW_THREE_s, self.ONE_TOW_THREE_b, self.TWO_THREE_FOUR_s,
                                   self.TWO_THREE_FOUR_b, self.TWO_SEVEN_TEN_s, self.TWO_SEVEN_TEN_b,
                                   self.FIVE_SIX_SEVEN_s, self.FIVE_SIX_SEVEN_b, self.ONE_FIVE_TEN_s,
                                   self.ONE_FIVE_TEN_b, self.SIX_SEVEN_EIGHT_s, self.SIX_SEVEN_EIGHT_b,
                                   self.SEVEN_EIGHT_NINE_s, self.SEVEN_EIGHT_NINE_b, self.EIGHT_NINE_TEN_s,
                                   self.EIGHT_NINE_TEN_b]

        #   含有一个红字的
        self.had_one_red_lian_cards = [self.ONE_TOW_THREE_s, self.ONE_TOW_THREE_b, self.TWO_THREE_FOUR_s,
                                       self.TWO_THREE_FOUR_b, self.FIVE_SIX_SEVEN_s, self.FIVE_SIX_SEVEN_b,
                                       self.SIX_SEVEN_EIGHT_s, self.SIX_SEVEN_EIGHT_b, self.SEVEN_EIGHT_NINE_s,
                                       self.SEVEN_EIGHT_NINE_b, self.EIGHT_NINE_TEN_s, self.EIGHT_NINE_TEN_b]

        #   绞牌
        self.jiao_1_s = ['1b\x00', '1s\x00', '1s\x00']
        self.jiao_1_b = ['1b\x00', '1b\x00', '1s\x00']
        self.jiao_2_s = ['2b\x00', '2s\x00', '2s\x00']
        self.jiao_2_b = ['2b\x00', '2b\x00', '2s\x00']
        self.jiao_3_s = ['3b\x00', '3s\x00', '3s\x00']
        self.jiao_3_b = ['3b\x00', '3b\x00', '3s\x00']
        self.jiao_4_s = ['4b\x00', '4s\x00', '4s\x00']
        self.jiao_4_b = ['4b\x00', '4b\x00', '4s\x00']
        self.jiao_5_s = ['5b\x00', '5s\x00', '5s\x00']
        self.jiao_5_b = ['5b\x00', '5b\x00', '5s\x00']
        self.jiao_6_s = ['6b\x00', '6s\x00', '6s\x00']
        self.jiao_6_b = ['6b\x00', '6b\x00', '6s\x00']
        self.jiao_7_s = ['7b\x00', '7s\x00', '7s\x00']
        self.jiao_7_b = ['7b\x00', '7b\x00', '7s\x00']
        self.jiao_8_s = ['8b\x00', '8s\x00', '8s\x00']
        self.jiao_8_b = ['8b\x00', '8b\x00', '8s\x00']
        self.jiao_9_s = ['9b\x00', '9s\x00', '9s\x00']
        self.jiao_9_b = ['9b\x00', '9b\x00', '9s\x00']
        self.jiao_T_s = ['Tb\x00', 'Ts\x00', 'Ts\x00']
        self.jiao_T_b = ['Tb\x00', 'Tb\x00', 'Ts\x00']

        # 绞牌
        self.jiao_pai_list = [self.jiao_1_s, self.jiao_1_b, self.jiao_2_s, self.jiao_2_b, self.jiao_3_s, self.jiao_3_b,
                              self.jiao_4_s, self.jiao_4_b, self.jiao_5_s, self.jiao_5_b, self.jiao_6_s, self.jiao_6_b,
                              self.jiao_7_s, self.jiao_7_b, self.jiao_8_s, self.jiao_8_b, self.jiao_9_s, self.jiao_9_b,
                              self.jiao_T_s, self.jiao_T_b]

        # 含有红字的绞牌
        self.jiao_had_red_list = [self.jiao_2_s, self.jiao_2_b, self.jiao_7_s, self.jiao_7_b, self.jiao_T_s,
                                  self.jiao_T_b]

        # 歪胡子连牌
        self.One_Two_s = ['1s\x00', '2s\x00']
        self.One_Two_b = ['1b\x00', '2b\x00']

        self.One_Three_s = ['1s\x00', '3s\x00']
        self.One_Three_b = ['1b\x00', '3b\x00']

        self.Two_Three_s = ['2s\x00', '3s\x00']
        self.Two_Three_b = ['2b\x00', '3b\x00']

        self.Two_Four_s = ['2s\x00', '4s\x00']
        self.Two_Four_b = ['2b\x00', '4b\x00']

        self.Two_Seven_s = ['2s\x00', '7s\x00']
        self.Two_Seven_b = ['2b\x00', '7b\x00']

        self.Two_Ten_s = ['2s\x00', 'Ts\x00']
        self.Two_Ten_b = ['2b\x00', 'Tb\x00']

        self.Seven_Ten_s = ['7s\x00', 'Ts\x00']
        self.Seven_Ten_b = ['7b\x00', 'Tb\x00']

        self.Three_Four_s = ['3s\x00', '4s\x00']
        self.Three_Four_b = ['3b\x00', '4b\x00']

        self.Three_Five_s = ['3s\x00', '5s\x00']
        self.Three_Five_b = ['3b\x00', '5b\x00']

        self.Four_Five_s = ['4s\x00', '5s\x00']
        self.Four_Five_b = ['4b\x00', '5b\x00']

        self.Four_Six_s = ['4s\x00', '6s\x00']
        self.Four_Six_b = ['4b\x00', '6b\x00']

        self.Five_Six_s = ['5s\x00', '6s\x00']
        self.Five_Six_b = ['5b\x00', '6b\x00']

        self.Five_Seven_s = ['5s\x00', '7s\x00']
        self.Five_Seven_b = ['5b\x00', '7b\x00']

        self.Six_Seven_s = ['6s\x00', '7s\x00']
        self.Six_Seven_b = ['6b\x00', '7b\x00']

        self.Six_Eight_s = ['6s\x00', '8s\x00']
        self.Six_Eight_b = ['6b\x00', '8b\x00']

        self.Seven_Eight_s = ['7s\x00', '8s\x00']
        self.Seven_Eight_b = ['7b\x00', '8b\x00']

        self.Seven_Nine_s = ['7s\x00', '9s\x00']
        self.Seven_Nine_b = ['7b\x00', '9b\x00']

        self.Eight_Nine_s = ['8s\x00', '9s\x00']
        self.Eight_Nine_b = ['8b\x00', '9b\x00']

        self.Eight_Ten_s = ['8s\x00', 'Ts\x00']
        self.Eight_Ten_b = ['8b\x00', 'Tb\x00']

        self.Nine_Ten_s = ['9s\x00', 'Ts\x00']
        self.Nine_Ten_b = ['9b\x00', 'Tb\x00']

        #   散牌
        self.One = ['1s\x00', '1b\x00']
        self.Two = ['2s\x00', '2b\x00']
        self.Three = ['3s\x00', '3b\x00']
        self.Four = ['4s\x00', '4b\x00']
        self.Five = ['5s\x00', '5b\x00']
        self.Six = ['6s\x00', '6b\x00']
        self.Seven = ['7s\x00', '7b\x00']
        self.Eight = ['8s\x00', '8b\x00']
        self.Nine = ['9s\x00', '9b\x00']
        self.Ten = ['Ts\x00', 'Tb\x00']

        #   歪胡子123用于印
        self.waihuzi_yin_cards_123 = [self.ONE_TOW_THREE_s, self.ONE_TOW_THREE_b]

        #   歪胡子有胡息的连牌
        self.WaiHuZi_had_xi_lian_cards = [self.Two_Seven_s, self.Two_Seven_b, self.Two_Ten_s, self.Two_Ten_b,
                                          self.Seven_Ten_s, self.Seven_Ten_b]

        #   歪胡子单个红字的
        self.WaiHuZi_only_one_red_card_list = [self.One_Two_s, self.One_Two_b, self.ONE_TOW_THREE_s,
                                               self.ONE_TOW_THREE_b, self.Two_Three_s, self.Two_Three_b,
                                               self.Two_Four_s, self.Two_Four_b, self.TWO_THREE_FOUR_s,
                                               self.TWO_THREE_FOUR_b, self.FIVE_SIX_SEVEN_s, self.FIVE_SIX_SEVEN_b,
                                               self.Five_Seven_s, self.Five_Seven_b,
                                               self.Six_Seven_s, self.Six_Seven_b, self.SIX_SEVEN_EIGHT_s,
                                               self.SIX_SEVEN_EIGHT_b, self.Seven_Eight_s, self.Seven_Eight_b,
                                               self.Seven_Nine_s, self.Seven_Nine_b, self.SEVEN_EIGHT_NINE_s,
                                               self.SEVEN_EIGHT_NINE_b, self.EIGHT_NINE_TEN_s, self.EIGHT_NINE_TEN_b,
                                               self.Eight_Ten_s, self.Eight_Ten_s, self.Nine_Ten_s, self.Nine_Ten_b]
        #   歪胡子两个红字的
        self.waihuzi_two_red_card_list = [self.Two_Seven_s, self.Two_Seven_b, self.Two_Ten_s, self.Two_Ten_b,
                                          self.Seven_Ten_s, self.Seven_Ten_b]

        #   歪胡子两字连牌
        self.waihuzi_two_len_card_list = [self.One_Two_s, self.One_Two_b, self.One_Three_s, self.One_Three_b,
                                          self.Two_Three_s, self.Two_Three_b, self.Two_Four_s, self.Two_Four_b,

                                          self.Three_Four_s, self.Three_Four_b, self.Three_Five_s, self.Three_Five_b,
                                          self.Four_Five_s, self.Four_Five_b, self.Four_Six_s, self.Four_Six_b,
                                          self.Five_Six_s, self.Five_Six_b, self.Five_Seven_s, self.Five_Seven_b,
                                          self.Six_Seven_s, self.Six_Seven_b, self.Six_Eight_s, self.Six_Eight_b,
                                          self.Seven_Eight_s, self.Seven_Eight_b, self.Seven_Nine_s, self.Seven_Nine_b,
                                          self.Eight_Nine_s, self.Eight_Nine_b, self.Eight_Ten_s, self.Eight_Ten_b,
                                          self.Nine_Ten_s, self.Nine_Ten_b, self.Two_Seven_s, self.Two_Seven_b,
                                          self.Two_Ten_s, self.Two_Ten_b, self.Seven_Ten_s, self.Seven_Ten_b, ]

        #   散牌集合
        self.wai_scattered_cards_list = [self.One, self.Two, self.Three, self.Four, self.Five, self.Six, self.Seven,
                                         self.Eight, self.Nine, self.Ten]

        #   无红字三字连牌
        self.wai_had_no_red_cards_list = [self.THREE_FOUR_FIVE_s, self.THREE_FOUR_FIVE_b, self.FOUR_FIVE_SIX_s,
                                          self.FOUR_FIVE_SIX_b]








class RoomInfo:
    def __init__(self):
        self.ShaoYangZiPai = 1  # 邵阳字牌
        self.ShaoYangBoPi = 2  # 邵阳剥皮
        self.LouDi = 3  # 娄底放罚炮
        self.ChangDe = 4  # 常德跑胡子
        self.HengYang6 = 5  # 衡阳六抢胡
        self.ChangSha = 6  # 长沙跑胡子
        self.XiangXiang = 7  # 湘乡告胡子
        self.YongZhou = 8  # 永州扯胡子
        self.HuaiHua = 9  # 怀化红拐弯
        self.ChenZhou = 10  # 郴州
        self.YouXian = 11  # 攸县
        self.YongFeng = 14  # 永丰跑胡子
        self.HengYang10 = 18  # 衡阳十胡卡
        self.HongGuaiWan468 = 19  # 四六八红拐弯
        self.YiYang = 20  # 益阳
        self.QiDong15 = 21  # 祁东十五胡
        self.YueYang = 23  # 岳阳玩法


#   操作及胡息概况
class OperateInfo:
    def __init__(self):
        self.Chi = 1
        self.Peng = 2
        self.Pao = 3
        self.Wei = 6
        self.NotUsed = 7  # 谁都不要的牌
        self.Ti = 8
        self.Hu = 9
        self.Guo = 10
        self.Chu = 11
        self.ChouWei = 16  # 臭偎
        self.Zhuang = 17  # 给庄家的牌
        self.Wai = 18  # 歪
        self.Liu = 19  # 溜
        self.Wai2Liu = 20  # 歪到溜
        self.Kan2Liu = 31  # 坎变溜

    def get_Liu_huxi(self):
        return 5

    def get_Wai_huxi(self):
        return 4

    def get_WaiKan_huxi(self):
        return 3

    def get_WaiPeng_huxi(self):
        return 1

    def get_WaiLian_huxi(self):
        return 1

    #   获取碰牌胡息
    def get_Peng_huxi(self, cards):
        #   获取大小字
        charBuffer = cards[1][1:2]
        if charBuffer is 's':
            #   小字胡息1息
            return 1
        else:
            #   大字胡息3息
            return 3

    #   获取偎牌胡息
    def get_Wei_huxi(self, cards):
        charBuffer = cards[1][1:2]
        if charBuffer is 's':
            #   小字胡息3息
            return 3
        else:
            #   大字胡息6息
            return 6

    #   获取提牌胡息
    def get_Ti_huxi(self, cards):
        charBuffer = cards[1][1:2]
        if charBuffer is 's':
            #   小字胡息9息
            return 9
        else:
            #   大字胡息12息
            return 12

    #   获取跑牌胡息
    def get_Pao_huxi(self, cards):
        charBuffer = cards[1][1:2]
        if charBuffer is 's':
            #   小字胡息6息
            return 6
        else:
            #   大字胡息9息
            return 9

    #   获取坎牌胡息
    def get_Kan_huxi(self, cards):
        charBuffer = cards[1][1:2]
        if charBuffer is 's':
            #   小字胡息3息
            return 3
        else:
            #   大字胡息6息
            return 6

    #   获取连牌胡息
    def get_Lian_huxi(self, cards):
        #   判断是否为绞牌
        isJiao = False
        check_data = []
        for i in cards:
            check_data.append(i[:1])
        #   绞牌为三个数字相同的牌组成
        count = check_data.count(check_data[0])
        if count == 3:
            isJiao = True
        else:
            isJiao = False

        #   绞牌无息，直接返回0
        if isJiao:
            return 0, 'JIAO'

        info = LianPaiInfo()
        hadXi = False
        #   判断连牌是否有息
        for i in info.had_xi_lian_cards:
            if set(cards).issubset(set(i)):
                hadXi = True
        #   牌型为有息时
        if hadXi:
            #   有息时计算胡息
            charBuffer = cards[1][1:2]
            if charBuffer is 's':
                #   小字胡息3息
                return 3, 'LIAN'
            else:
                #   大字胡息6息
                return 6, 'LIAN'
        #   牌型无息返回0
        else:
            return 0, 'LIAN'
