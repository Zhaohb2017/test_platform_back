#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@ author: Hubery
@ create on: 2018/10/9 17:08
@ file: behavior.py
@ site:
@ purpose: 用户所有行为接口
"""
import json
import requests
from .config import *
from .connect import *
from .utils import *
from .protocol import *
from .unpack import *
from .cards import *

InsignificantProtocolList = [1017,      # SERVER_BROADCAST_REWARD
                             1086,      # SERVER__UPDATE_GOLD
                             10080,     # GMAE_SERVER_SWITCH_TO_MATCH_SERVER
                             9999,      # SERVER_VERSION_MESSAGE
                             1087,      # 推送钻石
                             1088,      # NOTIFY_RETURN_GOLD
                             1003,      # 服务器返回的桌子快照数据
                             1004,      # 服务器广播玩家进入信息
                             1006,      # 服务器广播玩家重连
                             1032,      # 发送玩家桌面数据
                             1034,      # 服务器广播玩家手上的牌数
                             1023,      # 服务器广播玩家出牌
                             1033,      # 服务器广播玩家摸牌
                             ]

class UserBehavior(object):
    def __init__(self, account, isHomeOwner=False):
        self.account = account
        self.sesskey = None
        self.game_type = 0

        # self.sesskey = sesskey  # 外部传入外网
        # self.sid = sid  # 各个线程sid

        self.SetGameType = None
        self.conn = None
        self.user_mid = None
        self.user_gp = None
        self.room_id = 0
        self.seat_id = 0
        self.logined = False
        self.last_room_id = 0
        self.homeowner = isHomeOwner
        self.record_init_card_state = False     # 初始计算牌长度时房主多一张
        self.hand_cards = []
        self.dun_cards_num = None
        self.room_type = None
        self.last_push_card = ""                # 上一轮出的牌
        self.CanOperate = False
        self.game_start = False
        self.player_num = 0
        self.touch_card = None
        self.create_room_code = None
        self.now_round_over = False
        self.banker = 0
        self.baocards = []
        self.cur_operations = []  # 玩家当前可以进行的操作集合。操作 100:出牌 101:碰牌操作 102:杠牌操作 103:胡牌操作 104:取消操作 105:摸牌操作 106:吃牌操作 107:补张操作
        self.cur_operation_id = 0  # 玩家当前进行的操作id
        self.case_operations = []  # 根据用例配置预定义的操作

        self.dissolve_state = False  # 解散状态
        self.BasicTask()

    def BasicTask(self):
        # self.GetUserSesskey()
        # self.LoadUserInfo()
        # self.ConnectGameServer()
        # 临时指定测试账号直接登录游戏服
        if self.account == 58950:
            self.user_mid = 58950
            self.user_gp = 101
        elif self.account == 58951:
            self.user_mid = 58951
            self.user_gp = 101
        elif self.account == 58952:
            self.user_mid = 58952
            self.user_gp = 101
        elif self.account == 58953:
            self.user_mid = 58953
            self.user_gp = 101
        self.ConnectGameServer()

    def GetUserSesskey(self):
        getSessKeyData = {'method': 'Amember.login', 'sitemid': self.account, 'site': SERVER_CONFIG['site_id'],
                          'channel': SERVER_CONFIG['channel_id'], 'gp': SERVER_CONFIG['gp_id'], 'pass': ''}
        try:
            content = requests.get(bread_base_url + json.dumps(getSessKeyData))
            self.sesskey = json.loads(content.text)['data']['sesskey']
            if self.sesskey is None:
                print("get sesskey is error.")
        except Exception as e:
            print("GetUserSesskey", e)

    def LoadUserInfo(self):
        getUserData = {'method': 'Amember.load', 'sesskey': self.sesskey}
        try:
            content = requests.get(bread_base_url + json.dumps(getUserData))
            user_data = json.loads(content.text)
            self.user_mid, self.user_gp = user_data['data']['aUser']['mid'], user_data['data']['aUser']['gp']
            if self.user_mid is None or self.user_gp is None:
                print("load user info is error by mid or gp is none.")
        except Exception as e:
            print("LoadUserInfo", e)

    def ConnectGameServer(self):
        self.conn = Connecter(SERVER_CONFIG['server_ip'], SERVER_CONFIG['server_port'], self.ProtocolDataProcess,
                              self.ConnectSuccessCallBack)
        self.conn.async_connect()

    def ConnectSuccessCallBack(self):
        self.Login(self.user_mid, self.user_gp, self.game_type)

    def ConnectClose(self):
        self.conn.connection_close()
        self.conn.close_loop()

    def SendDataToServer(self, data):
        self.conn.send_protocol(data)

    def ProtocolDataProcess(self, protocolNum, data):
        print("收到数据 protocolNum[{0}] data[{1}]".format(protocolNum, data))
        if protocolNum in InsignificantProtocolList:
            return
        if protocolNum == 1026 and not self.game_start:
            return
        # 处理包体数据，拿到明文数据，传递给各回包函数中处理
        if protocolNum not in ProtocolClassify.protocol_corresponding_function:
            print("收到未知协议号[{0}], data：{1}".format(protocolNum, data))
            return
        data_list = ProtocolClassify.protocol_corresponding_function[protocolNum]
        protocol_entity, funcName = data_list[0], data_list[1]
        real_data = UnPackData().unpack_data(protocolNum, protocol_entity, data)
        class_method = self.__class__.__dict__.get(funcName)
        #   协议处理
        if class_method:
            # 未登录状态在game server中执行登录前置要求
            class_method(self, real_data)
        else:
            print(self.user_mid, "本类中不存在 <{0}> 方法, 协议号: <1>".format(funcName, protocolNum))

    ###############################################################################
    ##   below are all of server interfaces
    ##   On: represents return
    ###############################################################################
    def Login(self, mid, gp, game_type):
        update_data = {"mid": mid, "no_used": "", "gp": gp, 'game_type': game_type}
        cs_login_data = CSLogin(update_data)
        self.SendDataToServer(cs_login_data.real_data)

    def OnLogin(self, data):
        if data['err'][1] is not 0:
            print("玩家: {0} 登录失败, 错误码: {1}".format(self.user_mid, data['error_code'][1]))
            self.ConnectClose()
            return
        else:
            self.logined = True
            print("玩家: {0} 登录成功.".format(self.user_mid))

    def OnReconnect(self, data):
        if data['room_id'][1] != 0:
            self.last_room_id = data['room_id'][1]
            # if self.last_room_id != 0:
            #     self.ApplyEnterRoom(self.last_room_id)
            print("玩家: {0} 断线重连成功, 并且在房间中, 房间号是: {1}".format(self.user_mid, data['room_id'][1]))
        else:
            print("玩家: {0} 断线重连成功, 不在房间中。".format(self.user_mid))  # 玩家未准备退出后服务器不发roomid？
        #   因断线重连会取消准备，所以补发准备动作（在此不区分是否在房中）。
        self.ReadyGame()


    def CheckIn(self):
        time.sleep(2)
        if self.homeowner and self.last_room_id != 0:
            #   房主选择提出解散房间
            print("房主{0}还在房间中，解散房间".format(self.user_mid))
            self.DissolveRoom()
        while self.last_room_id != 0:
            print("玩家{0}还在房间中，等待房间解散...".format(self.user_mid))
            time.sleep(0.5)

    def CreateRoom(self, update_data):
        self.CheckIn()
        time.sleep(1)
        create_room_data = RoomDataReplace(self.SetGameType, update_data)
        # create_room_data['gameClubId'] = 6721121
        # create_room_data['gameClubName'] = "自动化测试"
        cs_create_room_data = CSCreateRoom(create_room_data)
        # cs_create_room_data = CSCreateRoom(update_data)
        self.SendDataToServer(cs_create_room_data.real_data)

    def OnCreateRoom(self, data):
        self.create_room_code = data['err'][1]
        if self.create_room_code >= 0:
            self.room_id = data["roomid"][1]
            print("玩家: {0} 创建< {1} >房间成功. roomid：{2}".format(self.user_mid, self.room_type, self.room_id))
            # self.OnInformEnterRoom(self, data)
        else:
            if data['err'][1] == -1101:
                print("创建房间失败，金币不足")
            elif data['err'][1] == -1105:
                print("创建房间失败，已经在房间中")
            else:
                print("OnCreateRoom 创建房间失败: %s" % data)
            self.DissolveRoom()

    def ApplyEnterRoom(self, room_id, club_id=0):
        update_data = {"room_id": room_id, "version": 0, "ip": 0, "password": 0, "source": 0, "club_pay": 0}
        cs_enter_room_data = CSRequestEnterRoom(update_data)
        self.SendDataToServer(cs_enter_room_data.real_data)

    def OnInformEnterRoom(self, data):
        if data['seat_no'][1] > 0:
            self.seat_id = data['seat_no'][1]
            self.room_id = data['scene_id'][1]
            if self.homeowner:
                print("房间通知： 玩家: {0} 进入房间，房间号是: {1}, 座位号是: {2}".format(self.user_mid, self.room_id, self.seat_id))
            else:
                print("房间通知： 玩家: {0} 进入房间，座位号是: {1}".format(self.user_mid, self.seat_id))
            #   准备游戏
            self.ReadyGame()
        else:
            if data['seat_no'][1] == 1102:
                print("进入房间失败。房间未找到")
            else:
                print("进入房间失败。OnInformEnterRoom： %s" % data)

    # 服务器返回的房间快照数据
    def sc_room_snapshot(self, data):
        print("服务器返回的房间快照数据： %s" % data)
        return
        json_str = data['json_str'][1]
        json_str = '{0}{1}{2}'.format("'", json_str.strip(), "'")
        roominfojson = json.loads(json_str)
        self.room_id = roominfojson["room"]
        print("room_id:%s" % self.room_id)

    # 服务器返回的桌子快照数据
    def sc_desktop_snapshot(self, data):
        print("服务器返回的桌子快照数据： %s" % data)

    # 玩家发起解散
    def DissolveRoom(self):
        cs_dissolve_room_data = CSDissolveRoom({})
        self.SendDataToServer(cs_dissolve_room_data.real_data)
        print(" 玩家: {0} 发起解散房间申请.".format(self.user_mid))

    # 玩家收到发起解散消息
    def OnInformDissolveRoom(self, data):
        if not self.homeowner:
            self.ToVoteDissolveRoom()

    def ToVoteDissolveRoom(self, opinion=1):
        print("玩家: {0} 进行解散投票：{1}.".format(self.user_mid, opinion))
        update_data = {"opinion": opinion}
        cs_vote_dissolve_room_data = CSChoseDissolveRoom(update_data)
        self.SendDataToServer(cs_vote_dissolve_room_data.real_data)

    def OnVoteDissolveRoom(self, data):
        print("房间通知： 玩家: {0} 投票成功.".format(self.user_mid))

    # 玩家收到解散消息
    def OnVoteDissolveRoomEnd(self, data):
        print("房间通知：游戏解散。玩家[{0}] seat_id[{1}] room_id[{2}] data:{3}".
              format(self.user_mid, self.seat_id, self.room_id, data))
        self.dissolve_state = 1
        self.last_room_id = self.room_id
        self.room_id = 0
        self.game_start = 0
        self.game_type = 0
        self.cur_operation_id = 0
        self.seat_id = 0
        self.hand_cards = []
        self.banker = 0
        self.homeowner = 0
        self.CanOperate = []
        self.baocards = []
        self.cur_operations = []
        self.dun_cards_num = 0

    def ApplyLeaveRoom(self):
        cs_leave_room_data = CSLeaveRoom()
        self.SendDataToServer(cs_leave_room_data.real_data)

    def OnLeaveRoom(self, data):
        if data['mid'][1] == self.user_mid:
            if data['error_code'][1] == -17:
                self.last_room_id = 0
                self.dissolve_state = True  # 解散状态
                print("房间通知： 玩家: {0} 通过解散房间离开.".format(data['mid'][1]))
            else:
                print("房间通知： 玩家: {0} 打完牌局后离开房间.".format(data['mid'][1]))

    def ReadyGame(self):
        cs_request_ready_data = CSRequestReady()
        self.SendDataToServer(cs_request_ready_data.real_data)

    def OnReadyGame(self, data):
        if data['seat_no'][1] == self.seat_id:
            print("房间通知： {0} 号玩家: {1} 准备游戏.".format(self.seat_id, self.user_mid))

    def OnGameStart(self, data):
        self.game_start = True
        self.banker = data['banker_seatno'][1]
        print("房间通知： 开始游戏（玩家{0}）。  庄家：{1} .".format(self.seat_id, self.banker))

    def OnInformLessMode(self, data):
        print("房間通知：少人模式返回參數: %s" % data['RoomInfo'])

    def ApplyOpenLessMode(self):
        cs_request_ready_data = CSOpenLessMode()
        self.SendDataToServer(cs_request_ready_data.real_data)

    def OnOpenLessMode(self, data):
        if data['ErrorCode'] == 0:
            print("房间通知： 少人模式开启成功, 参数如下: %s" % data)

    def MakeCards(self, update_data):
        real_data = {"cards_list": ""}
        for k, v in update_data.items():
            real_data["cards_list"] += v

        if len(list(real_data["cards_list"].replace(",", ""))) is not 160:
            return
        cs_cards_type = CSMakeCardsType(real_data)
        self.SendDataToServer(cs_cards_type.real_data)

    def OnMakeCards(self, data):
        if data['error_code'][1] is not 0:
            print("--------------> 做牌失败, 联系开发人员.")
            return
        else:
            print("--------------> 做牌成功.")
        print()

    # 服务器发牌
    def OnRecvCards(self, data):
        self.hand_cards = data["card_lists"][1]
        print("发牌。玩家[{0}]手牌：{1}".format(self.seat_id, self.hand_cards))

    # 服务器广播宝牌
    def OnRecvBaoCards(self, data):
        self.baocards = data["bao_cards"][1]
        print("服务器广播宝牌。宝牌[{0}] 数量[{1}]".format(self.baocards, data["count"][1]))

    # 玩家摸牌
    def OnTouchCard(self, data):
        self.dun_cards_num = data['dun_count'][1]  # 牌蹲上剩余的牌数
        card = data['card'][1]  # 摸的那张牌
        seat_no = data['seat_no'][1]  # 摸牌的位置
        if self.seat_id != seat_no:
            print("房间通知摸牌， 但摸牌座位号: %s,与当前玩家座位号不一致 %s ." % (seat_no, self.seat_id))
            return
        print("房间通知: 当前摸牌玩家: %s, 座位号: %s, 摸到的牌: %s, 当前牌墩上还剩余 %s 张牌." % (
            self.user_mid, seat_no, card, self.dun_cards_num))
        self.touch_card = card
        self.hand_cards.append(card)

    def OnPlayerCanDo(self, data):
        if data['seat_no'][1] == self.seat_id:
            self.cur_operation_id = data['operation_id'][1]
            self.CanOperate = True
            self.cur_operations = []
            # 操作 100:出牌操作 101:碰牌操作 102:杠牌操作 103:胡牌操作 104:取消操作 105:摸牌操作 106:吃牌操作 107:补张操作
            for op in data['opeate'][1]:
                if op == 100:
                    self.cur_operations.append("出牌")
                elif op == 101:
                    self.cur_operations.append("碰")
                elif op == 102:
                    self.cur_operations.append("杠")
                elif op == 103:
                    self.cur_operations.append("胡")
                elif op == 104:
                    self.cur_operations.append("取消")
                elif op == 105:
                    self.cur_operations.append("摸牌")
                elif op == 106:
                    self.cur_operations.append("吃")
                elif op == 107:
                    self.cur_operations.append("补张")
                else:
                    self.cur_operations.append(op)
            print("玩家: %s, 座位号: %s, operation_id:%s, 当前可进行的操作有: %s" % (self.user_mid, self.seat_id,
                                                                       self.cur_operation_id, self.cur_operations))
            #  test start
            if self.cur_operations:
                self.ToPlayOperation(self.cur_operations[0], self.cur_operation_id, self.last_push_card)
                return
            #  test end
            if len(self.case_operations) > 0:
                caseop = self.case_operations.pop()
            else:
                caseop = None
            if caseop is None:
                if len(self.hand_cards) > 0:
                    card = self.hand_cards.pop()
                    print("玩家: %s, 座位号: %s, 用例未配置操作，选择出牌：%s" % (self.user_mid, self.seat_id, card))
                    self.PlayerOutCard({"card": card, "operation_id": self.cur_operation_id})
            else:
                print("玩家: %s, 座位号: %s, 根据用例配置选择的操作是: %s" % (self.user_mid, self.seat_id, caseop))
                self.ToPlayOperation(caseop, self.cur_operation_id, self.last_push_card)

    # 跳转到打牌动作对应方法
    def ToPlayOperation(self, operation, operation_id, card):
        if len(card) > 0:
            update_data = {"operation_id": operation_id, "card": card}
        else:
            update_data = {"operation_id": operation_id}
        if operation == "出牌":
            self.PlayerOutCard(update_data)
        elif operation == "碰":
            self.PlayerPengCard(update_data)
        elif operation == "杠":
            self.PlayerGangCard(update_data)
        elif operation == "胡":
            self.PlayerHuCard(update_data)
        elif operation == "取消":
            self.PlayerCancel(update_data)
        elif operation == "摸牌":
            self.OnTouchCard(update_data)
        elif operation == "吃":
            self.PlayerChiCard(update_data)
        elif operation == "补张":
            self.OnTouchCard(update_data)
        else:
            print("GetPlayOperation 玩家{0} 未知打牌动作：{1}".format(self.seat_id, operation))

    # 玩家出牌
    def PlayerOutCard(self, update_data):
        print("玩家{0} 座位号{1} 出牌。update_data：{2}".format(self.user_mid, self.seat_id, update_data))
        cs_request_function_data = CSClientPlayReq(update_data)
        self.SendDataToServer(cs_request_function_data.real_data)

    # 玩家吃牌
    def PlayerChiCard(self, update_data):
        print("玩家{0} 座位号{1} 吃牌。update_data：{2}".format(self.user_mid, self.seat_id, update_data))
        cs_request_function_data = CSClientChiReq(update_data)
        self.SendDataToServer(cs_request_function_data.real_data)

    # 玩家碰牌
    def PlayerPengCard(self, update_data):
        print("玩家{0} 座位号{1}碰牌。update_data：{2}".format(self.user_mid, self.seat_id, update_data))
        cs_request_function_data = CSClientPengReq(update_data)
        self.SendDataToServer(cs_request_function_data.real_data)

    # 玩家杠牌
    def PlayerGangCard(self, update_data):
        print("玩家{0} 座位号{1}杠牌。update_data：{2}".format(self.user_mid, self.seat_id, update_data))
        cs_request_function_data = CSClientGangReq(update_data)
        self.SendDataToServer(cs_request_function_data.real_data)

    # 玩家取消操作
    def PlayerCancel(self, update_data):
        print("玩家{0} 座位号{1}取消操作。update_data：{2}".format(self.user_mid, self.seat_id, update_data))
        cs_request_function_data = CSClientCancelReq(update_data)
        self.SendDataToServer(cs_request_function_data.real_data)

    # 玩家胡牌
    def PlayerHuCard(self, update_data):
        print("玩家{0} 座位号{1}胡牌。update_data：{2}".format(self.user_mid, self.seat_id, update_data))
        cs_request_function_data = CSClientHuReq(update_data)
        self.SendDataToServer(cs_request_function_data.real_data)

    def ReplaceMingTang(self, data):
        switcher = {
            1: "自摸",
            2: "红胡",
            3: "黑胡",
            4: "天胡",
            5: "地胡",
            6: "一点红",
            7: "一块匾",
            8: "卡胡",
            9: "海底胡",
            10: "大胡",
            11: "小胡",
            12: "红乌",
            13: "对字胡",
            14: "耍猴",
            15: "黄番",
            16: "十红",
            17: "十八大",
            18: "十八小",
            19: "二比",
            20: "三比",
            21: "四比",
            22: "双飘",
            23: "十六小",
            24: "王钓",
            25: "30胡",
            26: "30胡(十红)）",
            27: "地胡（地到底）",
            28: "王钓王",
            29: "王闯",
            30: "放炮",
            31: "毛胡",
            32: "听胡",
            33: "中庄",
            34: "连庄",
            35: "五福",
            36: "跑双",
            37: "小七对",
            38: "双龙",
            39: "小卡胡",
            40: "大卡胡",
            41: "小红",
            42: "大红",
            43: "碰碰胡",
            44: "红胡王钓",
            45: "红胡王闯",
            46: "黑胡王钓",
            47: "黑胡王闯",
            48: "点胡王钓",
            49: "点胡王闯",
            50: "王炸",
            51: "王闯王",
            52: "王炸王",
            53: "红湖王钓王",
            54: "黑胡王钓王",
            55: "点胡王钓王",
            56: "红湖王炸王",
            57: "点胡王炸王",
            58: "黑胡王炸王",
            59: "红湖王闯王",
            60: "黑胡王闯王",
            61: "点胡王闯王",
            62: "红湖王炸",
            63: "黑胡王炸",
            64: "点胡王炸",
            65: "红转点",
            66: "红转黑",
            67: "红转点王钓",
            68: "红转点王闯",
            69: "红转点王炸",
            70: "红转点王钓王",
            71: "红转点王闯王",
            72: "红转点王炸王",
            73: "红转黑王钓",
            74: "红转黑王闯",
            75: "红转黑王炸",
            76: "红转黑王钓王",
            77: " 红转黑王闯王",
            78: "红转黑王炸王",
            79: "30胡（地到底）",
            80: "十红（地到底）",
            81: "飘胡",
            82: "大团圆",
            83: "行行息",
            84: "扎鸟",
            85: "自摸2番的显示",
            86: "黄番(显示 为  xx番)",
            87: "多红",
            88: "四七红",
            89: "假行行",
        }
        try:
            return switcher[data]
        except:
            print("错误通知：未找到对应匹配的名堂，名堂编码--> %s" % data)


    def ReplaceCardType(self, data):
        switcher = {
            0: "碰牌",
            1: "一句话",
            2: "特殊的一句话",
            3: "比牌",
            4: "特殊的比牌",
            5: "绞牌",
            6: "偎牌",
            7: "跑牌",
            8: "提牌",
            9: "一对",
            10: "一坎",
            11: "单牌",
            16: "臭偎"
        }
        try:
            return switcher[data]
        except:
            print("错误通知：未找到对应匹配的牌型，牌型编码--> %s" % data)

    # 服务器广播小结算
    def OnSettlement(self, data):
        if self.homeowner and self.game_start:
            self.now_round_over = True
            MingTangInfos = []
            if len(data['TypeInfo']) != 0:
                MingTangInfos = [(self.ReplaceMingTang(value['Type']), value['Score']) for key, value in data['TypeInfo'].items()]

            CardTypeInfos = []
            if len(data['CardTypeInfo']) != 0:
                CardTypeInfos = [(self.ReplaceCardType(value['CardType']), str(value['Huxi']) + "息", value['Cards']) for key, value in data['CardTypeInfo'].items()]

            print("小局结算通知: 房间ID: %s, 本局庄家座位号: %s, 赢家总胡息: %s, "  % (data['RoomID'], data['BankerSeatID'], data['TotalHuxi']))
            print("    ---> 赢家手牌信息: %s" % CardTypeInfos)
            print("    ---> 名堂信息: %s" % MingTangInfos)
            for key, value in data['OnlineInfo'].items():
                print("    ---> %s号玩家的手牌信息为: %s张, %s" % (value['SeatID'], value['CardNum'], value['Cards']))

            for key, value in data['TiInfo'].items():
                print("    ---> %s号玩家的提牌信息为: %s张, %s" % (value['SeatID'], value['Num'], value['Cards']))
            print()

        time.sleep(2)
        # self.ReadyGame()

    def OnTotalSettlement(self, data):
        pass

    def OnErrorTips(self, data):
        if data["error_code"][1] != 0:
            print("房间通知: 当前操作有误, 错误码是: < %s >, 说明 -7 为非法操作, 参数错误. -20为出牌失败,可能是当前出的牌不在手牌中." % data["error_code"][1])

    def OperateApi(self, option, last_card="", card_types=None):
        if option in ["跑", "提", "偎"]:
            print("此操作 <%s> 由服务器主动执行, 等待服务器执行中." % option)
            return
        while not self.CanOperate:
            time.sleep(0.5)

        self.CanOperate = False
        operate = GetOperateID(option)
        if card_types is None and option in [1, 11, 18, 19]:
            print("操作为 <吃、出、溜、歪> 时, 应提供出牌牌型.")
            return

        if operate in [1, 11, 18, 19]:
            operate_data = None
            if operate == 1:
                operate_card = self.GetCardsStruct(card_types)
                for card in operate_card:
                    if last_card in card:
                        operate_card.remove(card)
                        break

                operate_data = {"function_type": operate, "card_num": len(operate_card), "_card": operate_card,
                                "function_index": self.serial}

            elif operate == 11:
                operate_card = card_types[0]
                operate_data = {"function_type": operate, "card_num": len(card_types), "_card": operate_card,
                                "function_index": self.serial}

            elif operate == 18:
                pass

            elif operate == 19:
                pass

            else:
                print("玩家通知: 操作为 %s 的接口有误." % operate)
            self.serial = None
            self.PlayerOperates(operate_data)

        elif operate in [2, 9, 10]:
            operate_data = {"function_type": operate, "card_num": 0, "function_index": self.serial}
            self.serial = None
            self.PlayerOperates(operate_data)


    def GetCardsStruct(self, card_data):
        operate_card = []
        for _type in card_data:
            card_list = _type.split(",")
            for i in card_list:
                operate_card.append(i + "\x00")

        return operate_card

    def DelHandCards(self, operate, tips_cards):
        print(self.user_mid, "删除手牌操作是: %s, 要删的牌是: %s" % (operate, tips_cards))
        #   跑牌, 不需要删
        if operate is 3:
            print(self.user_mid, "跑牌操作,无需删除手牌...")

        #   偎牌或者臭偎
        elif operate is 6 or operate is 16:
            del_index = 0
            for i in tips_cards:
                if i in self.hand_cards:
                    if del_index < 2:
                        self.hand_cards.remove(i)
                        del_index += 1
                    else:
                        break
            print(self.user_mid, "偎牌操作,删除2张...")

        #   提牌， 删除4张
        elif operate is 8:
            for i in tips_cards:
                if i in self.hand_cards:
                    self.hand_cards.remove(i)
            print(self.user_mid, "起手提操作,删除4张...")

        # 如果是溜，删4张
        if operate is 19:
            for i in tips_cards:
                if i in self.hand_cards:
                    self.hand_cards.remove(i)
            print(self.user_mid, "起手溜操作,删除4张...")

        # 如果是歪, 删2张
        elif operate is 18:
            del_index = 0
            for i in tips_cards:
                if i in self.hand_cards:
                    if del_index < 2:
                        self.hand_cards.remove(i)
                        del_index += 1
                    else:
                        break
            print(self.user_mid, "歪牌操作,删除2张...")

        # 如果是歪变溜,不用删
        elif operate is 20:
            if self.room_type is RoomInfo().YiYang:
                for i in tips_cards:
                    if i in self.hand_cards:
                        self.hand_cards.remove(i)
                print(self.user_mid, "歪溜删牌4张， 删掉的牌是: %s" % tips_cards)
            else:
                print(self.user_mid, "歪溜无需删牌...")

        # 如果是坎变溜,删3张
        elif operate is 31:
            del_index = 0
            for i in tips_cards:
                if i in self.hand_cards:
                    if del_index < 3:
                        self.hand_cards.remove(i)
                        del_index += 1
                    else:
                        break
            print(self.user_mid, "坎溜操作，删除3张...")

        # 如果是碰,删掉两张
        elif operate is 2:
            del_index = 0
            for i in tips_cards:
                if i in self.hand_cards:
                    if del_index < 2:
                        self.hand_cards.remove(i)
                        del_index += 1
                    else:
                        break
            print(self.user_mid, "碰牌操作,删除2张...")

        # 如果是吃
        elif operate is 1:
            for i in tips_cards:
                if i in self.hand_cards and i != self.last_push_card:
                    self.hand_cards.remove(i)

            print(self.user_mid, "吃牌操作,删除2张...%s" % tips_cards)

        # 如果是出
        elif operate is 11:
            self.hand_cards.remove(tips_cards[0])
            print(self.user_mid, "出牌操作,删除1张...%s" % tips_cards[0])
        elif operate is 7:
            print(self.user_mid, "无人要的牌，已经在出牌的时候提前打了...")
        elif operate is -7:
            print(self.user_mid, "非法操作....")
        elif operate is -20:
            print(self.user_mid, "无法出牌...")
        elif operate is 9:
            print(self.user_mid, "胡牌操作，无需删除手牌...")
        else:
            print(self.user_mid, "尚未添加的操作是: %s" % operate)
