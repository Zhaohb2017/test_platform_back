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
import logging
from runner.chaoyue.master.phz.config import *
from runner.chaoyue.master.phz.connect import *
from runner.chaoyue.master.phz.utils import *
from runner.chaoyue.master.phz.unpack import *
from runner.chaoyue.master.phz.cards import *


def helper_print(account, function_name, protocol_number, data, print_state=False):
    if print_state:
        print("account: %s, protocol_number: %s, %s :" % (
            account, protocol_number, time.strftime("%Y-%m-%d %X", time.localtime())))
        print("%s: %s" % (function_name, data))
        # print()


class UserBehavior(object):
    def __init__(self, mid, isHomeOwner=False, different="local"):
        # if type(mid) is str:
        #     self.user_mid = int(mid)  # 用户编号
        # elif type(mid) is int:
        self.user_mid = mid
        self.touch_card = ''
        self.sc_club_game_list_data = {}
        self.account = None
        self.different = different
        self.ip = "192.168.1.153"
        self.port = 9007
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
        self.dissolve_state = False  # 解散状态

        self.sesskey = None  # 登录唯一标识
        self.user_gp = None  # 用户组
        self.room_id = None  # 创建房间得到的房间ID
        self.user_clubID = None  # 俱乐部ID
        self.conn = None  # 连接器对象
        self.user_current_gold = None  # 用户当前金币数量
        self.last_room_id = None  # 断线重连之前的房间ID
        self.current_fun_index = None  # 操作序列号
        self.can_do_data = None  # 可以做什么操作的数据
        self.current_fun_data = None  # 当前操作返回的结果，包括胡息,座位号,牌内容
        self.total_hu_xi = None  # 总胡息
        self.total_7_men_zi = None  # 七方门子总数
        self.molding_card_list = []  # 已出牌牌型
        self.hand_cards_list = None  # 手牌
        self.logined = False  # 是否登录
        self.isEnterRoom = False  # 是否进入房间了
        self.seat_id = None  # 座位号
        self.get_room_state = False  # 获取房间快照信息
        self.dissolve_room_state = False  # 解散房间标志
        self.isNotMyPart = False  # 广播消息不接收非自身信息
        self.game_start_state = False  # 游戏开始标志
        self.game_over = False  # 小局结束
        self.current_rounds = False  # 判定是谁操作的轮次
        self.in_the_room = False  # 不在房间中
        self.isAgree = False  # 设置解散房间同意状态
        self.last_push_card = None  # 上个玩家出的牌
        self.remain_card = None  # 荒牌状态

        self.reconnect_status = False  # 重连状态
        self.sc_now_operation_player = None  # 当前操作用户
        self.room_dissolve_status = False  # 解散房间状态

        self.join_house_status = False  # 加入房间状态
        self.create_room_join_room_status = False  # 创建房间进入房间状态
        self.operation_sign = None  # 操作码
        self.operation_chu_data = {}  # 出牌数据
        self.operation_guo_data = {}  # 过牌数据
        self.peng_card = None  # 碰牌数据
        self.operation_hu_data = {}  # 胡牌数据
        self.player_broadcast_ti = {}  # 玩家自动提牌数据
        self.player_broadcast_wei = {}  # 玩家自动偎牌数据
        self.player_broadcast_pao = {}  # 玩家自动跑牌数据
        self.player_broadcast_peng = {}  # 玩家自动碰牌数据
        self.small_settle_accounts_data = {}  # 小局结算数据
        self.total_settlement_data = {}  # 大局结算数据
        self.end_hu_card_data = {}  # 最后胡牌
        self.departure_room_data = {}  # 离开房间返回数据
        self.is_join_hand_card = None  # 加入手牌
        self.mo_card = None  # 摸牌
        self.chi_card = None  # 吃的牌
        self.player_hand_cards = []  # 玩家手上的牌
        self.phz_login()  #调登录

    # #   注册用户
    # def phz_get_sseskey(self):
    #     get_sesskey_data = {'method': 'Amember.login', 'sitemid': self.account, 'site': self.confData['site_id'],
    #                         'channel': self.confData['channel_id'], 'gp': self.confData['gp_id'], 'pass': ''}
    #
    #     try:
    #         #   请求访问
    #         url = None
    #         if self.different == "local":
    #             if self.versions == "master":
    #                 url = self.confData['php_base_url_master']
    #             elif self.versions == "ChangSha":
    #                 url = self.confData['php_base_url_changsha']
    #             else:
    #                 url = self.confData['php_base_url_changde']
    #         else:
    #             if self.different == "test":
    #                 if self.versions == "master":
    #                     url = self.confData['test_php_base_url_master']
    #                 elif self.versions == "ChangSha":
    #                     url = self.confData['test_php_base_url_changsha']
    #                 else:
    #                     url = self.confData['test_php_base_url_changde']
    #
    #         call_get_sesskey_data = requests.get(url + json.dumps(get_sesskey_data))
    #         if call_get_sesskey_data.status_code != 200:
    #             raise Exception ("PHP connection fail")
    #         self.sesskey = json.loads(call_get_sesskey_data.text)['data']['sesskey']
    #
    #         if self.sesskey is None:
    #             raise Exception("get sesskey error...")
    #     except Exception as e:
    #         raise e
    #
    # #   加载用户信息
    # def phz_load_user_info(self):
    #     if self.sesskey is None:
    #         return
    #     #	获取用户数据
    #     get_user_data = {'method': 'Amember.load', 'sesskey': self.sesskey}
    #     try:
    #         #   请求访问
    #         url = None
    #         if self.different == "local":
    #             if self.versions == "master":
    #                 url = self.confData['php_base_url_master']
    #             elif self.versions == "ChangSha":
    #                 url = self.confData['php_base_url_changsha']
    #             else:
    #                 url = self.confData['php_base_url_changde']
    #         else:
    #             if self.different == "test":
    #                 if self.versions == "master":
    #                     url = self.confData['test_php_base_url_master']
    #                 elif self.versions == "ChangSha":
    #                     url = self.confData['test_php_base_url_changsha']
    #                 else:
    #                     url = self.confData['test_php_base_url_changde']
    #
    #         call_get_user_data = requests.get(url + json.dumps(get_user_data))
    #         user_data = json.loads(call_get_user_data.text)
    #
    #         self.user_mid, self.user_gp = user_data['data']['aUser']['mid'], user_data['data']['aUser']['gp']
    #         print("玩家信息mid: %s" % self.user_mid)
    #
    #         if self.user_mid is None and self.user_gp is None:
    #             raise Exception("get user data error... user_mid: %s, user_gp: %s" % (self.user_mid, self.user_gp))
    #         return user_data['data']['aUser']['mid']
    #     except Exception as e:
    #         raise e
    #
    # #   获取用户俱乐部ID
    # def phz_get_user_clubId(self):
    #     url = self.confData['php_get_user_clubId'] % self.user_mid
    #     try:
    #         #	请求访问
    #         call_get_user_data = requests.get(url)
    #         user_gold_data = json.loads(call_get_user_data.text)
    #         if user_gold_data['svflag'] is 1:
    #             self.user_clubID = user_gold_data['data']
    #             return self.user_clubID
    #         else:
    #             return None
    #     except Exception as e:
    #         raise e
    #
    # #   查询用户当前金币数额
    # def phz_query_user_gold(self):
    #     url = self.confData['php_query_gold_url'] % self.user_mid
    #     try:
    #         #	请求访问
    #         call_get_user_data = requests.get(url)
    #         user_gold_data = json.loads(call_get_user_data.text)
    #         self.user_current_gold = user_gold_data['data']
    #         return self.user_current_gold
    #     except Exception as e:
    #         raise e
    #
    # #   修改用户金币数额
    # def phz_update_user_gold(self, user_mid, update_gold):
    #     url = self.confData['php_update_gold_url'] % (user_mid, update_gold)
    #     print("请求增加金币url:", url)
    #     try:
    #         #	请求访问
    #         call_get_user_data = requests.get(url)
    #         print("增加金币返回数据", call_get_user_data.text)
    #         # user_gold_data = json.loads(call_get_user_data.text)
    #         # self.user_current_gold = user_gold_data['data']
    #         # return self.user_current_gold
    #     except Exception as e:
    #         raise e
    #
    # #   获取代理商固定玩法和自动开房值
    # def phz_get_agent_wanfa_value(self):
    #     clubID = self.phz_get_user_clubId()
    #     if len(clubID) <= 0:
    #         return False
    #     #	获取用户数据
    #     clubplay = "3,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,%s,0,club,0,0,0" % clubID[0]
    #     agent_data = {"method": "Aactive.saveClubPlays",
    #                   "sesskey": self.sesskey, "clubid": clubID[0],
    #                   "clubplays": clubplay, "type": 0}
    #     try:
    #         #	请求访问
    #         call_get_user_data = requests.get(self.confData['php_cache_wanfa_url'] + json.dumps(agent_data))
    #         agent_data = json.loads(call_get_user_data.text)
    #         if agent_data['svflag'] == 1:
    #             return True
    #         else:
    #             return False
    #     except Exception as e:
    #         raise e

    #   登录
    def phz_login(self, _CONDICTION=None):
        # self.phz_get_sseskey()
        user_mid = self.phz_load_user_info()
        self.qs_connect()


    def qs_connect(self):
        print("socket_Connected is build...")
        print("connect ip is : %s, port: %s" % (self.ip, self.port))
        self.conn = Connecter(self.ip, self.port, self.ProtocolDataProcess, self.on_connect_server)
        self.conn.async_connect()

    #   连接成功回调
    def on_connect_server(self):
        print('socket_Connected is success..')
        print("-----------------------------------------------------")
        self.qs_login(self.user_mid, self.user_gp)

    #   发送数据到TCP服务器
    def SendDataToServer(self, data):
        self.conn.send_protocol(data)

    #   关闭连接
    def connect_close(self):
        self.conn.connection_close()
        loop_close()


    def ProtocolDataProcess(self, protocolNum, data):
        L = [1017, 1086, 10022, 10080, 10008]
        if protocolNum in L:
            return
        if protocolNum == 1026 and not self.game_start:
            return
        # 处理包体数据，拿到明文数据，传递给各回包函数中处理
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



    #   数据处理
    def qs_protocol(self, protocol_num, data):
        L = [1017, 1086, 10022, 10080, 10008]
        if protocol_num in L:
            return

        # 处理包体数据，拿到明文数据，传递给各回包函数中处理
        data_list = ProtocolClassify.protocol_corresponding_function[protocol_num]
        # print("qs_protocol_函数,",protocol_num)
        protocol_entity, funcName = data_list[0], data_list[1]
        real_data = None
        real_data = UnPackData().unpack_data(protocol_num, protocol_entity, data)
        #   如果当前解包数据是无的话，返回
        #         # if real_data is None:
        #                 #     return
        #   获取当前类的方法函数
        class_method = self.__class__.__dict__.get(funcName)
        #   协议处理
        if class_method:
            # 未登录状态在game server中执行登录前置要求
            class_method(self, funcName, protocol_num, real_data)
        else:
            pass
            # print("it has no function..")
    #   登录
    def qs_login(self, mid, gp):
        update_data = {"mid": mid, "gp": 101}
        print(update_data)
        cs_login_data = CSLogin(update_data)
        self.SendDataToServer(cs_login_data.real_data)

    #   登录回包
    def OnLogin(self,data):
        self.sc_login_data = data
        if data["error_code"][1] == 0:
            self.logined = True
        if not self.logined:
            return

    def OnReconnect(self, data):
        if data['room_id'][1] != 0:
            self.last_room_id = data['room_id'][1]
            # if self.last_room_id != 0:
            #     self.ApplyEnterRoom(self.last_room_id)
            logging.info("玩家: {0} 断线重连成功, 并且在房间中, 房间号是: {1}".format(self.user_mid, data['room_id'][1]))
            print("玩家: {0} 断线重连成功, 并且在房间中, 房间号是: {1}".format(self.user_mid, data['room_id'][1]))
        else:
            logging.info("玩家: {0} 断线重连成功, 不在房间中。".format(self.user_mid))
            print("玩家: {0} 断线重连成功, 不在房间中。".format(self.user_mid))

    def CheckIn(self):
        time.sleep(2)
        if self.homeowner and self.last_room_id != 0:
            #   房主选择提出解散房间
            self.DissolveRoom()

        while self.last_room_id != 0:
            time.sleep(0.5)

    def CreateRoom(self, update_data):
        # self.CheckIn()
        time.sleep(1)
        create_room_data = RoomDataReplace(self.SetGameType, update_data)
        # create_room_data['gameClubId'] = 6721121
        # create_room_data['gameClubName'] = "自动化测试"
        print("创房：",create_room_data)
        cs_create_room_data = CSCreateRoom(create_room_data)
        # cs_create_room_data = CSCreateRoom(update_data)
        self.SendDataToServer(cs_create_room_data.real_data)

    def CreateRoomLeiYang(self, update_data):
        create_room_data = RoomDataReplace(self.SetGameType, update_data)
        cs_create_room_leiyang_data = CSCreateRoomLeiYang(create_room_data)
        self.SendDataToServer(cs_create_room_leiyang_data.real_data)

    def OnCreateRoom(self, data):
        logging.info("OnCreateRoom: %s" % data)
        print("OnCreateRoom: %s" % data)
        self.create_room_code = data['error_code'][1]
        if data["error_code"][1] == 0:
            self.room_id = data["gameRoomId"][1]
            self.room_type = int(data['gameRoomType'][1][:len(data['gameRoomType'][1]) - 1])
            self.player_num = data["gamePlayer"][1]
            logging.info("玩家: {0} 创建< {1} >房间成功.".format(self.user_mid, GetGameType(self.room_type)))
            print("玩家: {0} 创建< {1} >房间成功.".format(self.user_mid, GetGameType(self.room_type)))

        elif data['error_code'][1] == -78:
            self.DissolveRoom()




    # 益阳创建房间
    def CreateRoomYiYang(self, update_data):
        create_room_data = RoomDataReplace(self.SetGameType, update_data)
        # create_room_data['gameClubId'] = 6721121
        # create_room_data['gameClubName'] = "自动化测试"
        # print(create_room_data)

        cs_create_room_yiyang_data = CSCreateRoomYiYang(data=create_room_data)
        self.SendDataToServer(cs_create_room_yiyang_data.real_data)

    # 益阳创建房间回包数据
    def OnCreateRoomYiYang(self, data):
        # print("OnCreateRoomYiYang", data)
        self.sc_create_room_yiyang_data = data
        #   创建房间成功
        if data["error_code"][1] == 0:
            self.room_id = data["gameRoomid"][1]
            self.room_type = int(data['gameRoomType'][1][:len(data['gameRoomType'][1]) - 1])
            self.jushu = data['gameJuShu'][1]
            logging.info("玩家: {0} 创建< {1} >房间成功.".format(self.user_mid, GetGameType(self.room_type)))
            print("玩家: {0} 创建< {1} >房间成功.".format(self.user_mid, GetGameType(self.room_type)))

    def ApplyEnterRoom(self, room_id, club_id=0):
        update_data = {"room_id": room_id, "join_room_type": 0}

        # print(update_data)
        cs_enter_room_data = CSRequestEnterRoom(update_data)
        self.SendDataToServer(cs_enter_room_data.real_data)

    def OnInformEnterRoom(self, data):
        # print("OnInformEnterRoom： %s" % data)
        if data['error_code'][1] is 0:
            self.seat_id = data['seat_id'][1]
            if self.homeowner:
                logging.info("房间通知： 玩家: {0} 进入房间，房间号是: {1}, 座位号是: {2}".format(self.user_mid, self.room_id, self.seat_id))
                print("房间通知： 玩家: {0} 进入房间，房间号是: {1}, 座位号是: {2}".format(self.user_mid, self.room_id, self.seat_id))
            else:
                logging.info("房间通知： 玩家: {0} 进入房间，座位号是: {1}".format(self.user_mid, self.seat_id))
                print("房间通知： 玩家: {0} 进入房间，座位号是: {1}".format(self.user_mid, self.seat_id))

            print()
            #   准备游戏
            self.ReadyGame()

    def DissolveRoom(self):
        cs_dissolve_room_data = CSDissolveRoom({})
        self.SendDataToServer(cs_dissolve_room_data.real_data)

    def OnInformDissolveRoom(self, data):
        if not self.homeowner:
            self.ToVoteDissolveRoom()

        # if data['mid'][1] != self.user_mid:
        #     #   同意解散
        #     self.ToVoteDissolveRoom()
        # else:
        logging.info("房间通知： 玩家: {0} 发起解散房间申请.".format(self.user_mid))
        print("房间通知： 玩家: {0} 发起解散房间申请.".format(self.user_mid))

    def ToVoteDissolveRoom(self, opinion=1):
        update_data = {"vote_opinion": opinion}
        cs_vote_dissolve_room_data = CSChoseDissolveRoom(update_data)
        self.SendDataToServer(cs_vote_dissolve_room_data.real_data)

    def OnVoteDissolveRoom(self, data):
        if data['mid'][1] != self.user_mid:
            logging.info("房间通知： 玩家: {0} 同意解散房间.".format(self.user_mid))
            print("房间通知： 玩家: {0} 同意解散房间.".format(self.user_mid))

    def ApplyLeaveRoom(self):
        cs_leave_room_data = CSLeaveRoom()
        self.SendDataToServer(cs_leave_room_data.real_data)

    def OnLeaveRoom(self, data):
        if data['mid'][1] == self.user_mid:
            if data['error_code'][1] == -17:
                self.last_room_id = 0
                self.dissolve_state = True  # 解散状态
                logging.info("房间通知： 玩家: {0} 通过解散房间离开.".format(data['mid'][1]))
                print("房间通知： 玩家: {0} 通过解散房间离开.".format(data['mid'][1]))
            else:
                logging.info("房间通知： 玩家: {0} 打完牌局后离开房间.".format(data['mid'][1]))
                print("房间通知： 玩家: {0} 打完牌局后离开房间.".format(data['mid'][1]))

    def ReadyGame(self):
        cs_request_ready_data = CSRequestReady()
        self.SendDataToServer(cs_request_ready_data.real_data)

    def OnReadyGame(self, data):
        if data['seat_id'][1] == self.seat_id:
            logging.info("房间通知： {0} 号玩家: {1} 准备游戏.".format(self.seat_id, self.user_mid))
            print("房间通知： {0} 号玩家: {1} 准备游戏.".format(self.seat_id, self.user_mid))

    def OnGameStart(self, data):
        self.game_start = True
        logging.info("房间通知： {0} 号玩家: {1} 开始游戏.".format(self.seat_id, self.user_mid))
        logging.info("房间通知： 庄家座位号: %s" % data['banker_seat_id'][1])
        print("房间通知： {0} 号玩家: {1} 开始游戏.".format(self.seat_id, self.user_mid))
        print("房间通知： 庄家座位号: %s" % data['banker_seat_id'][1])

    def OnInformLessMode(self, data):
        logging.info("房間通知：少人模式返回參數: %s" % data['RoomInfo'])
        print("房間通知：少人模式返回參數: %s" % data['RoomInfo'])

    def ApplyOpenLessMode(self):
        cs_request_ready_data = CSOpenLessMode()
        self.SendDataToServer(cs_request_ready_data.real_data)

    def OnOpenLessMode(self, data):
        if data['ErrorCode'] == 0:
            logging.info("房间通知： 少人模式开启成功, 参数如下: %s" % data)
            print("房间通知： 少人模式开启成功, 参数如下: %s" % data)

    def MakeCards(self, update_data):
        real_data = {"cards_list": ""}
        for data in update_data:
            for cards in data:
                for card in cards:
                    real_data["cards_list"] += card

        print("real_data： %s" % real_data)
        # for k, v in update_data.items():
        #     real_data["cards_list"] += v

        if len(list(real_data["cards_list"].replace(",", ""))) is not 160:
            return
        cs_cards_type = CSMakeCardsType(real_data)
        self.SendDataToServer(cs_cards_type.real_data)

    def OnMakeCards(self, data):
        if data['error_code'][1] is not 0:
            logging.info("--------------> 做牌失败, 联系开发人员.")
            print("--------------> 做牌失败, 联系开发人员.")
            return
        else:
            logging.info("--------------> 做牌成功.")
            print("--------------> 做牌成功.")

        print()

    def OnRecvCards(self, data):
        #   初始手牌
        self.hand_cards = data["card_lists"][1]

    def OnTouchCard(self, data):
        self.dun_cards_num = data['remain_card'][1]
        if self.homeowner:
            logging.info("房间通知: 当前摸牌玩家: %s, 座位号: %s, 摸到的牌: %s, 当前牌墩上还剩余 %s 张牌." % (
                self.user_mid, data['seat_id'][1], data['touch_card'][1], data['remain_card'][1]))
            print("房间通知: 当前摸牌玩家: %s, 座位号: %s, 摸到的牌: %s, 当前牌墩上还剩余 %s 张牌." % (
                self.user_mid, data['seat_id'][1], data['touch_card'][1], data['remain_card'][1]))

            print()
            self.touch_card = data['touch_card'][1]

        if data['seat_id'][1] == self.seat_id:
            if data['remain_card'][1] is 19:
                self.hand_cards.append(data['touch_card'][1])

    def OnPlayerCanDo(self, data):
        self.serial = (data['fun_index'][1])[:len(data['fun_index'][1]) - 1]
        if data['seat_id'][1] == self.seat_id:
            self.CanOperate = True
            AllOperate = []
            if self.room_type is RoomInfo().YiYang:
                if data['is_LiuPai'][1] is 1:
                    AllOperate.append("溜")
                if data['is_waiPai'][1] is 1:
                    AllOperate.append("歪")

            if data['is_chi_card'][1] is 1:
                self.last_push_card = data['last_push_card'][1]
                AllOperate.append("吃")
            if data['is_hu_card'][1] is 1:
                AllOperate.append("胡")
            if data['is_peng_card'][1] is 1:
                AllOperate.append("碰")
            if data['is_chu_card'][1] is 1:
                AllOperate.append("出")

            logging.info("玩家: %s, 座位号: %s, 当前可进行的操作有: %s" % (self.user_mid, self.seat_id, AllOperate))
            print("玩家: %s, 座位号: %s, 当前可进行的操作有: %s" % (self.user_mid, self.seat_id, AllOperate))
            print()
            if "胡" in AllOperate:
                self.PlayerOperates({"function_type": 9, "card_num": 0, "function_index": self.serial})

    def PlayerOperates(self, update_data):
        cs_request_function_data = CSRequestFunction(update_data)
        self.SendDataToServer(cs_request_function_data.real_data)

    def OnPlayerOperate(self, data):
        if data["error_code"][1] == -7 and data['seat_id'][1] == -100:
            logging.info("房间通知: 出牌操作失败, 当前操作为非法操作. 联系开发或李佳.\n")
            print("房间通知: 出牌操作失败, 当前操作为非法操作. 联系开发或李佳.\n")
            return

        if data["error_code"][1] == -20 and data['seat_id'][1] == -100:
            logging.info("房间通知: 出牌操作失败, 可能是当前手牌中没有此牌.\n")
            print("房间通知: 出牌操作失败, 可能是当前手牌中没有此牌.\n")
            return

        if data["seat_id"][1] == self.seat_id:
            if data['do_function'][1] != 9:
                if data['do_function'][1] == 7:
                    logging.info("房间通知: 玩家: %s, 座位号: %s, < %s >, 牌型是: %s" % (
                        self.user_mid, self.seat_id, GetOperateCH(data['do_function'][1]), data['_card'][1]))
                    print("房间通知: 玩家: %s, 座位号: %s, < %s >, 牌型是: %s" % (
                        self.user_mid, self.seat_id, GetOperateCH(data['do_function'][1]), data['_card'][1]))
                else:
                    logging.info("房间通知: 玩家: %s, 座位号: %s, < %s >牌成功, 牌型是: %s" % (
                        self.user_mid, self.seat_id, GetOperateCH(data['do_function'][1]), data['_card'][1]))
                    print("房间通知: 玩家: %s, 座位号: %s, < %s >牌成功, 牌型是: %s" % (
                        self.user_mid, self.seat_id, GetOperateCH(data['do_function'][1]), data['_card'][1]))
            else:
                logging.info("房间通知: 玩家: %s, 座位号: %s, < %s >牌成功." % (
                    self.user_mid, self.seat_id, GetOperateCH(data['do_function'][1])))
                print("房间通知: 玩家: %s, 座位号: %s, < %s >牌成功." % (
                    self.user_mid, self.seat_id, GetOperateCH(data['do_function'][1])))

            print()

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
            logging.info("错误通知：未找到对应匹配的名堂，名堂编码--> %s" % data)
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
            logging.info("错误通知：未找到对应匹配的牌型，牌型编码--> %s" % data)
            print("错误通知：未找到对应匹配的牌型，牌型编码--> %s" % data)

    def OnSettlement(self, data):
        if self.homeowner and self.game_start:
            self.now_round_over = True
            MingTangInfos = []
            if len(data['TypeInfo']) != 0:
                MingTangInfos = [(self.ReplaceMingTang(value['Type']), value['Score']) for key, value in data['TypeInfo'].items()]

            CardTypeInfos = []
            if len(data['CardTypeInfo']) != 0:
                CardTypeInfos = [(self.ReplaceCardType(value['CardType']), str(value['Huxi']) + "息", value['Cards']) for key, value in data['CardTypeInfo'].items()]

            logging.info("小局结算通知: 房间ID: %s, 本局庄家座位号: %s, 赢家总胡息: %s, "  % (data['RoomID'], data['BankerSeatID'], data['TotalHuxi']))
            logging.info("    ---> 赢家手牌信息: %s" % CardTypeInfos)
            logging.info("    ---> 名堂信息: %s" % MingTangInfos)
            print("小局结算通知: 房间ID: %s, 本局庄家座位号: %s, 赢家总胡息: %s, "  % (data['RoomID'], data['BankerSeatID'], data['TotalHuxi']))
            print("    ---> 赢家手牌信息: %s" % CardTypeInfos)
            print("    ---> 名堂信息: %s" % MingTangInfos)
            for key, value in data['OnlineInfo'].items():
                logging.info("    ---> %s号玩家的手牌信息为: %s张, %s" % (value['SeatID'], value['CardNum'], value['Cards']))
                print("    ---> %s号玩家的手牌信息为: %s张, %s" % (value['SeatID'], value['CardNum'], value['Cards']))

            for key, value in data['TiInfo'].items():
                logging.info("    ---> %s号玩家的提牌信息为: %s张, %s" % (value['SeatID'], value['Num'], value['Cards']))
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








