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
from .protocol import *

class DefineProtocol:
    """
        客户端发包CS
    """
    PAO_HU_ZI_CS_LOGIN = 1000  # 登录
    PAO_HU_ZI_CS_REQUEST_ENTER_ROOM = 1001  # 请求进入房间
    PAO_HU_ZI_CS_LEAVE_ROOM = 1004  # 离开房间
    PAO_HU_ZI_CS_REQUEST_READY = 1005  # 请求准备
    PAO_HU_ZI_CS_REQUEST_QUERY_PLAYER_ROOM_INFO = 1009  # 请求玩家房间及玩家信息
    PAO_HU_ZI_CS_CREATE_ROOM = 1010  # 创建房间
    PAO_HU_ZI_CS_REQUEST_FUNCTION = 1012  # 请求操作
    PAO_HU_ZI_CS_DISSOLVE_ROOM = 1008  # 解散房间
    PAO_HU_ZI_CS_CHOSE_DISSOLVE_ROOM = 1012  # 选择解散房间
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
    PAO_HU_ZI_SC_LEAVE_ROOM = 1009  # 离开房间
    PAO_HU_ZI_SC_ENTER_ROOM_PLAYER_INFO = 1004  # 通知进入房间玩家信息
    PAO_HU_ZI_SC_REQUEST_READY = 1005  # 请求准备
    PAO_HU_ZI_SC_GAME_START = 1007  # 游戏开始
    PAO_HU_ZI_SC_CREATE_ROOM = 1010  # 创建房间
    PAO_HU_ZI_SC_SEND_CARDS = 1020  # 发牌
    PAO_HU_ZI_SC_BROADCASTBAOCARDS = 1075  # 服务器广播宝牌
    PAO_HU_ZI_SC_TOUCH_CARDS = 1028  # 摸牌
    PAO_HU_ZI_SC_WHICH_PLAYER_CAN_DO = 1022  # 服务器通知用户做相应的操作
    PAO_HU_ZI_SC_TOTAL_SETTLEMENT = 1015  # 总结算
    PAO_HU_ZI_SC_PLAY_GAME_TIMES = 1017  # 广播当前已玩的局数
    PAO_HU_ZI_SC_DISSOLVE_ROOM = 1008  # 发起解散房间
    PAO_HU_ZI_SC_STEP_OUT_ROOM = 1019  # 暂离房间
    PAO_HU_ZI_SC_DISSOLVE_ROOMACK = 1012  # 玩家解散房间投票Ack
    PAO_HU_ZI_SC_DISSOLVE_ROOMEND = 1013  # 正式解散房间
    PAO_HU_ZI_SC_SETTLEMENT = 1031  # 小局结算
    PAO_HU_ZI_SC_ERROR_TIPS = 1027  # 错误提示
    PAO_HU_ZI_SC_RECONNECTION_SERVER_SEND_CARDS = 1035  # 断线重连后服务器推自己手上的牌
    # PAO_HU_ZI_SC_MAKE_CARDS_TYPE = 1057  # 测试专用做牌
    # PAO_HU_ZI_SC_SERVER_CLOSE = 1998  # 服务器即将关闭
    # PAO_HU_ZI_SC_RECONNECTION = 1999  # 断线重连


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
                                       DefineProtocol.PAO_HU_ZI_SC_DISSOLVE_ROOMACK: [SCChoseDissolveRoom,
                                                                                      "OnVoteDissolveRoom"],
                                       DefineProtocol.PAO_HU_ZI_SC_DISSOLVE_ROOMEND: [SCChoseDissolveRoomEnd,
                                                                                      "OnVoteDissolveRoomEnd"],
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
                                       DefineProtocol.PAO_HU_ZI_SC_BROADCASTBAOCARDS: [SCBaoCards, "OnRecvBaoCards"],
                                       DefineProtocol.PAO_HU_ZI_SC_TOUCH_CARDS: [SCTouchCards, "OnTouchCard"],
                                       DefineProtocol.PAO_HU_ZI_SC_WHICH_PLAYER_CAN_DO: [SCPlayerCanDo,
                                                                                         "OnPlayerCanDo"],
                                       # DefineProtocol.PAO_HU_ZI_SC_REQUEST_FUNCTION: [SCRequestFunction,
                                       #                                                "OnPlayerOperate"],
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
                                       # DefineProtocol.PAO_HU_ZI_SC_JINGWEIDU: [SCJingWeiDu, "sc_jingweidu"],
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

                                       1093: [SCInformLessMode, "OnInformLessMode"],
                                       1094: [SCOpenLessMode, "OnOpenLessMode"],
                                       }


