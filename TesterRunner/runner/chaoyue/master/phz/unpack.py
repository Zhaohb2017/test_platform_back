#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@ author: Hubery
@ create on: 2018/10/9 17:09
@ file: unpack.py
@ site: 
@ purpose: unpack into plain text
"""
import struct
from runner.chaoyue.master.phz.protocol import *

class DefineProtocol:
    """
        客户端发包CS
    """
    PAO_HU_ZI_CS_LOGIN = 1000  # 登录
    PAO_HU_ZI_CS_REQUEST_ENTER_ROOM = 1001  # 请求进入房间
    PAO_HU_ZI_CS_LEAVE_ROOM = 1004  # 离开房间
    PAO_HU_ZI_CS_REQUEST_READY = 1006  # 请求准备
    PAO_HU_ZI_CS_REQUEST_QUERY_PLAYER_ROOM_INFO = 1009  # 请求玩家房间及玩家信息
    PAO_HU_ZI_CS_CREATE_ROOM = 1010  # 创建房间
    PAO_HU_ZI_CS_REQUEST_FUNCTION = 1012  # 请求操作
    PAO_HU_ZI_CS_DISSOLVE_ROOM = 1018  # 解散房间
    PAO_HU_ZI_CS_CHOSE_DISSOLVE_ROOM = 1020  # 选择解散房间
    PAO_HU_ZI_CS_JINGWEIDU = 1028  # 经纬度
    PAO_HU_ZI_CS_CHECK_IN_CLUB = 1041  # 检查是否在俱乐部里面
    PAO_HU_ZI_CS_GAME_SERVER_TRUSTEESHIP = 1053  # 游戏服托管
    PAO_HU_ZI_CS_MAKE_CARDS_TYPE = 1057  # 测试专用做牌
    PAO_HU_ZI_CS_CREATED_GAME_LIST = 1100  # 已创建的比赛
    PAO_HU_ZI_CS_CLUB_GAME_LIST = 1101  # 所在俱乐部比赛
    PAO_HU_ZI_CS_CHAT_SEND_CONTENT = 2001  # 发聊天内容
    PAO_HU_ZI_CS_CHAT_SEND_CONTENT_WITH_FACE = 2009  # 发表情

    PAO_HU_ZI_CS_SEND_GIFT = 1042  # 送礼物

    """
        服务器回包SC
    """
    PAO_HU_ZI_SC_LOGIN = 1000  # 登录
    PAO_HU_ZI_SC_REQUEST_ENTER_ROOM = 1001  # 请求进入房间
    PAO_HU_ZI_SC_ROOM_SNAPSHOT = 1002  # 房间快照
    PAO_HU_ZI_SC_DESKTOP_SNAPSHOT = 1003  # 桌面快照
    PAO_HU_ZI_SC_LEAVE_ROOM = 1004  # 离开房间
    PAO_HU_ZI_SC_ENTER_ROOM_PLAYER_INFO = 1005  # 通知进入房间玩家信息
    PAO_HU_ZI_SC_REQUEST_READY = 1006  # 请求准备
    PAO_HU_ZI_SC_GAME_START = 1008  # 游戏开始
    PAO_HU_ZI_SC_CREATE_ROOM = 1010  # 创建房间
    PAO_HU_ZI_SC_SEND_CARDS = 1011  # 发牌
    PAO_HU_ZI_SC_REQUEST_FUNCTION = 1012  # 请求操作
    PAO_HU_ZI_SC_TOUCH_CARDS = 1013  # 摸牌
    PAO_HU_ZI_SC_WHICH_PLAYER_CAN_DO = 1014  # 广播谁可以做什么操作
    PAO_HU_ZI_SC_TOTAL_SETTLEMENT = 1015  # 总结算
    PAO_HU_ZI_SC_PLAY_GAME_TIMES = 1017  # 广播当前已玩的局数
    PAO_HU_ZI_SC_DISSOLVE_ROOM = 1018  # 解散房间
    PAO_HU_ZI_SC_STEP_OUT_ROOM = 1019  # 暂离房间
    PAO_HU_ZI_SC_CHOSE_DISSOLVE_ROOM = 1020  # 选择解散房间
    PAO_HU_ZI_SC_SETTLEMENT = 1026  # 小局结算
    PAO_HU_ZI_SC_ERROR_TIPS = 1027  # 错误提示
    PAO_HU_ZI_SC_JINGWEIDU = 1028  # 经纬度
    PAO_HU_ZI_SC_RECONNECTION_SERVER_SEND_CARDS = 1035  # 断线重连后服务器推自己手上的牌
    PAO_HU_ZI_SC_SEND_GIFT = 1042  # 送礼物
    PAO_HU_ZI_SC_NOT_IN_ROOM = 1043  # 不在房间中，不能进行操作
    PAO_HU_ZI_SC_GAME_SERVER_TRUSTEESHIP = 1053  # 游戏服托管
    PAO_HU_ZI_SC_MAKE_CARDS_TYPE = 1057  # 测试专用做牌
    PAO_HU_ZI_SC_IS_JIACHUI = 1059  # 玩家选择是否加锤
    PAO_HU_ZI_SC_CREATED_GAME_LIST = 1100  # 已创建的比赛
    PAO_HU_ZI_SC_CLUB_GAME_LIST = 1101  # 所在俱乐部比赛
    PAO_HU_ZI_SC_CHANGE_GOLD_COINS = 1086  # 金币改变
    PAO_HU_ZI_SC_SERVER_CLOSE = 1998  # 服务器即将关闭
    PAO_HU_ZI_SC_RECONNECTION = 1999  # 断线重连
    PAO_HU_ZI_SC_COMMON_CHAT = 2002  # 广播公聊
    PAO_HU_ZI_SC_CHAT_SEND_CONTENT = 2001  # 发聊天内容
    PAO_HU_ZI_SC_COMMON_CHAT_WITH_FACE = 2010  # 广播公聊 表情
    PAO_HU_ZI_SC_CHAT_SEND_CONTENT_WITH_FACE = 2009  # 发表情
    PAO_HU_ZI_SC_PLAYER_CHANGE_IDENTITY = 10022  # 玩家改变身份
    PAO_HU_ZI_SC_CHANGE_SERVER = 10080  # 切换服务器
    PAO_HU_ZI_SC_CREATE_ROOM_YIYANG = 2029  # 益阳创建房间
    PAO_HU_ZI_SC_SETTLEMENT_YUEYANG = 2025  # 岳阳结算
    PAO_HU_ZI_SC_CAN_MOTION = 2026  # 岳阳玩家能做什么
    PAO_HU_ZI_SC_TOTAL_SETTLEMENT_YUEYANG = 2028  # 岳阳总结算
    PAO_HU_ZI_SC_BLACK_CARDS = 2030  # 黑牌
    PAO_HU_ZI_SC_DEAD_HAND = 3035   # 死手
    PAO_HU_ZI_SC_SERVER_PUSH_GOD_CARDS = 3040    # 服务器推送神牌 益阳
    PAO_HU_ZI_SC_PLAYER_CAN_DO_YIYANG = 12026   # 益阳玩家能做什么
    PAO_HU_ZI_SC_PUSH_CHOU_CARD_YIYANG = 2030   # 益阳臭牌
    PAO_HU_ZI_SC_SEND_CARDS_RUNFAST = 5020      #跑得快发牌
    PAO_HU_ZI_SC_NEXT_USER_OUTCARD = 5021       #跑得快下一个出牌玩家
    PAO_HU_ZI_SC_USER_OUTCARD = 5023            #跑得快用户出牌
    PAO_HU_ZI_SC_READY = 5005                   # 跑得快用户准备
    PAO_HU_ZI_SC_GAMESTART = 5007               # 服务器广播游戏开始
    PAO_HU_ZI_SC_DISSOLVERUNFAST = 5008         #客户端发起解散房间
    PAO_HU_ZI_SC_JIACHUI   = 1058               # 广播选择加锤
    RUNFAST_REQUEST_LEAVE_ROOM = 5009                    #用户请求离开房间
    RUNFAST_OPERATION = 5022                        #通知用户做相应的操作
    RUNFAST_DISSOLVEROOM = 5012
    RUNFAST_BROADCAST_HAS_BEEN_DISBAND = 5013       # 解散房间服务器应答
    RUNFAST_SETTLE_ACCOUNTS_SMALL = 5025            # 小局结算
    RUNFAST_SETTLE_ACCOUNTS_BIG = 5027              # 大局结算
    MAJIANG_PUSH_PLAYERS_SHAPSHOT = 6002            # 服务器通知进入房间
    MAJIANG_CLIENT_REQUEST_DISSOLVE = 6008          # 客户端发起解散房间
    MAJIANG_CLIENT_REQUEST_LEAVE_ROOM = 6009        # 客户端发起解散房间
    MAJIANG_BROADCAST_HAS_BEEN_DISBAND = 6013       # 解散房间服务器应答
    MAJIANG_READY = 6005                            # 玩家准备
    MAJIANG_SERVER_BROADCAST_GAMESTART = 6007       # 服务器广播游戏开始
    MAJIANG_SERVER_NOTIFY_ON_DEAL = 6023            # 发牌
    MAJIANG_SERVER_BROADCAST_NEXT_PLAYER = 6025     # 服务器广播下个出牌人
    MAJIANG_SERVER_NOTIFY_ISTING = 6044             # 服务器通知是否听牌
    MAJIANG_SERVER_NOTIFY_OPERATE = 6026            # 服务器通知玩家做相应的操作
    MAJIANG_CLIENT_RESPONSE_DISSOLVE = 6012         # 选择是否解散房间
    MAJIANG_ACCOUNT_SMALL = 6037                    # 小局结算
    MAJIANG_ZHA_NIAO = 6036                         # 服务器广播扎码牌
    MAJIANG_ACCOUNT_BIG = 6038                      # 大局结算
    MAJIANG_ONPLAY = 6029                           # 出牌数据
    MAJIANG_ONCANCLE = 6030                         # 取消
    MAJIANG_ONCHI = 6031                            # 吃牌数据
    MAJIANG_ONPENG = 6032                           # 碰牌数据
    MAJIANG_ONGANG = 6033                           # 杠牌数据
    MAJIANG_ONHU =  6034                            # 胡牌数据
    MAJIANG_ONBU = 6050                             # 补杠
    MAJIANG_MOCARD = 6027                           # 服务器通知用户摸牌
    MAJIANG_PIAOFEN = 6021                         # 飘风
    MAJIANG_BROADCAST_PIAO = 6020                   # 服务器通知玩家飘分
    MAJIANG_JIACHUI = 6052                          # 通知客户端锤
    MAJIANG_CHUI_OPERATION = 6053                   # 锤







#   根据参数数据类型分类
class ProtocolClassify:
    # 根据每个协议实体中参数数据类型划分，纯int32, 纯int16, 纯int64，含有string四类
    protocol_classify = {"INT32": [DefineProtocol.PAO_HU_ZI_SC_LOGIN, DefineProtocol.PAO_HU_ZI_SC_RECONNECTION,
                                   DefineProtocol.PAO_HU_ZI_SC_CHANGE_SERVER, ], "INT16": [],
                         "INT64": [DefineProtocol.PAO_HU_ZI_SC_CHANGE_GOLD_COINS, ],
                         "STRING": [DefineProtocol.PAO_HU_ZI_SC_CREATE_ROOM,
                                    DefineProtocol.PAO_HU_ZI_SC_REQUEST_ENTER_ROOM, ], }
    #   协议号对应的回包处理函数
    protocol_corresponding_function = {DefineProtocol.PAO_HU_ZI_SC_LOGIN: [SCLogin, "OnLogin"],
                                       # DefineProtocol.PAO_HU_ZI_SC_CHANGE_GOLD_COINS: [SCGoldCoinsChange,
                                       #                                                 "sc_gold_coins_change"],
                                       DefineProtocol.PAO_HU_ZI_SC_RECONNECTION: [SCReconnection, "OnReconnect"],
                                       # DefineProtocol.PAO_HU_ZI_SC_CHANGE_SERVER: [SCChangeServer, "sc_change_server"],
                                       DefineProtocol.PAO_HU_ZI_SC_CREATE_ROOM: [SCCreateRoom, "OnCreateRoom"],
                                       DefineProtocol.PAO_HU_ZI_SC_LEAVE_ROOM: [SCLeaveRoom, "OnLeaveRoom"],
                                       DefineProtocol.PAO_HU_ZI_SC_DISSOLVE_ROOM: [SCDissolveRoom, "OnInformDissolveRoom"],
                                       # DefineProtocol.PAO_HU_ZI_SC_DISSOLVE_ROOM: [SCLeaveRoom, "sc_leave_room"],
                                       DefineProtocol.PAO_HU_ZI_SC_CHOSE_DISSOLVE_ROOM: [SCChoseDissolveRoom,
                                                                                         "OnVoteDissolveRoom"],
                                       DefineProtocol.PAO_HU_ZI_SC_REQUEST_ENTER_ROOM: [SCRequestEnterRoom,
                                                                                        "OnInformEnterRoom"],
                                       DefineProtocol.PAO_HU_ZI_SC_GAME_SERVER_TRUSTEESHIP: [SCTrusteeship,
                                                                                             "sc_trusteeship"],
                                       DefineProtocol.PAO_HU_ZI_SC_DESKTOP_SNAPSHOT: [SCDesktopSnapshot,
                                                                                      "sc_desktop_snapshot"],
                                       DefineProtocol.PAO_HU_ZI_SC_ROOM_SNAPSHOT: [SCRoomSnapshot, "sc_room_snapshot"],
                                       DefineProtocol.PAO_HU_ZI_SC_ENTER_ROOM_PLAYER_INFO: [SCEnterRoomPlayerInfo,
                                                                                            "sc_enter_room_player_info"],
                                       DefineProtocol.PAO_HU_ZI_SC_REQUEST_READY: [SCRequestReady, "OnReadyGame"],
                                       DefineProtocol.PAO_HU_ZI_SC_PLAY_GAME_TIMES: [SCPlayGameTimes,
                                                                                     "sc_play_game_times"],
                                       DefineProtocol.PAO_HU_ZI_SC_NOT_IN_ROOM: [SCNotInRoom, "sc_not_in_room"],
                                       DefineProtocol.PAO_HU_ZI_SC_SERVER_CLOSE: [SCServerClose, "sc_server_close"],
                                       DefineProtocol.PAO_HU_ZI_SC_GAME_START: [SCGameStart, "OnGameStart"],
                                       DefineProtocol.PAO_HU_ZI_SC_SEND_CARDS: [SCSendCards, "OnRecvCards"],
                                       DefineProtocol.PAO_HU_ZI_SC_TOUCH_CARDS: [SCTouchCards, "OnTouchCard"],
                                       DefineProtocol.PAO_HU_ZI_SC_WHICH_PLAYER_CAN_DO: [SCPlayerCanDo,
                                                                                         "OnPlayerCanDo"],
                                       DefineProtocol.PAO_HU_ZI_SC_REQUEST_FUNCTION: [SCRequestFunction,
                                                                                      "OnPlayerOperate"],
                                       DefineProtocol.PAO_HU_ZI_SC_SETTLEMENT: [SCSettlement, "OnSettlement"],
                                       DefineProtocol.PAO_HU_ZI_SC_TOTAL_SETTLEMENT: [SCTotalSettlement,
                                                                                      "OnTotalSettlement"],
                                       DefineProtocol.PAO_HU_ZI_SC_COMMON_CHAT: [SCCommonChat, "sc_common_chat"],
                                       DefineProtocol.PAO_HU_ZI_SC_ERROR_TIPS: [SCErrorTips, "OnErrorTips"],
                                       DefineProtocol.PAO_HU_ZI_CS_CHAT_SEND_CONTENT: [SCChat, "sc_chat"],
                                       DefineProtocol.PAO_HU_ZI_CS_CHAT_SEND_CONTENT_WITH_FACE: [SCChatFace,
                                                                                                 "sc_chat_face"],
                                       DefineProtocol.PAO_HU_ZI_SC_SEND_GIFT: [SCSendGift, "sc_send_gift"],
                                       DefineProtocol.PAO_HU_ZI_SC_COMMON_CHAT_WITH_FACE: [SCCommonChatWithFace,
                                                                                           "sc_common_chat_with_face"],
                                       DefineProtocol.PAO_HU_ZI_SC_MAKE_CARDS_TYPE: [SCMakeCardsType,
                                                                                     "OnMakeCards"],
                                       DefineProtocol.PAO_HU_ZI_SC_RECONNECTION_SERVER_SEND_CARDS: [
                                           SCReconnectionServerSendCards, "sc_reconnection_server_send_cards"],
                                       DefineProtocol.PAO_HU_ZI_SC_JINGWEIDU: [SCJingWeiDu, "sc_jingweidu"],
                                       DefineProtocol.PAO_HU_ZI_SC_CREATED_GAME_LIST: [SCCreatedGameList,
                                                                                       "sc_created_game_lisst"],
                                       DefineProtocol.PAO_HU_ZI_SC_CLUB_GAME_LIST: [SCClubGameList,
                                                                                    "sc_club_game_list"],
                                       # DefineProtocol.PAO_HU_ZI_SC_PLAYER_CHANGE_IDENTITY: [SCPlayerChangeIdentity,
                                       #                                                      "sc_player_change_identity"],
                                       DefineProtocol.PAO_HU_ZI_SC_CREATE_ROOM_YIYANG: [SCCreateRoomYiYang,
                                                                                        "OnCreateRoomYiYang"],
                                       DefineProtocol.PAO_HU_ZI_SC_CAN_MOTION: [SCPlayerCanDoYueYang,
                                                                                'sc_player_can_do_yueyang'],
                                       DefineProtocol.PAO_HU_ZI_SC_STEP_OUT_ROOM: [SCStepOutRoom, 'sc_step_out_room'],
                                       DefineProtocol.PAO_HU_ZI_SC_BLACK_CARDS: [SCBlackCards, 'sc_black_cards'],
                                       DefineProtocol.PAO_HU_ZI_SC_SETTLEMENT_YUEYANG: [SCSettlementYueYang, 'sc_settlement_yueyang'],
                                       DefineProtocol.PAO_HU_ZI_SC_TOTAL_SETTLEMENT_YUEYANG: [SCTotalSettlementYueYang, 'sc_total_settlement_yueyang'],
                                       DefineProtocol.PAO_HU_ZI_SC_DEAD_HAND: [SCDeadHand, "sc_dead_hand"],
                                       DefineProtocol.PAO_HU_ZI_SC_PLAYER_CAN_DO_YIYANG: [SCPlayerCanDoYiYang, 'sc_player_can_do_yiyang'],
                                       DefineProtocol.PAO_HU_ZI_SC_SERVER_PUSH_GOD_CARDS: [SCServerPushGodCards, 'sc_server_push_god_cards'],
                                       DefineProtocol.PAO_HU_ZI_SC_PUSH_CHOU_CARD_YIYANG: [SCSmellyCard, 'sc_smelly_card_yiyang'],
                                       DefineProtocol.PAO_HU_ZI_SC_IS_JIACHUI: [SCPaohuziJiaChui,"sc_paohuzi_isJiachui"],

                                       1093: [SCInformLessMode, "OnInformLessMode"],
                                       1094: [SCOpenLessMode, "OnOpenLessMode"],
                                       DefineProtocol.PAO_HU_ZI_SC_SEND_CARDS_RUNFAST: [SCSendCardsRunfast,'sc_runfast_sendCard'],
                                       DefineProtocol.PAO_HU_ZI_SC_NEXT_USER_OUTCARD: [SCNextUserRunfast,'sc_runfast_nextUser'],
                                       DefineProtocol.PAO_HU_ZI_SC_USER_OUTCARD: [SCOutCard,"sc_runfast_outcard"],
                                       DefineProtocol.PAO_HU_ZI_SC_JIACHUI: [SCJiachui,"sc_paohuzi_jiaochui"],
                                       DefineProtocol.PAO_HU_ZI_SC_READY: [SCReady,"sc_runfast_ready"],
                                       DefineProtocol.PAO_HU_ZI_SC_GAMESTART: [SCBroadcastGameStart,'sc_runfast_BroadcastGameStart'],
                                       DefineProtocol.PAO_HU_ZI_SC_DISSOLVERUNFAST: [SCDissolveRoomFunfast,"sc_runfast_dissolveRoom"],
                                       DefineProtocol.RUNFAST_OPERATION: [SCRunfastOperation,"sc_runfast_operation"],
                                       DefineProtocol.RUNFAST_DISSOLVEROOM: [SCRunfastDissolveroom,'sc_runfast_dissolveroomInfo'],
                                       DefineProtocol.RUNFAST_SETTLE_ACCOUNTS_SMALL: [SCRunfastSettleAccountsSmall,'sc_runfast_settleAccountSmall'],
                                       DefineProtocol.RUNFAST_BROADCAST_HAS_BEEN_DISBAND: [SCRunfastBeenDisband,'sc_runfast_bennDisband'],
                                       DefineProtocol.RUNFAST_REQUEST_LEAVE_ROOM: [SCRunfastLeaveRoom,'sc_runfast_leaveRoom'],
                                       DefineProtocol.RUNFAST_SETTLE_ACCOUNTS_BIG: [SCRunfastSettleAccountsBig,'sc_runfast_settleAccountBig'],
                                       DefineProtocol.MAJIANG_CLIENT_REQUEST_DISSOLVE: [SCMajiangDissolve,"sc_majiang_dissolve"],
                                       DefineProtocol.MAJIANG_CLIENT_REQUEST_LEAVE_ROOM: [SCMajiangLeaveRoom,'sc_majiang_leaveRoom'],
                                       DefineProtocol.MAJIANG_BROADCAST_HAS_BEEN_DISBAND: [SCMajiangBeenDisband,"sc_majiang_beenDisband"],
                                       DefineProtocol.MAJIANG_READY: [SCMajiangReady,'sc_majiang_ready'],
                                       DefineProtocol.MAJIANG_SERVER_BROADCAST_GAMESTART: [SCMajiangGameStart,"sc_majiang_gameStart"],
                                       DefineProtocol.MAJIANG_SERVER_NOTIFY_ON_DEAL: [SCMajiangNotifyOnDeal,"sc_majiang_userCard"],
                                       DefineProtocol.MAJIANG_SERVER_BROADCAST_NEXT_PLAYER: [SCMajiangNextPlayer,'sc_majiang_nextPlayer'],
                                       DefineProtocol.MAJIANG_SERVER_NOTIFY_ISTING: [SCMajiangNotifyIsTing,"sc_majiang_ting"],
                                       DefineProtocol.MAJIANG_SERVER_NOTIFY_OPERATE: [SCMajiangOperate,"sc_majiang_operate"],
                                       DefineProtocol.MAJIANG_CLIENT_RESPONSE_DISSOLVE: [SCMajiangResponseDissoleve,'sc_majiang_responseDissolve'],
                                       DefineProtocol.MAJIANG_ACCOUNT_SMALL: [SCMajiangAccountSmall,'sc_majiang_accountSmall'],
                                       DefineProtocol.MAJIANG_ZHA_NIAO: [SCMajiangZhaMa,'sc_majiang_zhaMa'],
                                       DefineProtocol.MAJIANG_ACCOUNT_BIG: [SCMajiangAccountBig,'sc_majiang_accountBig'],
                                       DefineProtocol.MAJIANG_ONPLAY: [SCMajiangOnPlay,"sc_majiang_OnPlay"],
                                       DefineProtocol.MAJIANG_ONCHI: [SCMajiangOnChi,"sc_majiang_OnChi"],
                                       DefineProtocol.MAJIANG_ONPENG: [SCMajiangOnPeng,"sc_majiang_OnPeng"],
                                       DefineProtocol.MAJIANG_ONGANG: [SCMajiangOnGang,"sc_majiang_OnGang"],
                                       DefineProtocol.MAJIANG_ONHU: [SCMajiangOnHu,"sc_majiang_OnHu"],
                                       DefineProtocol.MAJIANG_ONCANCLE: [SCMajiangOnCancle,"sc_majiang_OnCancle"],
                                       DefineProtocol.MAJIANG_MOCARD: [SCMajiangMoCard,"sc_majiang_MoCard"],
                                       DefineProtocol.MAJIANG_ONBU: [SCMajiangOnBu,"sc_majiang_OnBu"],
                                       DefineProtocol.MAJIANG_PIAOFEN: [SCMajiangPiaoFen,"sc_majiang_piaofen"],
                                       DefineProtocol.MAJIANG_BROADCAST_PIAO: [SCMajiangPiao,"sc_majiang_broadcast_piao"],
                                       DefineProtocol.MAJIANG_JIACHUI:[SCMajiangNotifyJiaChui,"sc_majiang_Notifyjiachui"],
                                       DefineProtocol.MAJIANG_CHUI_OPERATION: [SCMajiangChui,"sc_majiang_chui"],
                                       }


class UnPackData:
    #   初始化协议号及包体数据
    def __init__(self):
        self.current_index = 0
        self.result = None
        self.normal_entity_list = [1000, 1004,1006, 1008, 1010, 1001,1013, 1014, 1016, 1017, 1019, 1020, 1035,
                                   1042, 1043, 1053, 1047, 1057,1058,1059, 1086, 1998, 1999, 2001, 2002, 2009, 2010, 2026,2027,
                                   2029, 3035, 3040, 10022, 10080, 12026, 2030,5021,5023,5005,5007,5009,5012,5013,6009,6013,
                                   6005,6007,6044,6025,6012,6030,6033,6034,6035,6027,6021,6020,6052,6053
                                   ]


    def get_protocol_classify(self, protocol_num):
        classify_list = ProtocolClassify.protocol_classify
        classify = None
        #   拿到协议所属分类
        for key, value in classify_list.items():
            for i in range(len(value)):
                if classify is None:
                    if protocol_num == value[i]:
                        classify = key
                        break
        if classify is not None:
            return classify
        else:
            return None

    def read_int16(self, data):
        value = struct.unpack("<h", data[0: 2])[0]
        return value

    def read_int32(self, data):
        value = struct.unpack("<i", data[0: 4])[0]
        return value

    def read_int64(self, data):
        value = struct.unpack("<q", data[0: 8])[0]
        return value

    def read_string(self, size, data):
        fmt = "<%ds" % size
        value = struct.unpack(fmt, data)[0]
        return value.decode("utf-8")

    def read_string1(self, data):
        size = self.read_int32()
        fmt = "<%ds" % size
        value = struct.unpack(fmt, self.body[self.cur_read_pos:self.cur_read_pos + struct.calcsize(fmt)])[0]
        return value

    def unpack_data(self, protocol_num, protocol_entity, data):
        need_parse_data = data
        entity = protocol_entity()
        entity_data = entity.sc_entity_data
        current_index = 0
        if protocol_num == 1001:
            size = self.read_int32(need_parse_data[12: (12 + 4)])
            game_type = self.read_string(size, need_parse_data[16: 16 + size])
            self.game_type = game_type
            if int(game_type[:-1]) in [25,26,28, 27,29,30,31,32,33,34]:
                for i in entity_data:
                    if i == "error_code":
                        entity_data[i][1]  = self.read_int32(need_parse_data[0: (4)])
                    if i == "timer":
                        entity_data[i][1] = self.read_int32(need_parse_data[4: (8)])
                    if i == "seat_id":
                        entity_data[i][1] = self.read_int32(need_parse_data[8: (8 + 4)])
                return entity_data


        elif protocol_num == 1005:
            print("1005协议号数据暂不解析")


        if protocol_num in self.normal_entity_list:
            for i in entity_data:
                if len(need_parse_data) <= 0 or len(need_parse_data) - current_index <= 0:
                    break

                if entity_data[i][0] == "INT32":
                    if len(need_parse_data) - current_index < 4:
                        break
                    entity_data[i][1] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                    current_index += 4
                elif entity_data[i][0] == "INT16":
                    if len(need_parse_data) - current_index < 2:
                        break
                    entity_data[i][1] = self.read_int16(need_parse_data[current_index: (current_index + 2)])
                    current_index += 2
                elif entity_data[i][0] == "INT64":
                    if len(need_parse_data) - current_index < 8:
                        break
                    entity_data[i][1] = self.read_int64(need_parse_data[current_index: (current_index + 8)])
                    current_index += 8
                else:
                    size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                    current_index += 4

                    entity_data[i][1] = self.read_string(size, need_parse_data[current_index: current_index + size])
                    current_index += size

                    # if protocol_num == DefineProtocol.PAO_HU_ZI_SC_CREATE_ROOM:  #     entity_data[i][1] = self.read_string(need_parse_data[current_index: current_index + len(str(entity_data[i][1]))])  #     current_index += len(entity_data[i][1])
        else:

            if protocol_num == 2026:
                print("xxxxxxxxxxxxxxxxx",need_parse_data)
                for i in entity_data:
                    if i == "BaiLiuZi":
                        BaiLiuZi = self.read_int16(need_parse_data[current_index: (current_index + 2)])
                        current_index += 4
                        print(BaiLiuZi)
                    if i == "seat_id":
                        seat_id = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                        current_index += 4
                        print(seat_id)
                    if i == "last_push_card":
                        name_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                        current_index += 4

                        last_push_card = self.read_string(name_len, need_parse_data[current_index: current_index + name_len])
                        current_index += name_len
                        print(last_push_card)
                    if i == "sure_liu_card":

                        name_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                        current_index += 4

                        sure_liu_card = self.read_string(name_len,
                                                          need_parse_data[current_index: current_index + name_len])
                        current_index += name_len
                        print(sure_liu_card)

                    if i == "sure_chi_card":
                        name_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                        current_index += 4

                        sure_chi_card = self.read_string(name_len,
                                                         need_parse_data[current_index: current_index + name_len])
                        current_index += name_len
                        print(sure_chi_card)

                    if i =="is_chu_card":
                        is_chu_card = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                        current_index += 4
                        print(is_chu_card)
                    if i == "is_peng_card":
                        is_peng_card = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                        current_index += 4
                        print(is_peng_card)
                    if i == "is_chi_card":
                        is_chi_card = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                        current_index += 4
                        print(is_chi_card)
                    if i == "is_hu_card":
                        is_hu_card = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                        current_index += 4
                        print(is_hu_card)





            if protocol_num == 5008:
                for i in entity_data:
                    if i == "error_code":
                        err = self.read_int32(need_parse_data[0: (4)])
                        entity_data[i][1] = err

                # return entity_data


            if protocol_num == 1002:  # 房间快照
                for i in entity_data:
                    if i == "_player_info":
                        num = entity_data['players'][1]
                        if num == 0:
                            break
                        info_data = {}
                        for k in range(num):
                            seat_id = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            mid = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            sex = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            name_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            name = self.read_string(name_len, need_parse_data[current_index: current_index + name_len])
                            current_index += name_len

                            icon_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            icon = self.read_string(icon_len, need_parse_data[current_index: current_index + icon_len])
                            current_index += icon_len

                            vip = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            gold = self.read_int64(need_parse_data[current_index: (current_index + 8)])
                            current_index += 8

                            jifen = self.read_int64(need_parse_data[current_index: (current_index + 8)])
                            current_index += 8

                            ip_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            ip = self.read_string(ip_len, need_parse_data[current_index: current_index + ip_len])
                            current_index += ip_len

                            key_1 = "seat_id_%s" % k
                            key_2 = "mid_%s" % k
                            key_3 = "sex_%s" % k
                            key_4 = "name_%s" % k
                            key_5 = "icon_%s" % k
                            key_6 = "vip_%s" % k
                            key_7 = "gold_%s" % k
                            key_8 = "jifen_%s" % k
                            key_9 = "ip_%s" % k

                            info_data[key_1] = seat_id
                            info_data[key_2] = mid
                            info_data[key_3] = sex
                            info_data[key_4] = name
                            info_data[key_5] = icon
                            info_data[key_6] = vip
                            info_data[key_7] = gold
                            info_data[key_8] = jifen
                            info_data[key_9] = ip
                        entity_data[i][1] = info_data
                    elif i == "info_jiwei":
                        num = entity_data['players'][1]
                        if num == 0:
                            break
                        info_data = {}
                        for j in range(num):
                            seat_id = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            jinwei_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            jinweidu = self.read_string(jinwei_len,
                                                        need_parse_data[current_index: current_index + jinwei_len])
                            current_index += jinwei_len

                            key_1 = "seat_id_%s" % j
                            key_2 = "jinweidu_%s" % j

                            info_data[key_1] = seat_id
                            info_data[key_2] = jinweidu
                        entity_data[i][1] = info_data
                    else:
                        if len(need_parse_data) - current_index < 4:
                            break
                        entity_data[i][1] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                        current_index += 4


            elif protocol_num == 5025:
                custom_list = []
                outcard_list = []
                players_info = {}
                players_data = {}

                for i in entity_data:
                    if i == "players_info":
                        print()
                        for x in range(entity_data["players_num"]):
                            seat_id = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            mid = self.read_int32(need_parse_data[current_index: (current_index + 4)])

                            current_index += 4

                            name_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            name = self.read_string(name_len,need_parse_data[current_index: current_index + name_len])
                            current_index += name_len

                            icon_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            icon = self.read_string(icon_len, need_parse_data[current_index: current_index + icon_len])
                            current_index += icon_len

                            bomb_num = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            score = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            seat_score = self.read_int64(need_parse_data[current_index: (current_index + 8)])
                            current_index += 8

                            hand_cards_num = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            if hand_cards_num != 0:
                                for i in range(hand_cards_num):
                                    card_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                    current_index += 4
                                    card = self.read_string(card_len,need_parse_data[current_index: current_index + card_len])
                                    current_index += card_len
                                    custom_list.append(card)

                            outcard_num = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            if outcard_num != 0:
                                for i in range(outcard_num):
                                    card_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                    current_index += 4
                                    card = self.read_string(card_len,
                                                            need_parse_data[current_index: current_index + card_len])
                                    current_index += card_len
                                    outcard_list.append(card)

                            players_data["seat_id"] = seat_id
                            players_data["mid"] = mid
                            players_data["name"] = name
                            players_data["icon"] = icon
                            players_data["bomb_num"] = bomb_num
                            players_data["score"] = score
                            players_data["seat_score"] = seat_score
                            players_data["hand_cards_num"] = hand_cards_num
                            players_data["hand_cards"] = custom_list
                            players_data["outcard_num"] = outcard_num
                            players_data["outcard_list"] = outcard_list
                            players_info["%s"%x] = players_data
                        entity_data['players_info'][1] = players_info

                    elif i == "cards_info":
                        info_list = []
                        if entity_data["cards_remaining_num"] is not 0:
                            for x in range(entity_data["cards_remaining_num"]):
                                card_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4
                                card = self.read_string(card_len,need_parse_data[current_index: current_index + card_len])
                                current_index += card_len
                                info_list.append(card)
                        entity_data[i][1] = info_list

                    else:
                        if entity_data[i][0] == "INT32":
                            if len(need_parse_data) - current_index < 4:
                                break
                            entity_data[i] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                        elif entity_data[i][0] == "STRING":
                            size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            entity_data[i] = self.read_string(size,need_parse_data[current_index: current_index + size])
                            current_index += size

            elif protocol_num == 5027 :
                players_data = {}
                players_info = {}
                for i in entity_data:
                    if i == "Playing_info":
                        for x in range(entity_data["Playing_num"]):
                            seat_id = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            mid = self.read_int32(need_parse_data[current_index: (current_index + 4)])

                            current_index += 4

                            name_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            name = self.read_string(name_len,need_parse_data[current_index: current_index + name_len])
                            current_index += name_len

                            icon_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            icon = self.read_string(icon_len, need_parse_data[current_index: current_index + icon_len])
                            current_index += icon_len

                            seat_score = self.read_int64(need_parse_data[current_index: (current_index + 8)])
                            current_index += 8

                            bomb_num = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            win_num = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            lose_num = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            top_score = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4


                            players_data["seat_id"] = seat_id
                            players_data["mid"] = mid
                            players_data["name"] = name
                            players_data["icon"] = icon
                            players_data["seat_score"] = seat_score
                            players_data["bomb_num"] = bomb_num
                            players_data["win_num"] = win_num
                            players_data["lose_num"] = lose_num
                            players_data["top_score"] = top_score
                            players_info["%s"%x] = players_data
                        entity_data['Playing_info'][1] = players_info

                    elif i == "dissolveTypeInfo":
                        dissolveTypeInfo_list = {}
                        if entity_data["dissolveType"] is not 0:
                            user_num = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            for x in range(user_num):
                                seat_id = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4
                                dissolve_type = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4
                                dissolveTypeInfo_list['seat_id'] = seat_id
                                dissolveTypeInfo_list['dissolve_type'] = dissolve_type

                        entity_data['dissolveTypeInfo'][1] = dissolveTypeInfo_list

                    else:
                        if entity_data[i][0] == "INT32":
                            if len(need_parse_data) - current_index < 4:
                                break
                            entity_data[i] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                        elif entity_data[i][0] == "STRING":
                            size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            entity_data[i] = self.read_string(size,need_parse_data[current_index: current_index + size])
                            current_index += size

            elif protocol_num == 6050:
                for i in entity_data:
                    if i == "ErrorCode":
                        seat_id = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                        current_index += 4
                        entity_data["ErrorCode"] = seat_id
                    else:
                        if entity_data["ErrorCode"] in [1,2,3,4]:
                            if entity_data[i][0] == "INT32":
                                if len(need_parse_data) - current_index < 4:
                                    break
                                entity_data[i] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4

                            elif entity_data[i][0] == "STRING":
                                size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4
                                entity_data[i] = self.read_string(size,
                                                                  need_parse_data[current_index: current_index + size])
                                current_index += size







            elif protocol_num == 6037:
                hu_users_list = []
                Operation_cards_list = []
                hand_card_list = []
                mingtang_list = []
                players_info = {}

                for i in entity_data:
                    if i == "hu_player_seat_id":
                        for x in range(entity_data["hu_player_num"]):
                            seat_id = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            hu_users_list.append(seat_id)
                        entity_data["hu_player_seat_id"] = hu_users_list

                    elif i == "players_info":
                        for x in range(entity_data["players_num"]):
                            players_data = {}
                            seat_id = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            mid = self.read_int32(need_parse_data[current_index: (current_index + 4)])

                            current_index += 4

                            name_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            name = self.read_string(name_len, need_parse_data[current_index: current_index + name_len])
                            current_index += name_len


                            score = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            seat_score = self.read_int64(need_parse_data[current_index: (current_index + 8)])
                            current_index += 8

                            hucard_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            hu_cards = self.read_string(hucard_len, need_parse_data[current_index: current_index + hucard_len])
                            current_index += hucard_len

                            Operation_cards_num = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            if Operation_cards_num != 0:
                                Operation_cards_dict = {}
                                for i in range(Operation_cards_num):
                                    card_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                    current_index += 4
                                    card = self.read_string(card_len,need_parse_data[current_index: current_index + card_len])
                                    current_index += card_len

                                    OperationType = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                    current_index += 4
                                    Operation_cards_dict['card'] = card
                                    Operation_cards_dict['OperationType'] = OperationType
                                Operation_cards_list.append(Operation_cards_dict)


                            hand_card_num = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            if hand_card_num != 0:
                                for i in range(hand_card_num):
                                    card_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                    current_index += 4
                                    card = self.read_string(card_len,
                                                            need_parse_data[current_index: current_index + card_len])
                                    current_index += card_len
                                    hand_card_list.append(card)

                            mingtang_num = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            if mingtang_num != 0:
                                mingtang_dict = {}
                                for i in range(mingtang_num):
                                    MingTangType = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                    current_index += 4

                                    MingTang_Num = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                    current_index += 4
                                    mingtang_dict['MingTangType'] = MingTangType
                                    mingtang_dict['MingTang_Num'] = MingTang_Num
                                mingtang_list.append(mingtang_dict)

                            players_data["seat_id"] = seat_id
                            players_data["mid"] = mid
                            players_data["name"] = name
                            players_data["score"] = score
                            players_data["seat_score"] = seat_score
                            players_data["hu_cards"] = hu_cards
                            players_data["Operation_cards_num"] = Operation_cards_num
                            players_data["Operation_cards_list"] = Operation_cards_list
                            players_data["hand_card_num"] = hand_card_num
                            players_data["hand_card_list"] = hand_card_list
                            players_data["mingtang_num"] = mingtang_num
                            players_data["mingtang_list"] = mingtang_list
                            players_info["%s" % x] = players_data

                        entity_data['players_info'][1] = players_info

                    elif i == "zhaoMa_card":
                        info_list = []
                        if entity_data["zhaoMa_num"] is not 0:
                            for x in range(entity_data["zhaoMa_num"]):
                                card_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4
                                card = self.read_string(card_len,
                                                        need_parse_data[current_index: current_index + card_len])
                                current_index += card_len
                                info_list.append(card)
                        entity_data["zhaoMa_card"] = info_list
                    elif i == "zhongMa_players_info":
                        info_list = []
                        info_dict = {}
                        users_num = {}
                        if entity_data["zhongMa_players_num"] is not 0:
                            for x in range(entity_data["zhongMa_players_num"]):
                                seat_ID = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4

                                zhongMa_num = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4
                                card_list = []
                                if zhongMa_num is not 0:
                                    for z in range(zhongMa_num):
                                        card_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                        current_index += 4
                                        card = self.read_string(card_len,
                                                                need_parse_data[
                                                                current_index: current_index + card_len])
                                        current_index += card_len
                                        card_list.append(card)
                                info_dict["seat_ID"] = seat_ID
                                info_dict["zhongMa_num"] = zhongMa_num
                                info_dict["zhongMa_card"] = card_list
                                users_num["%s"%i] = info_dict
                            info_list.append(users_num)

                        entity_data["zhongMa_players_info"] = info_list

                    else:
                        if entity_data[i][0] == "INT32":
                            if len(need_parse_data) - current_index < 4:
                                break
                            entity_data[i] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                        elif entity_data[i][0] == "STRING":
                            size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            entity_data[i] = self.read_string(size,
                                                              need_parse_data[current_index: current_index + size])
                            current_index += size


            elif protocol_num == 6038:
                for i in entity_data:
                    if i == "dissolveTypeInfo":

                        user_info = {}
                        if entity_data["dissolveType"] is not 0:
                            for x in range(entity_data["Playing_num"]):
                                info_dict = {}
                                seat_ID = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4
                                dissolve_type = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4
                                info_dict['seat_ID'] = seat_ID
                                info_dict['dissolve_type'] = dissolve_type
                                user_info['%s'%x] = info_dict
                        entity_data["dissolveTypeInfo"] = user_info
                    else:
                        if entity_data[i][0] == "INT32":
                            if len(need_parse_data) - current_index < 4:
                                break
                            entity_data[i] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                        elif entity_data[i][0] == "STRING":
                            size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            entity_data[i] = self.read_string(size,
                                                              need_parse_data[current_index: current_index + size])
                            current_index += size

            elif protocol_num == 6029:
                for i in entity_data:
                    if i == "Error":
                        Error = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                        current_index += 4
                        entity_data['Error'][1] = Error
                    if i == "Card":
                        if entity_data['Error'][1] in [1,2,3,4]:
                            card_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            card = self.read_string(card_len,
                                                    need_parse_data[
                                                    current_index: current_index + card_len])
                            current_index += card_len
                            entity_data['Card'][1] = card

            elif protocol_num == 6031:
                for i in entity_data:
                    if i == "Error":
                        Error = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                        current_index += 4
                        entity_data['Error'][1] = Error
                    if i == "Card":
                        if entity_data['Error'][1] in [1,2,3,4]:
                            card_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            card = self.read_string(card_len,
                                                    need_parse_data[
                                                    current_index: current_index + card_len])
                            current_index += card_len
                            entity_data['Card'][1] = card

            elif protocol_num == 6032:
                for i in entity_data:
                    if i == "Error":
                        Error = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                        current_index += 4
                        entity_data['Error'][1] = Error

                    elif i == "by_peng_seat_id":
                        if entity_data['Error'][1] in [1, 2, 3, 4]:
                            seat_id = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            entity_data['by_peng_seat_id'][1] = seat_id


                    elif i == "by_card":
                        if entity_data['Error'][1] in [1,2,3,4]:
                            card_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            card = self.read_string(card_len,
                                                    need_parse_data[
                                                    current_index: current_index + card_len])
                            current_index += card_len
                            entity_data['by_card'][1] = card




            elif protocol_num == 6008:
                players_data = {}
                players_info = {}
                for i in entity_data:
                    if i == "player_info":
                        for x in range(entity_data["player_num"]):
                            seat_id = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            mid = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            players_data["seat_id"] = seat_id
                            players_data["mid"] = mid
                            players_info["%s" % x] = players_data
                        entity_data['player_info'][1] = players_info


                    else:
                        if entity_data[i][0] == "INT32":
                            if len(need_parse_data) - current_index < 4:
                                break
                            entity_data[i] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                        elif entity_data[i][0] == "STRING":
                            size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            entity_data[i] = self.read_string(size,
                                                              need_parse_data[current_index: current_index + size])
                            current_index += size


            elif protocol_num == 6023:
                cards = []
                for i in entity_data:
                    if i == "hand_cards":
                        for x in range(entity_data["hand_card_num"]):
                            size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            card = self.read_string(size,need_parse_data[current_index: current_index + size])
                            current_index += size
                            cards.append(card)
                        entity_data['hand_cards'][1] = cards
                    else:
                        if entity_data[i][0] == "INT32":
                            if len(need_parse_data) - current_index < 4:
                                break
                            entity_data[i] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4


            elif protocol_num == 6036:
                cards = []
                for i in entity_data:
                    if i == "zhaMa_card":
                        if entity_data["zhaMa_num"] is not 0:
                            for x in range(entity_data["zhaMa_num"]):
                                size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4
                                card = self.read_string(size, need_parse_data[current_index: current_index + size])
                                current_index += size
                                cards.append(card)
                            entity_data['zhaMa_card'] = cards

                    elif i == "zhongMa_players_info":
                        info_list = []
                        info_dict = {}
                        users_num = {}
                        if entity_data["zhongMa_players_num"] is not 0:
                            for x in range(entity_data["zhongMa_players_num"]):
                                seat_ID = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4

                                zhongMa_num = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4
                                card_list = []
                                if zhongMa_num is not 0:
                                    for z in range(zhongMa_num):
                                        card_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                        current_index += 4
                                        card = self.read_string(card_len,
                                                                need_parse_data[
                                                                current_index: current_index + card_len])
                                        current_index += card_len
                                        card_list.append(card)
                                info_dict["seat_ID"] = seat_ID
                                info_dict["zhongMa_num"] = zhongMa_num
                                info_dict["zhongMa_card"] = card_list
                                users_num["%s" % i] = info_dict
                            info_list.append(users_num)

                        entity_data["zhongMa_players_info"] = info_list

                    else:
                        if entity_data[i][0] == "INT32":
                            if len(need_parse_data) - current_index < 4:
                                break
                            entity_data[i] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4


            elif protocol_num == 6026:
                cards = []
                for i in entity_data:
                    if i == "operate_type_info":
                        for x in range(entity_data["operate_type_num"]):
                            OperationTypeID = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            cards.append(OperationTypeID)
                        entity_data['operate_type_info'][1] = cards
                    else:
                        if entity_data[i][0] == "INT32":
                            if len(need_parse_data) - current_index < 4:
                                break
                            entity_data[i] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                        elif entity_data[i][0] == "STRING":
                            size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            entity_data[i] = self.read_string(size,
                                                              need_parse_data[current_index: current_index + size])
                            current_index += size


            elif protocol_num == 1011:  # 发牌
                range_num = 0
                for i in entity_data:
                    if entity_data[i][0] == "INT32":
                        if len(need_parse_data) - current_index < 4:
                            break
                        entity_data[i][1] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                        range_num = entity_data[i][1]
                        current_index += 4
                    else:
                        card_list = []
                        for j in range(range_num):
                            size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            card = self.read_string(size, need_parse_data[current_index: current_index + size])
                            card_list.append(card)
                            current_index += size
                        entity_data[i][1] = card_list

            elif protocol_num == 5008:
                for i in entity_data:
                    if i == "error_code":
                        err = self.read_int32(need_parse_data[0: (4)])
                        entity_data[i][1] = err

            elif protocol_num == 5022:
                custom_list = []
                for i in entity_data:
                    if i == "Operation_num":
                        operation_num = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                        current_index += 4
                        entity_data[i][1] = operation_num


                    elif i == "Operation_info":
                        for x in range(entity_data["Operation_num"][1]):
                            operation_id = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            custom_list.append(operation_id)
                        entity_data[i][1] = custom_list

                    else:
                        if entity_data[i][0] == "INT32":
                            if len(need_parse_data) - current_index < 4:
                                break
                            entity_data[i] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                        elif entity_data[i][0] == "STRING":
                            size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            entity_data[i] = self.read_string(size,
                                                                 need_parse_data[current_index: current_index + size])
                            current_index += size



            elif protocol_num == 5020:  # 跑得快发牌
                range_num = 0
                for i in entity_data:
                    if i == "card_num":
                        if entity_data[i][0] == "INT32":
                            if len(need_parse_data) - current_index < 4:
                                break
                            entity_data[i][1] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            range_num = entity_data[i][1]
                            current_index += 4


                    elif i == "card_lists":
                        card_list = []
                        for j in range(range_num):
                            size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            card = self.read_string(size, need_parse_data[current_index: current_index + size])
                            card_list.append(card)
                            current_index += size
                        entity_data[i][1] = card_list


                    elif i == "banker_id":
                        bankerID = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                        current_index += 4
                        entity_data[i][1] = bankerID



            elif protocol_num == 1012:  # 请求操作返回
                # print("1012: %s" % data)
                for i in entity_data:
                    if entity_data["card_num"][1] != 0:
                        if i == "_card":
                            card_list = []
                            for x in range(entity_data["card_num"][1]):
                                size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4
                                card = self.read_string(size, need_parse_data[current_index: current_index + size])
                                card_list.append(card)
                                current_index += size
                            entity_data['_card'][1] = card_list

                    if i == "_player":
                        player_list = {}
                        if entity_data["player_num"][1] == 0:
                            break
                        for j in range(entity_data["player_num"][1]):
                            seat_id = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            fen_shu = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            zong_fen = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            key_1 = "seat_id_%s" % j
                            key_2 = "fen_shu_%s" % j
                            key_3 = "zong_fen_%s" % j

                            player_list[key_1] = seat_id
                            player_list[key_2] = fen_shu
                            player_list[key_3] = zong_fen
                        entity_data[i][1] = player_list

                    if entity_data[i][0] == "INT32":
                        if len(need_parse_data) - current_index < 4:
                            break
                        entity_data[i][1] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                        if i == 'error_code':
                            if entity_data[i][1] == -20:
                                break
                        current_index += 4

            elif protocol_num == 1015:  # 总结算(积分结算)
                player_num = 0
                for i in entity_data:
                    if entity_data[i][0] == "INT32":
                        if len(need_parse_data) - current_index < 4:
                            break

                        if i == '_players_info':
                            num = entity_data['players'][1]
                            player_num = num
                            if num == 0:
                                break
                            info_data = {}
                            for j in range(num):
                                seat_id = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4

                                room_total_socre = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4

                                win_socre = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4

                                key_1 = "seat_id_%s" % j
                                key_2 = "room_total_socre_%s" % j
                                key_3 = "win_socre_%s" % j

                                info_data[key_1] = seat_id
                                info_data[key_2] = room_total_socre
                                info_data[key_3] = win_socre

                            entity_data[i][1] = info_data

                        elif i == "_players_num_info":
                            num = entity_data['players_num'][1]
                            if num == 0:
                                break

                            info_data = {}
                            for n in range(num):
                                if len(need_parse_data) - current_index < 4:
                                    break
                                seat_id = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4

                                if len(need_parse_data) - current_index < 4:
                                    break
                                hupai_num = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4

                                if len(need_parse_data) - current_index < 4:
                                    break
                                zimo_num = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4

                                if len(need_parse_data) - current_index < 4:
                                    break
                                dianpao_num = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4

                                if len(need_parse_data) - current_index < 4:
                                    break
                                tipai_num = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4

                                if len(need_parse_data) - current_index < 4:
                                    break
                                paopai_num = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4

                                key_1 = "seat_id_%s" % n
                                key_2 = "hupai_num_%s" % n
                                key_3 = "zimo_num_%s" % n
                                key_4 = "dianpao_num_%s" % n
                                key_5 = "tipai_num_%s" % n
                                key_6 = "paopai_num_%s" % n

                                info_data[key_1] = seat_id
                                info_data[key_2] = hupai_num
                                info_data[key_3] = zimo_num
                                info_data[key_4] = dianpao_num
                                info_data[key_5] = tipai_num
                                info_data[key_6] = paopai_num
                            entity_data[i][1] = info_data

                        elif i == "_players_num_info":
                            num = entity_data['players_number'][1]
                            if num == 0:
                                break
                            info_data = {}
                            for m in range(num):
                                seat_id = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4

                                tips_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4

                                tips = self.read_string(tips_len,
                                                        need_parse_data[current_index: current_index + tips_len])
                                current_index += tips_len

                                key_1 = "seat_id_%s" % m
                                key_2 = "tips_%s" % m

                                info_data[key_1] = seat_id
                                info_data[key_2] = tips
                            entity_data[i][1] = info_data

                        elif i == "_dissolve_info_list":
                            result = entity_data['dissolve_info'][1]
                            if result != 2 and result != 32:
                                break
                            info_data = {}
                            for x in range(player_num):
                                seat_id = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4

                                dissolve_state = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4

                                key_1 = "seat_id_%s" % x
                                key_2 = "dissolve_state_%s" % x

                                info_data[key_1] = seat_id
                                info_data[key_2] = dissolve_state
                            entity_data[i][1] = info_data

                        else:
                            entity_data[i][1] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

            elif protocol_num == 1093:      # 少人模式
                for i in entity_data:
                    if i == "PlayerInfo":
                        num = entity_data['PlayerNum']
                        if num == 0: break

                        player_info = {}
                        for j in range(num):
                            player_info[j] = {}
                            for info, _list in entity_data['PlayerInfo'][1].items():
                                if _list[0] == "INT32":
                                    player_info[j][info] = self.read_int32(
                                        need_parse_data[current_index: (current_index + 4)])
                                    current_index += 4

                                elif _list[0] == "INT64":
                                    player_info[j][info] = self.read_int64(
                                        need_parse_data[current_index: (current_index + 8)])
                                    current_index += 8

                                else:
                                    size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                    current_index += 4

                                    player_info[j][info] = self.read_string(size,
                                                                            need_parse_data[
                                                                            current_index: current_index + size])
                                    current_index += size

                        entity_data[i] = player_info

                    else:
                        if entity_data[i][0] == "INT32":
                            if len(need_parse_data) - current_index < 4:
                                break
                            entity_data[i] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                        elif entity_data[i][0] == "STRING":
                            size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            entity_data[i] = self.read_string(size,
                                                                 need_parse_data[current_index: current_index + size])
                            current_index += size


            elif protocol_num == 1094:  # 少人模式开启
                for i in entity_data:
                    if i == "OpenInfo":
                        num = entity_data['OpenNum']
                        if num == 0: break
                        open_info = {}
                        for j in range(num):
                            seat_id = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            state = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            open_info[j + 1] = {"SeatID": seat_id, "State": state}

                        entity_data[i] = open_info

                    else:
                        if entity_data[i][0] == "INT32":
                            if len(need_parse_data) - current_index < 4:
                                break
                            entity_data[i] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                        elif entity_data[i][0] == "STRING":
                            size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            entity_data[i] = self.read_string(size,
                                                              need_parse_data[current_index: current_index + size])
                            current_index += size

            elif protocol_num == 1018:  # 解散房间
                for i in entity_data:
                    if i == '_seat_id':
                        seat_id_list = []
                        for j in range(entity_data['agree_player'][1]):
                            seat_id = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            seat_id_list.append(seat_id)

                        entity_data[i][1] = seat_id_list

                    else:
                        if entity_data[i][0] == "INT32":
                            if len(need_parse_data) - current_index < 4:
                                break
                            entity_data[i][1] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            if i == 'error_code':
                                if entity_data[i][1] == -20:
                                    break
                            current_index += 4

                        elif entity_data[i][0] == "STRING":
                            size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            entity_data[i][1] = self.read_string(size,
                                                                 need_parse_data[current_index: current_index + size])
                            current_index += size


            elif protocol_num == 1026:  # 广播结算
                for i in entity_data:
                    if i == "PlayerInfo":
                        num = entity_data['PlayerNum']
                        player_info = {}
                        for j in range(num):
                            player_info[j] = {}
                            for info, _list in entity_data['PlayerInfo'][1].items():
                                if _list[0] == "INT32":
                                    player_info[j][info] = self.read_int32(
                                        need_parse_data[current_index: (current_index + 4)])
                                    current_index += 4

                                elif _list[0] == "INT64":
                                    player_info[j][info] = self.read_int64(
                                        need_parse_data[current_index: (current_index + 8)])
                                    current_index += 8

                                else:
                                    size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                    current_index += 4

                                    player_info[j][info] = self.read_string(size, need_parse_data[current_index: current_index + size])
                                    current_index += size

                        entity_data[i] = player_info

                    elif i == "WangBaValue":
                        num = entity_data['WangBaNum']
                        value_list = []
                        for j in range(num):
                            size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            value = self.read_string(size, need_parse_data[
                                                                          current_index: current_index + size])
                            current_index += size

                            value_list.append(value)

                        entity_data[i] = value_list


                    elif i == "TypeInfo":
                        num = entity_data['TotalTypeNum']
                        type_info = {}
                        for j in range(num):
                            if j not in type_info:
                                type_info[j] = {}
                            _type = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            score = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            type_info[j] = {'Type': _type, "Score": score}

                        entity_data[i] = type_info


                    elif i == "RemainCards":
                        num = entity_data['RemainNum']
                        card_list = []
                        for j in range(num):
                            size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            card = self.read_string(size, need_parse_data[
                                                           current_index: current_index + size])
                            current_index += size

                            card_list.append(card)

                        entity_data[i] = card_list


                    elif i == "OnlineInfo":
                        num = entity_data['OnlinePlayerNum']
                        player_info = {}
                        for j in range(num):
                            player_info[j] = {}
                            seat_id = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            card_num = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            card_list = []
                            for z in range(card_num):
                                size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4

                                card = self.read_string(size, need_parse_data[
                                                              current_index: current_index + size])
                                current_index += size

                                card_list.append(card)

                            player_info[j] = {"SeatID": seat_id, "CardNum": card_num, "Cards": card_list}

                        entity_data[i] = player_info

                    elif i == "CardTypeInfo":
                        num = entity_data['CardTypeNum']
                        player_info = {}
                        for j in range(num):
                            player_info[j] = {}
                            card_type = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            huxi = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            card_num = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            card_list = []
                            for z in range(card_num):
                                size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4

                                card = self.read_string(size, need_parse_data[
                                                              current_index: current_index + size])
                                current_index += size

                                card_list.append(card)

                            player_info[j] = {"CardType": card_type, "Huxi": huxi, "CardNum": card_num, "Cards": card_list}

                        entity_data[i] = player_info

                    elif i == "TiInfo":
                        num = entity_data['TiNum']
                        player_info = {}
                        for j in range(num):
                            seat_id = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            ti_num = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            ti_card_list = []
                            for z in range(ti_num):
                                size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4

                                card = self.read_string(size, need_parse_data[
                                                              current_index: current_index + size])
                                current_index += size

                                ti_card_list.append(card)

                                player_info[j] = {"SeatID": seat_id, "Num": ti_num, "Cards": ti_card_list}

                        entity_data[i] = player_info

                    else:
                        if entity_data[i][0] == "INT32":
                            if len(need_parse_data) - current_index < 4:
                                break
                            entity_data[i] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                        elif entity_data[i][0] == "INT64":
                            if len(need_parse_data) - current_index < 4:
                                break
                            entity_data[i] = self.read_int64(need_parse_data[current_index: (current_index + 8)])
                            current_index += 8

                        else:
                            size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            entity_data[i] = self.read_string(size, need_parse_data[current_index: current_index + size])
                            current_index += size



            elif protocol_num == 1028:  # 经纬度
                for i in entity_data:
                    if i == "players_info":
                        num = entity_data['players'][1]
                        if num == 0:
                            break
                        info_data = {}
                        for k in range(num):
                            seat_id = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            jingweidu_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            jingweidu = self.read_string(jingweidu_len,
                                                         need_parse_data[current_index: current_index + jingweidu_len])
                            current_index += jingweidu_len

                            key_1 = "seat_id_%s" % k
                            key_2 = "jingweidu_%s" % k

                            info_data[key_1] = seat_id
                            info_data[key_2] = jingweidu
                        entity_data[i][1] = info_data
                    else:
                        if len(need_parse_data) - current_index < 4:
                            break
                        entity_data[i][1] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                        current_index += 4

            elif protocol_num == 1100:  # 已创建的比赛
                for i in entity_data:
                    if i == "list_info":
                        num = entity_data['list_num'][1]
                        if num == 0:
                            break
                        info_data = {}
                        for k in range(num):
                            game_index = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            club_id = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            club_name_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            club_name = self.read_string(club_name_len,
                                                         need_parse_data[current_index: current_index + club_name_len])
                            current_index += club_name_len

                            room_type_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            room_type = self.read_string(room_type_len,
                                                         need_parse_data[current_index: current_index + room_type_len])
                            current_index += room_type_len

                            wanfa = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            difen = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            room_players = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            total_players = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            real_players = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            rounds_num = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            innings = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            format = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            state = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            distance_close_time = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            uuid_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            uuid = self.read_string(uuid_len, need_parse_data[current_index: current_index + uuid_len])
                            current_index += uuid_len

                            key_1 = "game_index_%s" % k
                            key_2 = "club_id_%s" % k
                            key_3 = "club_name_%s" % k
                            key_4 = "room_type_%s" % k
                            key_5 = "wanfa_%s" % k
                            key_6 = "difen_%s" % k
                            key_7 = "room_players_%s" % k
                            key_8 = "total_players_%s" % k
                            key_9 = "real_players_%s" % k
                            key_10 = "rounds_num_%s" % k
                            key_11 = "innings_%s" % k
                            key_12 = "format_%s" % k
                            key_13 = "state_%s" % k
                            key_14 = "distance_close_time_%s" % k
                            key_15 = "uuid_%s" % k

                            info_data[key_1] = game_index
                            info_data[key_2] = club_id
                            info_data[key_3] = club_name
                            info_data[key_4] = room_type
                            info_data[key_5] = wanfa
                            info_data[key_6] = difen
                            info_data[key_7] = room_players
                            info_data[key_8] = total_players
                            info_data[key_9] = real_players
                            info_data[key_10] = rounds_num
                            info_data[key_11] = innings
                            info_data[key_12] = format
                            info_data[key_13] = state
                            info_data[key_14] = distance_close_time
                            info_data[key_15] = uuid
                        entity_data[i][1] = info_data

                    else:
                        if len(need_parse_data) - current_index < 4:
                            break
                        entity_data[i][1] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                        current_index += 4

            elif protocol_num == 1101:  # 所在俱乐部比赛
                for i in entity_data:
                    if i == "list_info":
                        num = entity_data['list_num'][1]
                        if num == 0:
                            break
                        info_data = {}
                        for k in range(num):
                            club_icon_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            club_icon = self.read_string(club_icon_len,
                                                         need_parse_data[current_index: current_index + club_icon_len])
                            current_index += club_icon_len

                            club_name_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            club_name = self.read_string(club_name_len,
                                                         need_parse_data[current_index: current_index + club_name_len])
                            current_index += club_name_len

                            club_id = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            game_index = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            room_type_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            room_type = self.read_string(room_type_len,
                                                         need_parse_data[current_index: current_index + room_type_len])
                            current_index += room_type_len

                            wanfa = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            difen = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            room_players = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            total_players = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            real_players = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            rounds_num = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            innings = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            format = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            state = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            distance_close_time = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            uuid_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            uuid = self.read_string(uuid_len, need_parse_data[current_index: current_index + uuid_len])
                            current_index += uuid_len

                            key_1 = "club_icon_%s" % k
                            key_2 = "club_name_%s" % k
                            key_3 = "club_id_%s" % k
                            key_4 = "game_index_%s" % k
                            key_5 = "room_type_%s" % k
                            key_6 = "wanfa_%s" % k
                            key_7 = "difen_%s" % k
                            key_8 = "room_players_%s" % k
                            key_9 = "total_players_%s" % k
                            key_10 = "real_players_%s" % k
                            key_11 = "rounds_num_%s" % k
                            key_12 = "innings_%s" % k
                            key_13 = "format_%s" % k
                            key_14 = "state_%s" % k
                            key_15 = "distance_close_time_%s" % k
                            key_16 = "uuid_%s" % k

                            info_data[key_1] = club_icon
                            info_data[key_2] = club_name
                            info_data[key_3] = club_id
                            info_data[key_4] = game_index
                            info_data[key_5] = room_type
                            info_data[key_6] = wanfa
                            info_data[key_7] = difen
                            info_data[key_8] = room_players
                            info_data[key_9] = total_players
                            info_data[key_10] = real_players
                            info_data[key_11] = rounds_num
                            info_data[key_12] = innings
                            info_data[key_13] = format
                            info_data[key_14] = state
                            info_data[key_15] = distance_close_time
                            info_data[key_16] = uuid
                        entity_data[i][1] = info_data

                    else:
                        if len(need_parse_data) - current_index < 4:
                            break
                        entity_data[i][1] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                        current_index += 4

            elif protocol_num == 2025:  # 岳阳的小局结算
                for i in entity_data:
                    if i == 'RemainCards':
                        num = entity_data['RemainCardNum'][1]
                        if num == 0:
                            break
                        Cards = ''
                        for k in range(num):
                            size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            cards_data = self.read_string(size, need_parse_data[current_index: current_index + size])
                            current_index += size

                            Cards += cards_data

                        entity_data[i][1] = Cards
                    elif i == 'AllPlayerInfo':
                        num = entity_data['AllPlayerNum'][1]
                        if num == 0:
                            break
                        info_data = {}
                        for j in range(num):
                            PlayerSeatId = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            PlayerRemainCard = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            Cards = ""
                            if PlayerRemainCard != 0:
                                for k in range(PlayerRemainCard):
                                    size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                    current_index += 4

                                    cards_data = self.read_string(size,
                                                                  need_parse_data[current_index: current_index + size])
                                    current_index += size

                                    Cards += cards_data

                            key_1 = "PlayerSeatId_%s" % j
                            key_2 = "PlayerRemainCard_%s" % j
                            key_3 = "Cards_%s" % j

                            info_data[key_1] = PlayerSeatId
                            info_data[key_2] = PlayerRemainCard
                            info_data[key_3] = Cards

                        entity_data[i][1] = info_data

                    elif i == "ShapeNumInfo":
                        num = entity_data['ShapeTpyeNum'][1]
                        if num == 0:
                            break
                        info_data = {}
                        for j in range(num):
                            CardTpye = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            Huxi = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            CardNum = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            Cards = ""
                            if CardNum != 0:
                                for k in range(CardNum):
                                    size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                    current_index += 4

                                    cards_data = self.read_string(size, need_parse_data[current_index: current_index + size])
                                    current_index += size

                                    Cards += cards_data

                            key_1 = 'CardTpye_%s' % j
                            key_2 = 'Huxi_%s' % j
                            key_3 = 'CardNum_%s' % j
                            key_4 = 'Cards_%s' % j

                            info_data[key_1] = CardTpye
                            info_data[key_2] = Huxi
                            info_data[key_3] = CardNum
                            info_data[key_4] = Cards
                        entity_data[i][1] = info_data

                    elif i == 'ReservedWords':
                        if len(need_parse_data) - current_index < 2:
                            break
                        entity_data[i][1] = self.read_int16(need_parse_data[current_index: (current_index + 2)])
                        current_index += 2
                    elif i == "BonusNumInfo":
                        num = entity_data['BonusTpyeNum'][1]
                        if num == 0:
                            break
                        info_data = {}
                        for j in range(num):
                            Tpye = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            HuTpye = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            key_1 = 'Tpye_%s' % j
                            key_2 = 'HuTpye_%s' % j

                            info_data[key_1] = Tpye
                            info_data[key_2] = HuTpye

                        entity_data[i][1] = info_data
                    else:
                        if entity_data[i][0] == "INT32":
                            if len(need_parse_data) - current_index < 4:
                                break
                            entity_data[i][1] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                        else:
                            size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            if len(need_parse_data[current_index: current_index + size]) < 1:
                                break

                            # print("剩余字符2222", need_parse_data[current_index: current_index + size])
                            entity_data[i][1] = self.read_string(size,
                                                                 need_parse_data[current_index: current_index + size])
                            current_index += size

            elif protocol_num == 2028:
                for i in entity_data:
                    if i == 'ReservedWords':
                        if len(need_parse_data) - current_index < 2:
                            break
                        entity_data[i][1] = self.read_int16(need_parse_data[current_index: (current_index + 2)])
                        current_index += 2

                    elif i == 'PlayerInfo':
                        num = entity_data['PlayerNum'][1]
                        if num == 0:
                            break
                        info_data = {}
                        for j in range(num):
                            SeatID = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            RoomIntegral = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            WinIntegral = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            NameLen = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            Name = self.read_string(NameLen, need_parse_data[current_index: current_index + NameLen])
                            current_index += NameLen

                            Mid = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            IconLen = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            Icon = self.read_string(IconLen, need_parse_data[current_index: current_index + IconLen])
                            current_index += IconLen

                            key_1 = 'SeatID_%s' % j
                            key_2 = 'RoomIntegral_%s' % j
                            key_3 = 'WinIntegral_%s' % j
                            key_4 = 'Name_%s' % j
                            key_5 = 'Mid_%s' % j
                            key_6 = 'Icon_%s' % j

                            info_data[key_1] = SeatID
                            info_data[key_2] = RoomIntegral
                            info_data[key_3] = WinIntegral
                            info_data[key_4] = Name
                            info_data[key_5] = Mid
                            info_data[key_6] = Icon

                        entity_data[i][1] = info_data

                    elif i == 'PlayerMsg':
                        num = entity_data['PlayerCount'][1]
                        if num == 0:
                            break
                        info_data = {}
                        for j in range(num):
                            SeatID = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            HuCount = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            ZiMoCount = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            LiuCount = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            WaiCount = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            key_1 = 'SeatID_%s' % j
                            key_2 = 'HuCount_%s' % j
                            key_3 = 'ZiMoCount_%s' % j
                            key_4 = 'LiuCount_%s' % j
                            key_5 = 'WaiCount_%s' % j

                            info_data[key_1] = SeatID
                            info_data[key_2] = HuCount
                            info_data[key_3] = ZiMoCount
                            info_data[key_4] = LiuCount
                            info_data[key_5] = WaiCount

                        entity_data[i][1] = info_data

                    elif i == 'DissolveInfo':
                        num = entity_data['PlayerCount'][1]
                        if num != 4 or num != 32:
                            break

                        info_data = {}
                        for j in range(num):
                            SeatID = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            Operate = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            key_1 = 'SeatID_%s' % j
                            key_2 = 'Operate_%s' % j

                            info_data[key_1] = SeatID
                            info_data[key_2] = Operate

                        entity_data[i][1] = info_data

                    else:
                        if entity_data[i][0] == "INT32":
                            if len(need_parse_data) - current_index < 4:
                                break
                            entity_data[i][1] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                        else:
                            size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            if len(need_parse_data[current_index: current_index + size]) < 1:
                                break

                            # print("剩余字符2222", need_parse_data[current_index: current_index + size])
                            entity_data[i][1] = self.read_string(size,
                                                                 need_parse_data[current_index: current_index + size])
                            current_index += size

            elif protocol_num == 2030:
                for i in entity_data:
                    if entity_data[i][0] == "INT32":
                        if len(need_parse_data) - current_index < 4:
                            break
                        entity_data[i][1] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                        current_index += 4
                    else:
                        num = entity_data['card_num'][1]
                        if num == 0:
                            break

                        Cards = []
                        if num != 0:
                            for k in range(num):
                                size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                current_index += 4

                                cards_data = self.read_string(size,
                                                              need_parse_data[current_index: current_index + size])
                                current_index += size

                                Cards.append(cards_data)

                        entity_data[i][1] = Cards


        self.result = entity_data
        return entity_data