# InsignificantProtocolList = [1017, 1086, 10022, 10080, 10008]
#
# class UserBehavior(object):
#     def __init__(self, account, isHomeOwner=False):
#         self.account = account
#         self.sesskey = None
#
#         # self.sesskey = sesskey  # 外部传入外网
#         # self.sid = sid  # 各个线程sid
#
#         self.SetGameType = None
#         self.conn = None
#         self.user_mid = None
#         self.user_gp = None
#         self.room_id = 0
#         self.seat_id = 0
#         self.logined = False
#         self.last_room_id = 0
#         self.homeowner = isHomeOwner
#         self.record_init_card_state = False     # 初始计算牌长度时房主多一张
#         self.hand_cards = []
#         self.dun_cards_num = None
#         self.room_type = None
#         self.last_push_card = ""                # 上一轮出的牌
#         self.CanOperate = False
#         self.game_start = False
#         self.player_num = 0
#         self.touch_card = None
#         self.create_room_code = None
#         self.now_round_over = False
#
#         self.dissolve_state = False  # 解散状态
#         self.BasicTask()
#
#     def BasicTask(self):
#         self.GetUserSesskey()
#         self.LoadUserInfo()
#         self.ConnectGameServer()
#
#     def GetUserSesskey(self):
#         getSessKeyData = {'method': 'Amember.login', 'sitemid': self.account, 'site': SERVER_CONFIG['site_id'],
#                           'channel': SERVER_CONFIG['channel_id'], 'gp': SERVER_CONFIG['gp_id'], 'pass': ''}
#
#         try:
#             content = requests.get(bread_base_url + json.dumps(getSessKeyData))
#             self.sesskey = json.loads(content.text)['data']['sesskey']
#             if self.sesskey is None:
#                 print("get sesskey is error.")
#         except Exception as e:
#             print("GetUserSesskey", e)
#
#     def LoadUserInfo(self):
#         getUserData = {'method': 'Amember.load', 'sesskey': self.sesskey}
#         try:
#             content = requests.get(bread_base_url + json.dumps(getUserData))
#             user_data = json.loads(content.text)
#             self.user_mid, self.user_gp = user_data['data']['aUser']['mid'], user_data['data']['aUser']['gp']
#             if self.user_mid is None or self.user_gp is None:
#                 print("load user info is error by mid or gp is none.")
#         except Exception as e:
#             print("LoadUserInfo", e)
#
#     def ConnectGameServer(self):
#         self.conn = Connecter(SERVER_CONFIG['server_ip'], SERVER_CONFIG['server_port'], self.ProtocolDataProcess,
#                               self.ConnectSuccessCallBack)
#         self.conn.async_connect()
#
#     def ConnectSuccessCallBack(self):
#         self.Login(self.user_mid, self.user_gp, self.sesskey)
#
#     def ConnectClose(self):
#         self.conn.connection_close()
#         self.conn.close_loop()
#
#     def SendDataToServer(self, data):
#         self.conn.send_protocol(data)
#
#     def ProtocolDataProcess(self, protocolNum, data):
#         if protocolNum in InsignificantProtocolList:
#             return
#         if protocolNum == 1026 and not self.game_start:
#             return
#         # 处理包体数据，拿到明文数据，传递给各回包函数中处理
#         data_list = ProtocolClassify.protocol_corresponding_function[protocolNum]
#         protocol_entity, funcName = data_list[0], data_list[1]
#         real_data = UnPackData().unpack_data(protocolNum, protocol_entity, data)
#         class_method = self.__class__.__dict__.get(funcName)
#         #   协议处理
#         if class_method:
#             # 未登录状态在game server中执行登录前置要求
#             class_method(self, real_data)
#         else:
#             print(self.user_mid, "本类中不存在 <{0}> 方法, 协议号: <1>".format(funcName, protocolNum))
#
#     ###############################################################################
#     ##   below are all of server interfaces
#     ##   On: represents return
#     ###############################################################################
#     def Login(self, mid, gp, sesskey):
#         update_data = {"mid": mid, "gp": gp, 'sesskey': sesskey}
#         cs_login_data = CSLogin(update_data)
#         self.SendDataToServer(cs_login_data.real_data)
#
#     def OnLogin(self, data):
#         if data['error_code'][1] is not 0 and data['error_code'][1] != 3:
#             print("玩家: {0} 登录失败, 错误码: {1}".format(self.user_mid, data['error_code'][1]))
#             self.ConnectClose()
#             return
#         else:
#             self.logined = True
#             logging.info("玩家: {0} 登录成功.".format(self.user_mid))
#             print("玩家: {0} 登录成功.".format(self.user_mid))
#
#     def OnReconnect(self, data):
#         if data['room_id'][1] != 0:
#             self.last_room_id = data['room_id'][1]
#             # if self.last_room_id != 0:
#             #     self.ApplyEnterRoom(self.last_room_id)
#             logging.info("玩家: {0} 断线重连成功, 并且在房间中, 房间号是: {1}".format(self.user_mid, data['room_id'][1]))
#             print("玩家: {0} 断线重连成功, 并且在房间中, 房间号是: {1}".format(self.user_mid, data['room_id'][1]))
#         else:
#             logging.info("玩家: {0} 断线重连成功, 不在房间中。".format(self.user_mid))
#             print("玩家: {0} 断线重连成功, 不在房间中。".format(self.user_mid))
#
#     def CheckIn(self):
#         time.sleep(2)
#         if self.homeowner and self.last_room_id != 0:
#             #   房主选择提出解散房间
#             self.DissolveRoom()
#
#         while self.last_room_id != 0:
#             time.sleep(0.5)
#
#     def CreateRoom(self, update_data):
#         self.CheckIn()
#         time.sleep(1)
#         create_room_data = RoomDataReplace(self.SetGameType, update_data)
#         # create_room_data['gameClubId'] = 6721121
#         # create_room_data['gameClubName'] = "自动化测试"
#         cs_create_room_data = CSCreateRoom(create_room_data)
#         # cs_create_room_data = CSCreateRoom(update_data)
#         self.SendDataToServer(cs_create_room_data.real_data)
#
#     def CreateRoomLeiYang(self, update_data):
#         create_room_data = RoomDataReplace(self.SetGameType, update_data)
#         cs_create_room_leiyang_data = CSCreateRoomLeiYang(create_room_data)
#         self.SendDataToServer(cs_create_room_leiyang_data.real_data)
#
#     def OnCreateRoom(self, data):
#         logging.info("OnCreateRoom: %s" % data)
#         print("OnCreateRoom: %s" % data)
#         self.create_room_code = data['error_code'][1]
#         if data["error_code"][1] == 0:
#             self.room_id = data["gameRoomId"][1]
#             self.room_type = int(data['gameRoomType'][1][:len(data['gameRoomType'][1]) - 1])
#             self.player_num = data["gamePlayer"][1]
#             logging.info("玩家: {0} 创建< {1} >房间成功.".format(self.user_mid, GetGameType(self.room_type)))
#             print("玩家: {0} 创建< {1} >房间成功.".format(self.user_mid, GetGameType(self.room_type)))
#
#         elif data['error_code'][1] == -78:
#             self.DissolveRoom()
#
#
#
#
#     # 益阳创建房间
#     def CreateRoomYiYang(self, update_data):
#         create_room_data = RoomDataReplace(self.SetGameType, update_data)
#         # create_room_data['gameClubId'] = 6721121
#         # create_room_data['gameClubName'] = "自动化测试"
#         # print(create_room_data)
#
#         cs_create_room_yiyang_data = CSCreateRoomYiYang(data=create_room_data)
#         self.SendDataToServer(cs_create_room_yiyang_data.real_data)
#
#     # 益阳创建房间回包数据
#     def OnCreateRoomYiYang(self, data):
#         # print("OnCreateRoomYiYang", data)
#         self.sc_create_room_yiyang_data = data
#         #   创建房间成功
#         if data["error_code"][1] == 0:
#             self.room_id = data["gameRoomid"][1]
#             self.room_type = int(data['gameRoomType'][1][:len(data['gameRoomType'][1]) - 1])
#             self.jushu = data['gameJuShu'][1]
#             logging.info("玩家: {0} 创建< {1} >房间成功.".format(self.user_mid, GetGameType(self.room_type)))
#             print("玩家: {0} 创建< {1} >房间成功.".format(self.user_mid, GetGameType(self.room_type)))
#
#     def ApplyEnterRoom(self, room_id, club_id=0):
#         update_data = {"room_id": room_id, "join_room_type": 0}
#
#         # print(update_data)
#         cs_enter_room_data = CSRequestEnterRoom(update_data)
#         self.SendDataToServer(cs_enter_room_data.real_data)
#
#     def OnInformEnterRoom(self, data):
#         # print("OnInformEnterRoom： %s" % data)
#         if data['error_code'][1] is 0:
#             self.seat_id = data['seat_id'][1]
#             if self.homeowner:
#                 logging.info("房间通知： 玩家: {0} 进入房间，房间号是: {1}, 座位号是: {2}".format(self.user_mid, self.room_id, self.seat_id))
#                 print("房间通知： 玩家: {0} 进入房间，房间号是: {1}, 座位号是: {2}".format(self.user_mid, self.room_id, self.seat_id))
#             else:
#                 logging.info("房间通知： 玩家: {0} 进入房间，座位号是: {1}".format(self.user_mid, self.seat_id))
#                 print("房间通知： 玩家: {0} 进入房间，座位号是: {1}".format(self.user_mid, self.seat_id))
#
#             print()
#             #   准备游戏
#             self.ReadyGame()
#
#     def DissolveRoom(self):
#         cs_dissolve_room_data = CSDissolveRoom({})
#         self.SendDataToServer(cs_dissolve_room_data.real_data)
#
#     def OnInformDissolveRoom(self, data):
#         if not self.homeowner:
#             self.ToVoteDissolveRoom()
#
#         # if data['mid'][1] != self.user_mid:
#         #     #   同意解散
#         #     self.ToVoteDissolveRoom()
#         # else:
#         logging.info("房间通知： 玩家: {0} 发起解散房间申请.".format(self.user_mid))
#         print("房间通知： 玩家: {0} 发起解散房间申请.".format(self.user_mid))
#
#     def ToVoteDissolveRoom(self, opinion=1):
#         update_data = {"vote_opinion": opinion}
#         cs_vote_dissolve_room_data = CSChoseDissolveRoom(update_data)
#         self.SendDataToServer(cs_vote_dissolve_room_data.real_data)
#
#     def OnVoteDissolveRoom(self, data):
#         if data['mid'][1] != self.user_mid:
#             logging.info("房间通知： 玩家: {0} 同意解散房间.".format(self.user_mid))
#             print("房间通知： 玩家: {0} 同意解散房间.".format(self.user_mid))
#
#     def ApplyLeaveRoom(self):
#         cs_leave_room_data = CSLeaveRoom()
#         self.SendDataToServer(cs_leave_room_data.real_data)
#
#     def OnLeaveRoom(self, data):
#         if data['mid'][1] == self.user_mid:
#             if data['error_code'][1] == -17:
#                 self.last_room_id = 0
#                 self.dissolve_state = True  # 解散状态
#                 logging.info("房间通知： 玩家: {0} 通过解散房间离开.".format(data['mid'][1]))
#                 print("房间通知： 玩家: {0} 通过解散房间离开.".format(data['mid'][1]))
#             else:
#                 logging.info("房间通知： 玩家: {0} 打完牌局后离开房间.".format(data['mid'][1]))
#                 print("房间通知： 玩家: {0} 打完牌局后离开房间.".format(data['mid'][1]))
#
#     def ReadyGame(self):
#         cs_request_ready_data = CSRequestReady()
#         self.SendDataToServer(cs_request_ready_data.real_data)
#
#     def OnReadyGame(self, data):
#         if data['seat_id'][1] == self.seat_id:
#             logging.info("房间通知： {0} 号玩家: {1} 准备游戏.".format(self.seat_id, self.user_mid))
#             print("房间通知： {0} 号玩家: {1} 准备游戏.".format(self.seat_id, self.user_mid))
#
#     def OnGameStart(self, data):
#         self.game_start = True
#         logging.info("房间通知： {0} 号玩家: {1} 开始游戏.".format(self.seat_id, self.user_mid))
#         logging.info("房间通知： 庄家座位号: %s" % data['banker_seat_id'][1])
#         print("房间通知： {0} 号玩家: {1} 开始游戏.".format(self.seat_id, self.user_mid))
#         print("房间通知： 庄家座位号: %s" % data['banker_seat_id'][1])
#
#     def OnInformLessMode(self, data):
#         logging.info("房間通知：少人模式返回參數: %s" % data['RoomInfo'])
#         print("房間通知：少人模式返回參數: %s" % data['RoomInfo'])
#
#     def ApplyOpenLessMode(self):
#         cs_request_ready_data = CSOpenLessMode()
#         self.SendDataToServer(cs_request_ready_data.real_data)
#
#     def OnOpenLessMode(self, data):
#         if data['ErrorCode'] == 0:
#             logging.info("房间通知： 少人模式开启成功, 参数如下: %s" % data)
#             print("房间通知： 少人模式开启成功, 参数如下: %s" % data)
#
#     def MakeCards(self, update_data):
#         real_data = {"cards_list": ""}
#         for data in update_data:
#             for cards in data:
#                 for card in cards:
#                     real_data["cards_list"] += card
#
#         print("real_data： %s" % real_data)
#         # for k, v in update_data.items():
#         #     real_data["cards_list"] += v
#
#         if len(list(real_data["cards_list"].replace(",", ""))) is not 160:
#             return
#         cs_cards_type = CSMakeCardsType(real_data)
#         self.SendDataToServer(cs_cards_type.real_data)
#
#     def OnMakeCards(self, data):
#         if data['error_code'][1] is not 0:
#             logging.info("--------------> 做牌失败, 联系开发人员.")
#             print("--------------> 做牌失败, 联系开发人员.")
#             return
#         else:
#             logging.info("--------------> 做牌成功.")
#             print("--------------> 做牌成功.")
#
#         print()
#
#     def OnRecvCards(self, data):
#         #   初始手牌
#         self.hand_cards = data["card_lists"][1]
#
#     def OnTouchCard(self, data):
#         self.dun_cards_num = data['remain_card'][1]
#         if self.homeowner:
#             logging.info("房间通知: 当前摸牌玩家: %s, 座位号: %s, 摸到的牌: %s, 当前牌墩上还剩余 %s 张牌." % (
#                 self.user_mid, data['seat_id'][1], data['touch_card'][1], data['remain_card'][1]))
#             print("房间通知: 当前摸牌玩家: %s, 座位号: %s, 摸到的牌: %s, 当前牌墩上还剩余 %s 张牌." % (
#                 self.user_mid, data['seat_id'][1], data['touch_card'][1], data['remain_card'][1]))
#
#             print()
#             self.touch_card = data['touch_card'][1]
#
#         if data['seat_id'][1] == self.seat_id:
#             if data['remain_card'][1] is 19:
#                 self.hand_cards.append(data['touch_card'][1])
#
#     def OnPlayerCanDo(self, data):
#         self.serial = (data['fun_index'][1])[:len(data['fun_index'][1]) - 1]
#         if data['seat_id'][1] == self.seat_id:
#             self.CanOperate = True
#             AllOperate = []
#             if self.room_type is RoomInfo().YiYang:
#                 if data['is_LiuPai'][1] is 1:
#                     AllOperate.append("溜")
#                 if data['is_waiPai'][1] is 1:
#                     AllOperate.append("歪")
#
#             if data['is_chi_card'][1] is 1:
#                 self.last_push_card = data['last_push_card'][1]
#                 AllOperate.append("吃")
#             if data['is_hu_card'][1] is 1:
#                 AllOperate.append("胡")
#             if data['is_peng_card'][1] is 1:
#                 AllOperate.append("碰")
#             if data['is_chu_card'][1] is 1:
#                 AllOperate.append("出")
#
#             logging.info("玩家: %s, 座位号: %s, 当前可进行的操作有: %s" % (self.user_mid, self.seat_id, AllOperate))
#             print("玩家: %s, 座位号: %s, 当前可进行的操作有: %s" % (self.user_mid, self.seat_id, AllOperate))
#             print()
#             if "胡" in AllOperate:
#                 self.PlayerOperates({"function_type": 9, "card_num": 0, "function_index": self.serial})
#
#     def PlayerOperates(self, update_data):
#         cs_request_function_data = CSRequestFunction(update_data)
#         self.SendDataToServer(cs_request_function_data.real_data)
#
#     def OnPlayerOperate(self, data):
#         if data["error_code"][1] == -7 and data['seat_id'][1] == -100:
#             logging.info("房间通知: 出牌操作失败, 当前操作为非法操作. 联系开发或李佳.\n")
#             print("房间通知: 出牌操作失败, 当前操作为非法操作. 联系开发或李佳.\n")
#             return
#
#         if data["error_code"][1] == -20 and data['seat_id'][1] == -100:
#             logging.info("房间通知: 出牌操作失败, 可能是当前手牌中没有此牌.\n")
#             print("房间通知: 出牌操作失败, 可能是当前手牌中没有此牌.\n")
#             return
#
#         if data["seat_id"][1] == self.seat_id:
#             if data['do_function'][1] != 9:
#                 if data['do_function'][1] == 7:
#                     logging.info("房间通知: 玩家: %s, 座位号: %s, < %s >, 牌型是: %s" % (
#                         self.user_mid, self.seat_id, GetOperateCH(data['do_function'][1]), data['_card'][1]))
#                     print("房间通知: 玩家: %s, 座位号: %s, < %s >, 牌型是: %s" % (
#                         self.user_mid, self.seat_id, GetOperateCH(data['do_function'][1]), data['_card'][1]))
#                 else:
#                     logging.info("房间通知: 玩家: %s, 座位号: %s, < %s >牌成功, 牌型是: %s" % (
#                         self.user_mid, self.seat_id, GetOperateCH(data['do_function'][1]), data['_card'][1]))
#                     print("房间通知: 玩家: %s, 座位号: %s, < %s >牌成功, 牌型是: %s" % (
#                         self.user_mid, self.seat_id, GetOperateCH(data['do_function'][1]), data['_card'][1]))
#             else:
#                 logging.info("房间通知: 玩家: %s, 座位号: %s, < %s >牌成功." % (
#                     self.user_mid, self.seat_id, GetOperateCH(data['do_function'][1])))
#                 print("房间通知: 玩家: %s, 座位号: %s, < %s >牌成功." % (
#                     self.user_mid, self.seat_id, GetOperateCH(data['do_function'][1])))
#
#             print()
#
#     def ReplaceMingTang(self, data):
#         switcher = {
#             1: "自摸",
#             2: "红胡",
#             3: "黑胡",
#             4: "天胡",
#             5: "地胡",
#             6: "一点红",
#             7: "一块匾",
#             8: "卡胡",
#             9: "海底胡",
#             10: "大胡",
#             11: "小胡",
#             12: "红乌",
#             13: "对字胡",
#             14: "耍猴",
#             15: "黄番",
#             16: "十红",
#             17: "十八大",
#             18: "十八小",
#             19: "二比",
#             20: "三比",
#             21: "四比",
#             22: "双飘",
#             23: "十六小",
#             24: "王钓",
#             25: "30胡",
#             26: "30胡(十红)）",
#             27: "地胡（地到底）",
#             28: "王钓王",
#             29: "王闯",
#             30: "放炮",
#             31: "毛胡",
#             32: "听胡",
#             33: "中庄",
#             34: "连庄",
#             35: "五福",
#             36: "跑双",
#             37: "小七对",
#             38: "双龙",
#             39: "小卡胡",
#             40: "大卡胡",
#             41: "小红",
#             42: "大红",
#             43: "碰碰胡",
#             44: "红胡王钓",
#             45: "红胡王闯",
#             46: "黑胡王钓",
#             47: "黑胡王闯",
#             48: "点胡王钓",
#             49: "点胡王闯",
#             50: "王炸",
#             51: "王闯王",
#             52: "王炸王",
#             53: "红湖王钓王",
#             54: "黑胡王钓王",
#             55: "点胡王钓王",
#             56: "红湖王炸王",
#             57: "点胡王炸王",
#             58: "黑胡王炸王",
#             59: "红湖王闯王",
#             60: "黑胡王闯王",
#             61: "点胡王闯王",
#             62: "红湖王炸",
#             63: "黑胡王炸",
#             64: "点胡王炸",
#             65: "红转点",
#             66: "红转黑",
#             67: "红转点王钓",
#             68: "红转点王闯",
#             69: "红转点王炸",
#             70: "红转点王钓王",
#             71: "红转点王闯王",
#             72: "红转点王炸王",
#             73: "红转黑王钓",
#             74: "红转黑王闯",
#             75: "红转黑王炸",
#             76: "红转黑王钓王",
#             77: " 红转黑王闯王",
#             78: "红转黑王炸王",
#             79: "30胡（地到底）",
#             80: "十红（地到底）",
#             81: "飘胡",
#             82: "大团圆",
#             83: "行行息",
#             84: "扎鸟",
#             85: "自摸2番的显示",
#             86: "黄番(显示 为  xx番)",
#             87: "多红",
#             88: "四七红",
#             89: "假行行",
#         }
#         try:
#             return switcher[data]
#         except:
#             logging.info("错误通知：未找到对应匹配的名堂，名堂编码--> %s" % data)
#             print("错误通知：未找到对应匹配的名堂，名堂编码--> %s" % data)
#
#
#     def ReplaceCardType(self, data):
#         switcher = {
#             0: "碰牌",
#             1: "一句话",
#             2: "特殊的一句话",
#             3: "比牌",
#             4: "特殊的比牌",
#             5: "绞牌",
#             6: "偎牌",
#             7: "跑牌",
#             8: "提牌",
#             9: "一对",
#             10: "一坎",
#             11: "单牌",
#             16: "臭偎"
#         }
#         try:
#             return switcher[data]
#         except:
#             logging.info("错误通知：未找到对应匹配的牌型，牌型编码--> %s" % data)
#             print("错误通知：未找到对应匹配的牌型，牌型编码--> %s" % data)
#
#     def OnSettlement(self, data):
#         if self.homeowner and self.game_start:
#             self.now_round_over = True
#             MingTangInfos = []
#             if len(data['TypeInfo']) != 0:
#                 MingTangInfos = [(self.ReplaceMingTang(value['Type']), value['Score']) for key, value in data['TypeInfo'].items()]
#
#             CardTypeInfos = []
#             if len(data['CardTypeInfo']) != 0:
#                 CardTypeInfos = [(self.ReplaceCardType(value['CardType']), str(value['Huxi']) + "息", value['Cards']) for key, value in data['CardTypeInfo'].items()]
#
#             logging.info("小局结算通知: 房间ID: %s, 本局庄家座位号: %s, 赢家总胡息: %s, "  % (data['RoomID'], data['BankerSeatID'], data['TotalHuxi']))
#             logging.info("    ---> 赢家手牌信息: %s" % CardTypeInfos)
#             logging.info("    ---> 名堂信息: %s" % MingTangInfos)
#             print("小局结算通知: 房间ID: %s, 本局庄家座位号: %s, 赢家总胡息: %s, "  % (data['RoomID'], data['BankerSeatID'], data['TotalHuxi']))
#             print("    ---> 赢家手牌信息: %s" % CardTypeInfos)
#             print("    ---> 名堂信息: %s" % MingTangInfos)
#             for key, value in data['OnlineInfo'].items():
#                 logging.info("    ---> %s号玩家的手牌信息为: %s张, %s" % (value['SeatID'], value['CardNum'], value['Cards']))
#                 print("    ---> %s号玩家的手牌信息为: %s张, %s" % (value['SeatID'], value['CardNum'], value['Cards']))
#
#             for key, value in data['TiInfo'].items():
#                 logging.info("    ---> %s号玩家的提牌信息为: %s张, %s" % (value['SeatID'], value['Num'], value['Cards']))
#                 print("    ---> %s号玩家的提牌信息为: %s张, %s" % (value['SeatID'], value['Num'], value['Cards']))
#             print()
#
#         time.sleep(2)
#         # self.ReadyGame()
#
#     def OnTotalSettlement(self, data):
#         pass
#
#     def OnErrorTips(self, data):
#         if data["error_code"][1] != 0:
#             print("房间通知: 当前操作有误, 错误码是: < %s >, 说明 -7 为非法操作, 参数错误. -20为出牌失败,可能是当前出的牌不在手牌中." % data["error_code"][1])
#
#     def OperateApi(self, option, last_card="", card_types=None):
#         if option in ["跑", "提", "偎"]:
#             print("此操作 <%s> 由服务器主动执行, 等待服务器执行中." % option)
#             return
#         while not self.CanOperate:
#             time.sleep(0.5)
#
#         self.CanOperate = False
#         operate = GetOperateID(option)
#         if card_types is None and option in [1, 11, 18, 19]:
#             print("操作为 <吃、出、溜、歪> 时, 应提供出牌牌型.")
#             return
#
#         if operate in [1, 11, 18, 19]:
#             operate_data = None
#             if operate == 1:
#                 operate_card = self.GetCardsStruct(card_types)
#                 for card in operate_card:
#                     if last_card in card:
#                         operate_card.remove(card)
#                         break
#
#                 operate_data = {"function_type": operate, "card_num": len(operate_card), "_card": operate_card,
#                                 "function_index": self.serial}
#
#             elif operate == 11:
#                 operate_card = card_types[0]
#                 operate_data = {"function_type": operate, "card_num": len(card_types), "_card": operate_card,
#                                 "function_index": self.serial}
#
#             elif operate == 18:
#                 pass
#
#             elif operate == 19:
#                 pass
#
#             else:
#                 print("玩家通知: 操作为 %s 的接口有误." % operate)
#             self.serial = None
#             self.PlayerOperates(operate_data)
#
#         elif operate in [2, 9, 10]:
#             operate_data = {"function_type": operate, "card_num": 0, "function_index": self.serial}
#             self.serial = None
#             self.PlayerOperates(operate_data)
#
#
#     def GetCardsStruct(self, card_data):
#         operate_card = []
#         for _type in card_data:
#             card_list = _type.split(",")
#             for i in card_list:
#                 operate_card.append(i + "\x00")
#
#         return operate_card
#
#     def DelHandCards(self, operate, tips_cards):
#         print(self.user_mid, "删除手牌操作是: %s, 要删的牌是: %s" % (operate, tips_cards))
#         #   跑牌, 不需要删
#         if operate is 3:
#             print(self.user_mid, "跑牌操作,无需删除手牌...")
#
#         #   偎牌或者臭偎
#         elif operate is 6 or operate is 16:
#             del_index = 0
#             for i in tips_cards:
#                 if i in self.hand_cards:
#                     if del_index < 2:
#                         self.hand_cards.remove(i)
#                         del_index += 1
#                     else:
#                         break
#             print(self.user_mid, "偎牌操作,删除2张...")
#
#         #   提牌， 删除4张
#         elif operate is 8:
#             for i in tips_cards:
#                 if i in self.hand_cards:
#                     self.hand_cards.remove(i)
#             print(self.user_mid, "起手提操作,删除4张...")
#
#         # 如果是溜，删4张
#         if operate is 19:
#             for i in tips_cards:
#                 if i in self.hand_cards:
#                     self.hand_cards.remove(i)
#             print(self.user_mid, "起手溜操作,删除4张...")
#
#         # 如果是歪, 删2张
#         elif operate is 18:
#             del_index = 0
#             for i in tips_cards:
#                 if i in self.hand_cards:
#                     if del_index < 2:
#                         self.hand_cards.remove(i)
#                         del_index += 1
#                     else:
#                         break
#             print(self.user_mid, "歪牌操作,删除2张...")
#
#         # 如果是歪变溜,不用删
#         elif operate is 20:
#             if self.room_type is RoomInfo().YiYang:
#                 for i in tips_cards:
#                     if i in self.hand_cards:
#                         self.hand_cards.remove(i)
#                 print(self.user_mid, "歪溜删牌4张， 删掉的牌是: %s" % tips_cards)
#             else:
#                 print(self.user_mid, "歪溜无需删牌...")
#
#         # 如果是坎变溜,删3张
#         elif operate is 31:
#             del_index = 0
#             for i in tips_cards:
#                 if i in self.hand_cards:
#                     if del_index < 3:
#                         self.hand_cards.remove(i)
#                         del_index += 1
#                     else:
#                         break
#             print(self.user_mid, "坎溜操作，删除3张...")
#
#         # 如果是碰,删掉两张
#         elif operate is 2:
#             del_index = 0
#             for i in tips_cards:
#                 if i in self.hand_cards:
#                     if del_index < 2:
#                         self.hand_cards.remove(i)
#                         del_index += 1
#                     else:
#                         break
#             print(self.user_mid, "碰牌操作,删除2张...")
#
#         # 如果是吃
#         elif operate is 1:
#             for i in tips_cards:
#                 if i in self.hand_cards and i != self.last_push_card:
#                     self.hand_cards.remove(i)
#
#             print(self.user_mid, "吃牌操作,删除2张...%s" % tips_cards)
#
#         # 如果是出
#         elif operate is 11:
#             self.hand_cards.remove(tips_cards[0])
#             print(self.user_mid, "出牌操作,删除1张...%s" % tips_cards[0])
#         elif operate is 7:
#             print(self.user_mid, "无人要的牌，已经在出牌的时候提前打了...")
#         elif operate is -7:
#             print(self.user_mid, "非法操作....")
#         elif operate is -20:
#             print(self.user_mid, "无法出牌...")
#         elif operate is 9:
#             print(self.user_mid, "胡牌操作，无需删除手牌...")
#         else:
#             print(self.user_mid, "尚未添加的操作是: %s" % operate)