class UnPackData:
    #   初始化协议号及包体数据
    def __init__(self):
        self.current_index = 0
        self.result = None
        self.normal_entity_list = [1000, 1001, 1004, 1005, 1006, 1008, 1010, 1013, 1014, 1016, 1017, 1019, 1035,
                                   1042, 1043, 1053, 1047, 1057, 1086, 1998, 1999, 2001, 2002, 2009, 2010, 2026, 2027,
                                   2029, 3035, 3040, 10022, 10080, 12026, 2030]

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
            if protocol_num == 1002:  # 房间快照
                for i in entity_data:
                    if i == "players_info":
                        num = entity_data['players_num'][1]
                        if num == 0:
                            break
                        info_data = {}
                        for k in range(num):
                            seat_no = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            ip_addr_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            ip_addr = self.read_string(ip_addr_len, need_parse_data[current_index: current_index + ip_addr_len])
                            current_index += ip_addr_len

                            mid = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            gp = self.read_int32(need_parse_data[current_index: (current_index + 4)])
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

                            city_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            city = self.read_string(city_len, need_parse_data[current_index: current_index + city_len])
                            current_index += city_len

                            json_str_len = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            json_str = self.read_string(json_str_len, need_parse_data[current_index: current_index + json_str_len])
                            current_index += json_str_len

                            key_1 = "seat_no_%s" % k
                            key_2 = "ip_addr_%s" % k
                            key_3 = "mid_%s" % k
                            key_4 = "gp_%s" % k
                            key_5 = "sex_%s" % k
                            key_6 = "name_%s" % k
                            key_7 = "icon_%s" % k
                            key_8 = "city_%s" % k
                            key_9 = "json_str_%s" % k

                            info_data[key_1] = seat_no
                            info_data[key_2] = ip_addr
                            info_data[key_3] = mid
                            info_data[key_4] = gp
                            info_data[key_5] = sex
                            info_data[key_6] = name
                            info_data[key_7] = icon
                            info_data[key_8] = city
                            info_data[key_9] = json_str
                        entity_data[i][1] = info_data
                    else:
                        if len(need_parse_data) - current_index < 4:
                            break
                        if entity_data[i][0] == "INT32":
                            entity_data[i][1] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                        else:
                            size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            entity_data[i][1] = self.read_string(size, need_parse_data[current_index: current_index + size])
                            current_index += size
            elif protocol_num == 1020:  # 发牌
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
            elif protocol_num == 1075:  # 服务器广播宝牌
                range_num = 0
                for i in entity_data:
                    if entity_data[i][0] == "INT32":
                        if len(need_parse_data) - current_index < 4:
                            break
                        entity_data[i][1] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                        range_num = entity_data[i][1]
                        current_index += 4
                    else:
                        bao_cards = []
                        for j in range(range_num):
                            size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4

                            card = self.read_string(size, need_parse_data[current_index: current_index + size])
                            bao_cards.append(card)
                            current_index += size
                        entity_data[i][1] = bao_cards
            elif protocol_num == 1022:  # 服务器通知用户做相应的操作
                for i in entity_data:
                    if i == "opeate":
                        num = entity_data['opeate_size'][1]
                        if num == 0:
                            break
                        opeates = []
                        for k in range(num):
                            opeate = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            opeates.append(opeate)
                        entity_data[i][1] = opeates
                    else:
                        if len(need_parse_data) - current_index < 4:
                            break
                        if entity_data[i][0] == "INT32":
                            entity_data[i][1] = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                        else:
                            size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                            current_index += 4
                            entity_data[i][1] = self.read_string(size,
                                                                 need_parse_data[current_index: current_index + size])
                            current_index += size
            elif protocol_num == 1031:  # 服务器广播小结算
                for i in entity_data:
                    if i == "seats_info":
                        num = entity_data['players_num']
                        seats_info = {}
                        for j in range(num):
                            seats_info[j] = {}
                            for key, values in entity_data['seats_info'][1].items():
                                if key == "op_cardinfo":
                                    operated_cards_size = entity_data['seats_info'][1]["operated_cards_size"][1]
                                    op_cardinfo = {}
                                    for m in range(operated_cards_size):
                                        if values[0] == "INT32":
                                            op_cardinfo[m][1] = self.read_int32(
                                                need_parse_data[current_index: (current_index + 4)])
                                            current_index += 4
                                        else:
                                            size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                            current_index += 4
                                            op_cardinfo[m][1] = self.read_string(size, need_parse_data[
                                                                                 current_index: current_index + size])
                                            current_index += size
                                    seats_info[j][key] = op_cardinfo
                                elif key == "card":
                                    handcards_size = entity_data['seats_info'][1]["handcards_size"][1]
                                    cards = {}
                                    for m in range(handcards_size):
                                        size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                        current_index += 4
                                        cards[m][1] = self.read_string(size, need_parse_data[
                                                                        current_index: current_index + size])
                                        current_index += size
                                    seats_info[j][key] = cards
                                elif key == "mingtang_infos":
                                    mingtang_info_num = entity_data['seats_info'][1]["mingtang_info_num"][1]
                                    mingtang_infos = {}
                                    for m in range(mingtang_info_num):
                                        if values[0] == "INT32":
                                            mingtang_infos[m][1] = self.read_int32(
                                                need_parse_data[current_index: (current_index + 4)])
                                            current_index += 4
                                        else:
                                            size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                            current_index += 4
                                            mingtang_infos[m][1] = self.read_string(size, need_parse_data[
                                                                                 current_index: current_index + size])
                                            current_index += size
                                    seats_info[j][key] = mingtang_infos
                                elif values[0] == "INT32":
                                    seats_info[j][key] = self.read_int32(
                                        need_parse_data[current_index: (current_index + 4)])
                                    current_index += 4
                                elif values[0] == "INT64":
                                    seats_info[j][key] = self.read_int64(
                                        need_parse_data[current_index: (current_index + 8)])
                                    current_index += 8
                                else:
                                    size = self.read_int32(need_parse_data[current_index: (current_index + 4)])
                                    current_index += 4
                                    seats_info[j][key] = self.read_string(size, need_parse_data[current_index: current_index + size])
                                    current_index += size
                        entity_data[i] = seats_info
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
