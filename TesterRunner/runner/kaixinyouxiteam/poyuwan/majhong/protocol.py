#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@ author: Hubery
@ create on: 2018/10/9 16:56
@ file: protocol.py
@ site: 
@ purpose: all protocol structures
"""
from .pack import *


class Encrypt2ParseData:
    def __init__(self, update_data, method=None):
        self.update_data = update_data
        self.method = method

    #   Update protocol data and perform different processing of data according to requirements.
    def get_update_data(self):
        if self.method == "pack":
            return self.pack_data()
        elif self.method == "unpack":
            return self.unpack_data()
        else:
            return None

    #   pack data
    def pack_data(self):
        package = net_package(self.update_data["protocol_num"][1])

        if len(self.update_data) > 0:
            for k, v in self.update_data.items():
                if k != "protocol_num":
                    if v[0] == "INT32":
                        package.write_int32(v[1])
                    elif v[0] == "INT64":
                        package.write_int32(v[1])
                    elif v[0] == "INT16":
                        package.write_int16(v[1])
                    elif v[0] == "STRING":
                        if self.update_data["protocol_num"][1] == 1012:
                            if type(v[1]) == list:
                                for i in v[1]:
                                    # print(u"构造多张牌的数据: %s" % i)
                                    package.write_string(
                                        i[: len(i) - 1])  # print(u"数据组建：%s %s" % (package.int32data, package.data))
                            else:
                                # print(u"单张出牌操作数据: %s" % str(v[1]))
                                package.write_string(str(v[1]))
                        else:
                            package.write_string(str(v[1]))
        # print("package.encode: %s" % package.encode())
        return package.encode()

    #   unpack data
    def unpack_data(self):
        pass


#   Update protocol data.
class CommonUtils2UpdateData:
    def __init__(self, original_data, original_data_keys_list, update_data, method):
        self.original_data = original_data
        self.original_data_keys_list = original_data_keys_list
        self.data = update_data
        self.method = method

    def update_data(self):
        if len(self.data) > 0:
            for k, v in self.data.items():
                if k in self.original_data_keys_list:
                    self.original_data[k][1] = v

        # if self.original_data["protocol_num"][1] == 1012:
        # print("data: %s" % self.original_data)
        ud = Encrypt2ParseData(self.original_data, self.method)
        return ud.get_update_data()


#   common api to call update data
class CallUpdateApi:
    def __init__(self, original_data, original_data_keys_list, update_data, method):
        self.original_data = original_data
        self.original_data_keys_list = original_data_keys_list
        self.update_data = update_data
        self.method = method
        self.real_data = None
        self.get_real_data()

    def get_real_data(self):
        cu = CommonUtils2UpdateData(self.original_data, self.original_data_keys_list, self.update_data, self.method)
        self.real_data = cu.update_data()


#   login entity --> CS
class CSLogin:
    def __init__(self, data={}):
        self.cs_login_entity = {"protocol_num": ["INT32", 1000], "mid": ["INT32", 0], "no_used": ["STRING", ""],
                                "gp": ["INT32", 0], "game_type": ["INT32", 0], "resource": ["INT32", 0]}
        self.cs_keys_list = self.cs_login_entity.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_login_entity, self.cs_keys_list, self.update_data, self.method).real_data


#   login entity --> SC
class SCLogin:
    def __init__(self, data={}):
        self.sc_entity_data = {"err": ["INT32", 0]}
        self.sc_login_keys_list = self.sc_entity_data.keys()
        self.update_data = data
        self.method = "unpack"

#   gold coins change entity --> SC
class SCGoldCoinsChange:
    def __init__(self):
        self.sc_entity_data = {}


class SCReconnection:
    def __init__(self):
        self.sc_entity_data = {"gamestatus": ["INT32", 0], "room_id": ["INT32", 0], "server_id": ["INT32", 0]}


class SCChangeServer:
    def __init__(self):
        self.sc_entity_data = {}


#   create room entity -->CS
class CSCreateRoom:
    def __init__(self, data={}):
        self.cs_create_room_entity = {"protocol_num": ["INT32", 1010], "type": ["STRING", ""],
                                      "ju": ["INT32", 0], "players": ["INT32", 0], "play_type": ["INT32", 0],
                                      "operation": ["INT32", 0], "zhuaniao": ["INT32", 0],
                                      "gameFanXing": ["INT32", 0], "gameLianZhuang": ["INT32", 0],
                                      "isproxy": ["INT32", 0], "piaofen_operation": ["INT32", 0],
                                      "iJulebu_id": ["INT32", 0], "hongzhong_num": ["INT32", 0],
                                      "aa_kaifang": ["INT32", 0], "club_name": ["STRING", ""],
                                      "create_empty_room": ["INT32", 0],
                                      "password": ["INT32", 0], "fang_zuobi": ["INT32", 0],
                                      "all_agree_diss": ["INT32", 0], "wanfa_index": ["INT32", 0],
                                      "club_pay": ["INT32", 0], "shouju_zuozhuang": ["INT32", 0],
                                      "json_str": ["STRING", ""]}
        self.cs_keys_list = self.cs_create_room_entity.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_create_room_entity, self.cs_keys_list, self.update_data,
                                       self.method).real_data


#   create room -->SC
class SCCreateRoom:
    def __init__(self, data={}):
        self.sc_entity_data = {"wanfa_type": ["INT32", 1],  # 服务器固定传1表示麻将
                               "err": ["INT32", 0],
                               "roomid": ["INT32", 0]}
        self.sc_login_keys_list = self.sc_entity_data.keys()
        self.update_data = data
        self.method = "unpack"


class CSCreateRoomLeiYang:
    def __init__(self, data={}):
        self.cs_create_room_leiyang_entity = {"protocol_num": ["INT32", 1010], "gameRoomType": ["STRING", ""],
                                              "gameJuShu": ["INT32", 0], "gameFanShu": ["INT32", 0],
                                              "gameWanFa": ["INT32", 0], "gameJiaRuPaiJu": ["INT32", 0],
                                              "gamePlayer": ["INT32", 3], "gameFanXing": ["INT32", 0],
                                              "gameLianZhuang": ["INT32", 0], "gameDiFen": ["INT32", 0],
                                              "gameFengDing": ["INT32", 0], "gameZiMoFanBei": ["INT32", 0],
                                              "gameDianPaoBiHu": ["INT32", 2], "gameMaoHu": ["INT32", 0],
                                              "gameQiHu": ["INT32", 0], "gameHuYiDeng": ["INT32", 0],
                                              "gameBPLianZhuang": ["INT32", 0], "gameJiaTuo": ["INT32", 0],
                                              "gameYiWuShi": ["INT32", 0], "gameDaNiao": ["INT32", 0],
                                              "gameClubId": ["INT32", 0], "gameVip": ["INT32", 0],
                                              "gameClubName": ["STRING", "tt"], "gameShiZhongPai": ["INT32", 0],
                                              "gameUnUse": ["INT32", 0], "gameGuDingWanFa": ["INT32", 0],
                                              "gameParamIndex": ["INT32", 0]}
        self.cs_keys_list = self.cs_create_room_leiyang_entity.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_create_room_leiyang_entity, self.cs_keys_list, self.update_data,
                                       self.method).real_data


#   leave room -->CS
class CSLeaveRoom:
    def __init__(self, data={}):
        self.cs_leave_room_data = {"protocol_num": ["INT32", 1004]}
        self.cs_keys_list = self.cs_leave_room_data.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_leave_room_data, self.cs_keys_list, self.update_data,
                                       self.method).real_data


#   leave room -->SC
class SCLeaveRoom:
    def __init__(self):
        self.sc_entity_data = {"mid": ["INT32", 00], "error_code": ["INT32", 99]}


#   dissolve room -->CS
class CSDissolveRoom:
    def __init__(self, data={}):
        self.cs_dissolve_room_data = {"protocol_num": ["INT32", 1008]}
        self.cs_keys_list = self.cs_dissolve_room_data.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_dissolve_room_data, self.cs_keys_list, self.update_data,
                                       self.method).real_data


#   dissolve room --> SC: have not this entity
class SCDissolveRoom:
    def __init__(self):
        self.sc_entity_data = {"err": ["INT32", 0], "mid": ["INT32", 1], "disband_author": ["INT32", 1],
                               "over_time": ["INT32", 1], "option": ["vote_players", 1]}


#   chose dissolve room -->CS
class CSChoseDissolveRoom:
    def __init__(self, data={}):
        self.cs_chose_dissolve_room_data = {"protocol_num": ["INT32", 1012], "option": ["INT32", 1]}
        self.cs_keys_list = self.cs_chose_dissolve_room_data.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_chose_dissolve_room_data, self.cs_keys_list, self.update_data,
                                       self.method).real_data


#   chose dissolve room -->SC
class SCChoseDissolveRoom:
    def __init__(self):
        self.sc_entity_data = {"err": ["INT32", 0]}


#   dissolve room -->SC
class SCChoseDissolveRoomEnd:
    def __init__(self):
        self.sc_entity_data = {"scene_id": ["INT32", 0], "scene_type": ["STRING", 0], "type": ["INT32", 0]}


class CSRequestEnterRoom:
    def __init__(self, data={}):
        self.cs_request_enter_data = {"protocol_num": ["INT32", 1001], "room_id": ["INT32", 0], "version": ["INT32", 0],
                                      "ip": ["INT32", 0], "password": ["INT32", 0], "source": ["INT32", 0], "club_pay": ["INT32", 0],
                                      }
        self.cs_keys_list = self.cs_request_enter_data.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_request_enter_data, self.cs_keys_list, self.update_data,
                                       self.method).real_data


#   request enter room --> SC
class SCRequestEnterRoom:
    def __init__(self):
        self.sc_entity_data = {"wanfa_type": ["INT32", 1], "seat_no": ["INT32", 0], "scene_id": ["INT32", 0],
                               "scene_type": ["STRING", ""], "password": ["INT32", 0], "wanfa_index": ["INT32", 0], }


#   request query player and room info  -->CS
class CSRequestQueryInfo:
    def __init__(self, data={}):
        self.cs_request_query_info = {"protocol_num": ["INT32", 1009]}
        self.cs_keys_list = self.cs_request_query_info.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_request_query_info, self.cs_keys_list, self.update_data,
                                       self.method).real_data


#   request query player and room info  -->SC
class SCRequestQueryInfo:
    def __init__(self):
        self.sc_entity_data = {}


#   desktop snapshot --> SC
class SCDesktopSnapshot:
    def __init__(self):
        self.sc_entity_data = {"room_num": ["INT32", 0], "room_type": ["STRING", ""], "total_times": ["INT32", 0],
                               "banker_seat_id": ["INT32", 0], "current_player_seat_id": ["INT32", 0],
                               "current_card": ["STRING", ""], "current_send_card_seat_id": ["INT32", 0],
                               "hupai_type": ["INT32", 0], "player_num": ["INT32", 0], "player_info": ["INT32", {
                "seat_id": ["INT32", 0], "mid": ["INT32", 0], "zanli": ["INT32", 0], "isready": ["INT32", 0],
                "huxi": ["INT32", 0], "send_card_num": ["INT32", 0], "_card_list": ["STRING", ""],
                "molding_card": ["INT32", 0], "_card_type_list": ["INT32", {"shoupai_type": ["INT32", 0],
                                                                            "card_num": ["INT32", 0],
                                                                            "_card": ["STRING", ""], }]}],
                               "homer_seat_id": ["INT32", 0], "game_start_type": ["INT32", 0],
                               "player_number": ["INT32", 0],
                               "_player": ["INT32", {"seat_id": ["INT32", 0], "jiatuo_daniao": ["STRING", ""]}]}


#   room snapshot   -->SC
class SCRoomSnapshot:
    def __init__(self):
        self.sc_entity_data = {"room_owner": ['INT32', 0], "room_state": ['INT32', 0], "played_num": ['INT32', 0],
                               "total_ju": ['INT32', 0], "players_num": ['INT32', 0],
                               "players_info": ["INT32", {"seat_no": ['INT32', 0], "ip_addr": ['STRING', ""],
                                                          "mid": ['INT32', 0], "gp": ['INT32', 0],
                                                          "sex": ['INT32', 0], "name": ['STRING', ""],
                                                          "icon": ['STRING', ""], "city": ['STRING', ""],
                                                          "json_str": ["STRING", ""]}],
                               "banker_seatno": ["INT32", 0], "seats_size": ["INT32", 0], "json_str": ['STRING', ""]}


#   enter room player info -->SC
class SCEnterRoomPlayerInfo:
    def __init__(self):
        self.sc_entity_data = {"mid": ["INT32", 0], "sex": ["INT32", 0], "name": ["STRING", 0], "icon": ["STRING", 0],
                               "vip": ["INT32", 0], "gold": ["INT32", 0], "jifen": ["INT32", 0],
                               "seat_id": ["INT32", 0], "ip": ["STRING", 0], "jingweidu": ["STRING", 0],
                               "huxi": ["INT32", 0], "time": ["INT32", 0], "home_owner": ["INT32", 0]}


class SCPlayGameTimes:
    def __init__(self):
        self.sc_entity_data = {"has_been_play_times": ["INT32", 0]}


#   request ready -->CS
class CSRequestReady:
    def __init__(self, data={}):
        self.cs_request_ready_data = {"protocol_num": ["INT32", 1005]}
        self.cs_keys_list = self.cs_request_ready_data.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_request_ready_data, self.cs_keys_list, self.update_data,
                                       self.method).real_data


class SCRequestReady:
    def __init__(self):
        self.sc_entity_data = {"seat_no": ["INT32", 0]}


#   trusteeship --> CS
class CSTrusteeship:
    def __init__(self, data={}):
        self.cs_trusteeship_data = {"protocol_num": ["INT32", 1053]}
        self.cs_keys_list = self.cs_trusteeship_data.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_trusteeship_data, self.cs_keys_list, self.update_data,
                                       self.method).real_data


#   trusteeship --> SC
class SCTrusteeship:
    def __init__(self):
        self.sc_entity_data = {"seat_number": ["INT32", 0], "is_trusteeship": ["INT32", 0]}


#   game start -->SC
class SCGameStart:
    def __init__(self):
        self.sc_entity_data = {"err_no": ["INT32", 0], "played_num": ["INT32", 0], "banker_seatno": ["INT32", 0]}

#   少人模式
class SCInformLessMode:
    def __init__(self):
        self.sc_entity_data = {
            "PlayerNum": ["INT32", 0],
            "PlayerInfo":["INT32", {
                "SeatID": ["INT32", 0],
                "Mid": ["INT32", 0],
                "Sex": ["INT32", 0],
                "Name": ["STRING", ""],
                "Icon": ["STRING", ""],
                "Vip": ["INT32", 0],
                "Gold": ["INT64", 0],
                "Integral": ["INT32", 0],
                "IP": ["STRING", ""],
                "Json": ["STRING", ""]
            }],
            "RoomInfo": ["STRING", ""]
        }

#   选择发送少人模式 1094
class CSOpenLessMode:
    def __init__(self):
        self.cs_send_gift_data = {
            "protocol_num": ["INT32", 1094],
            "IsAgree": ["INT32", 1]
        }
        self.cs_keys_list = self.cs_send_gift_data.keys()
        self.update_data = {}
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_send_gift_data, self.cs_keys_list, self.update_data,
                                       self.method).real_data

class SCOpenLessMode:
    def __init__(self):
        self.sc_entity_data = {
            "ErrorCode": ["INT32", 0],
            "InitiateMid": ["INT32", 0],
            "OpenTime": ["INT32", 0],
            "OpenNum": ["INT32", 0],
            "OpenInfo": ["INT32", {
                "SeatID": ["INT32", 0],
                "State": ["INT32", 0]
            }]
        }

#   send card -->SC
class SCBaoCards:
    def __init__(self):
        self.sc_entity_data = {"count": ["INT32", 0], "bao_cards": ["STRING", ""], "is_reconnet": ["INT32", 0],
                               "fanbao_card": ["STRING", ""]}

#   send card -->SC
class SCSendCards:
    def __init__(self):
        self.sc_entity_data = {"card_num": ["INT32", 0], "card_lists": ["STRING", ""], "dun_count": ["INT32", 0]}


#   touch cards -->SC
class SCTouchCards:
    def __init__(self):
        self.sc_entity_data = {"seat_id": ["INT32", 0], "remain_card": ["INT32", 0], "touch_card": ["STRING", ""],
                               "is_open": ["INT32", 0], "is_hand_card": ["INT32", 0], "is_fanxing": ["INT32", 0]}


#   player can do -->SC
class SCPlayerCanDo:
    def __init__(self):
        self.sc_entity_data = {"seat_no": ["INT32", 1], "opeate_size": ["INT32", 0],
                               "opeate": ["INT32", 0], "operation_id": ["STRING", ""]}


#   玩家出牌请求 -->CS
class CSClientPlayReq:
    def __init__(self, data={}):
        self.cs_request_ready_data = {"protocol_num": ["INT32", 1023], "card": ["STRING", ""],
                                      "operation_id": ["STRING", ""]}
        self.cs_keys_list = self.cs_request_ready_data.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_request_ready_data, self.cs_keys_list, self.update_data,
                                       self.method).real_data


#   玩吃牌请求 -->CS
class CSClientChiReq:
    def __init__(self, data={}):
        self.cs_request_ready_data = {"protocol_num": ["INT32", 1036], "card": ["STRING", ""],
                                      "operation_id": ["STRING", ""]}
        self.cs_keys_list = self.cs_request_ready_data.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_request_ready_data, self.cs_keys_list, self.update_data,
                                       self.method).real_data


#   玩家碰牌请求 -->CS
class CSClientPengReq:
    def __init__(self, data={}):
        self.cs_request_ready_data = {"protocol_num": ["INT32", 1024], "operation_id": ["STRING", ""]}
        self.cs_keys_list = self.cs_request_ready_data.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_request_ready_data, self.cs_keys_list, self.update_data,
                                       self.method).real_data


#   玩家杠牌请求 -->CS
class CSClientGangReq:
    def __init__(self, data={}):
        self.cs_request_ready_data = {"protocol_num": ["INT32", 1025], "card": ["STRING", ""],
                                      "operation_id": ["STRING", ""]}
        self.cs_keys_list = self.cs_request_ready_data.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_request_ready_data, self.cs_keys_list, self.update_data,
                                       self.method).real_data


#   玩家取消操作请求 -->CS
class CSClientCancelReq:
    def __init__(self, data={}):
        self.cs_request_ready_data = {"protocol_num": ["INT32", 1027], "operation_id": ["STRING", ""]}
        self.cs_keys_list = self.cs_request_ready_data.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_request_ready_data, self.cs_keys_list, self.update_data,
                                       self.method).real_data


#   玩家取消操作请求 -->CS
class CSClientHuReq:
    def __init__(self, data={}):
        self.cs_request_ready_data = {"protocol_num": ["INT32", 1026], "operation_id": ["STRING", ""]}
        self.cs_keys_list = self.cs_request_ready_data.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_request_ready_data, self.cs_keys_list, self.update_data,
                                       self.method).real_data


class CSRequestFunction:
    def __init__(self, data={}):
        if data['card_num'] != 0:
            self.cs_request_function_data = {"protocol_num": ["INT32", 1012], "function_type": ["INT32", 0],
                                             "card_num": ["INT32", 0], "_card": ["STRING", []],
                                             "function_index": ["STRING", ""]}
        else:
            self.cs_request_function_data = {"protocol_num": ["INT32", 1012], "function_type": ["INT32", 0],
                                             "card_num": ["INT32", 0], "function_index": ["STRING", ""]}
        self.cs_keys_list = self.cs_request_function_data.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_request_function_data, self.cs_keys_list, self.update_data,
                                       self.method).real_data


class SCRequestFunction:
    def __init__(self):
        self.sc_entity_data = {"seat_no": ["INT32", 1], "opeate_size": ["INT32", 0],
                               "opeate": ["INT32", 0], "operation_id": ["STRING", ""]}


class SCErrorTips:
    def __init__(self):
        self.sc_entity_data = {"error_code": ["INT32", 0], "card": ["STRING", ""]}



#   小局结算 --1031
class SCSettlement:
    def __init__(self):
        self.sc_entity_data = {
            "wanfa_type": ["INT32", 1],
            "now_banker_seatno": ["INT32", 0],
            "next_banker_seatno": ["INT32", 0],
            "left_ju": ["INT32", 0],
            "hu_type": ["INT32", 0],
            "hu_card": ["STRING", ""],
            "hu_players": ["INT32", 0],
            "hu_seatno": ["INT32", 0],
            "players_num": ["INT32", 0],
            "seats_info": ["INT32", {
                "seat_no": ["INT32", 0],
                "mid": ["INT32", 0],
                "name": ["STRING", ""],
                "icon": ["STRING", ""],
                "game_score": ["INT32", 0],
                "seat_score": ["INT64", 0],
                "operated_cards_size": ["INT32", 0],
                "op_cardinfo": ["INT32", {
                    "card": ["STRING", ""],
                    "cause_op": ["INT32", 0],
                }],
                "handcards_size": ["INT32", 0],
                "card": ["STRING", ""],
                "mingtang_infos": ["INT32", {
                    "type": ["INT32", 0],
                    "num": ["INT32", 0],
                }],
            }],
            "zhaniao_num": ["INT32", 0],
            "card": ["STRING", ""],
            "room_json_str": ["STRING", ""],
            "bao_card_num": ["INT32", 0],
            "bao_cards": ["STRING", ""],
            "json_str": ["STRING", ""],
        }


#   not in room -->SC
class SCNotInRoom:
    def __init__(self):
        self.sc_entity_data = {"error_code": ["INT16", 0]}


#   server close -> SC
class SCServerClose:
    def __init__(self):
        self.sc_entity_data = {"error_code": ["INT32", 0]}


#   total settlement
class SCTotalSettlement:
    def __init__(self):
        self.sc_entity_data = {"players": ["INT32", 0], "_players_info": ["INT32", {"seat_id": ["INT32", -100],
                                                                                    "room_total_socre": ["INT32", -100],
                                                                                    "win_socre": ["INT32", -100], }],
                               "homeower_seat_id": ["INT32", -100], "room_id": ["INT32", -100],
                               "players_num": ["INT32", 0], "_players_num_info": ["INT32", {"seat_id": ["INT32", -100],
                                                                                            "hupai_num": ["INT32",
                                                                                                          -100],
                                                                                            "zimo_num": ["INT32", -100],
                                                                                            "dianpao_num": ["INT32",
                                                                                                            -100],
                                                                                            "tipai_num": ["INT32",
                                                                                                          -100],
                                                                                            "paopai_num": ["INT32",
                                                                                                           -100]}],
                               "ending_time": ["INT32", 0], "players_number": ["INT32", 0],
                               "_players_number_info": ["INT32", {"seat_id": ["INT32", -100], "tips": ["STRING", ""]}],
                               "play_game_num": ["INT32", 0], "total_game_num": ["INT32", 0], "club_id": ["INT32", 0],
                               "dissolve_info": ["INT32", 0], "_dissolve_info_list": ["INT32", {"seat_id": ["INT32", 0],
                                                                                                "dissolve_state": [
                                                                                                    "INT32", 0]}]}


#   common chat
class SCCommonChat:
    def __init__(self):
        self.sc_entity_data = {"chat_type": ["INT32", 0], "mid": ["INT32", 0], "name": ["STRING", ""],
                               "msg": ["STRING", ""], "seat_id": ["INT32", 0]}


class CSChat:
    def __init__(self, data):
        self.cs_chat_data = {"protocol_num": ["INT32", 2001], "msg": ["STRING", ""], "type": ["INT32", 0]}
        self.cs_keys_list = self.cs_chat_data.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_chat_data, self.cs_keys_list, self.update_data, self.method).real_data


class SCChat:
    def __init__(self):
        self.sc_entity_data = {"error_code": ["INT32", 0], "type": ["INT32", -100], "seat_id": ["INT32", 0]}


class CSChatFace:
    def __init__(self, data):
        self.cs_chat_face_data = {"protocol_num": ["INT32", 2009], "msg": ["STRING", ""], "type": ["INT32", 0]}
        self.cs_keys_list = self.cs_chat_face_data.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_chat_face_data, self.cs_keys_list, self.update_data,
                                       self.method).real_data


class SCChatFace:
    def __init__(self):
        self.sc_entity_data = {"error_code": ["INT32", -100], "type": ["INT32", -100], "seat_id": ["INT32", 0]}


class CSSendGift:
    def __init__(self, data):
        self.cs_send_gift_data = {"protocol_num": ["INT32", 1042], "recv_id": ["INT32", 0], "props": ["STRING", ""]}
        self.cs_keys_list = self.cs_send_gift_data.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_send_gift_data, self.cs_keys_list, self.update_data,
                                       self.method).real_data


class SCSendGift:
    def __init__(self):
        self.sc_entity_data = {"error_code": ["INT32", -100], "send_mid": ["INT32", 0], "recv_mid": ["INT32", 0],
                               "props": ["STRING", ""]}


class SCCommonChatWithFace:
    def __init__(self):
        self.sc_entity_data = {"type": ["INT32", -100], "mid": ["INT32", -100], "name": ["STRING", ""],
                               "msg": ["STRING", ""]}


class CSMakeCardsType:
    def __init__(self, data):
        self.cs_make_cards_type_data = {"protocol_num": ["INT32", 1057], "cards_list": ["STRING", ""]}
        self.cs_keys_list = self.cs_make_cards_type_data.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_make_cards_type_data, self.cs_keys_list, self.update_data,
                                       self.method).real_data


class SCMakeCardsType:
    def __init__(self):
        self.sc_entity_data = {"error_code": ["INT32", -100]}


class SCReconnectionServerSendCards:
    def __init__(self):
        self.sc_entity_data = {"dipai_num": ["INT32", -100], "_cards": ["STRING", ""]}


class CSJingWeiDu:
    def __init__(self, data):
        self.cs_jingweidu_data = {"protocol_num": ["INT32", 1028], "jingweidu": ["STRING", ""],
                                  "isrefresh": ["INT32", 99]}
        self.cs_keys_list = self.cs_jingweidu_data.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_jingweidu_data, self.cs_keys_list, self.update_data,
                                       self.method).real_data


class SCJingWeiDu:
    def __init__(self):
        self.sc_entity_data = {"players": ["INT32", -100],
                               "players_info": ["INT32", {"seat_id": ["INT32", 0], "jingweidu": ["STRING", ""]}]}


class CSCreatedGameList:
    def __init__(self, data):
        self.cs_created_game_list_data = {"protocol_num": ["INT32", 1100]}
        self.cs_keys_list = self.cs_created_game_list_data.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_created_game_list_data, self.cs_keys_list, self.update_data,
                                       self.method).real_data


class SCCreatedGameList:
    def __init__(self):
        self.sc_entity_data = {"list_num": ["INT32", 0], "list_info": ["INT32", {"game_index": ["INT32", 0],
                                                                                 "club_id": ["INT32", 0],
                                                                                 "club_name": ["STRING", ""],
                                                                                 "room_type": ["STRING", ""],
                                                                                 "wanfa": ["INT32", 0],
                                                                                 "difen": ["INT32", 0],
                                                                                 "room_players": ["INT32", 0],
                                                                                 "total_players": ["INT32", 0],
                                                                                 "real_players": ["INT32", 0],
                                                                                 "rounds_num": ["INT32", 0],
                                                                                 "innings": ["INT32", 0],
                                                                                 "format": ["INT32", 0],
                                                                                 "state": ["INT32", 0],
                                                                                 "distance_close_time": ["INT32", 0],
                                                                                 "uuid": ["STRING", ""], }

                                                                       ]}


class CSClubGameList:
    def __init__(self, data):
        self.cs_club_game_list_data = {"protocol_num": ["INT32", 1101]}
        self.cs_keys_list = self.cs_club_game_list_data.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_club_game_list_data, self.cs_keys_list, self.update_data,
                                       self.method).real_data


class SCClubGameList:
    def __init__(self):
        self.sc_entity_data = {"list_num": ["INT32", 0], "list_info": ["INT32", {"club_icon": ["STRING", ""],
                                                                                 "club_name": ["STRING", ""],
                                                                                 "club_id": ["INT32", 0],
                                                                                 "game_index": ["INT32", 0],
                                                                                 "room_type": ["STRING", ""],
                                                                                 "wanfa": ["INT32", 0],
                                                                                 "difen": ["INT32", 0],
                                                                                 "room_players": ["INT32", 0],
                                                                                 "total_players": ["INT32", 0],
                                                                                 "real_players": ["INT32", 0],
                                                                                 "rounds_num": ["INT32", 0],
                                                                                 "innings": ["INT32", 0],
                                                                                 "format": ["INT32", 0],
                                                                                 "state": ["INT32", 0],
                                                                                 "distance_close_time": ["INT32", 0],
                                                                                 "uuid": ["STRING", ""], }

                                                                       ]}


class SCPlayerChangeIdentity:
    def __init__(self):
        self.sc_entity_data = {"status": ["INT32", -100]}


class CSCreateRoomYiYang:
    def __init__(self, data={}):
        self.cs_create_room_entity = {"protocol_num": ["INT32", 2029], "gameBaoLiuZi": ["INT16", 1],
                                      "gameRoomType": ["STRING", "20"], "gamePaiJu": ["INT32", 0],
                                      "gameCiShu": ["INT32", 6], "gameWanFa": ["INT16", 0], "gamePlayer": ["INT32", 0],
                                      "gameFengDing": ["INT32", 100], "gameQiHu": ["INT32", 6],
                                      "gameClubId": ["INT32", 0], "gameVip": ["INT32", 0],
                                      "gameClubName": ["STRING", ""], "gameMoShi": ["INT32", 0],
                                      "gameParamIndex": ["INT32", 0], "gameTag": ["INT32", 0]

                                      }
        self.cs_keys_list = self.cs_create_room_entity.keys()
        self.update_data = data
        self.method = "pack"
        self.real_data = CallUpdateApi(self.cs_create_room_entity, self.cs_keys_list, self.update_data,
                                       self.method).real_data


class SCCreateRoomYiYang:
    def __init__(self, data={}):
        self.sc_entity_data = {"BaoLiuZi": ["INT16", 0], "error_code": ["INT32", 0], "gameRoomid": ["INT32", 0],
                               "gameRoomType": ["STRING", 0], "gamePaiJu": ["INT32", 0], "gameJuShu": ["INT32", 0],
                               "gameWanFa": ["INT16", 0], "gameRenShu": ["INT32", 0], "gameFengDing": ["INT32", 0],
                               "gameMinHuXi": ["INT32", 0], "gameClubId": ["INT32", 0], "gameVip": ["INT32", 0],
                               "gameClubName": ["STRING", ""]}

        self.sc_login_keys_list = self.sc_entity_data.keys()
        self.update_data = data
        self.method = "unpack"


# 岳阳玩法广播谁可以做什么操作
class SCPlayerCanDoYueYang:
    def __init__(self):
        self.sc_entity_data = {"BaiLiuZi": ["INT16", 0], "seat_id": ["INT32", 0], "last_push_card": ["STRING", ""],
                               "sure_liu_card": ["STRING", ""], "sure_chi_card": ["STRING", ""],
                               "is_chu_card": ["INT32", 99], "is_peng_card": ["INT32", 99],
                               "is_chi_card": ["INT32", 99], "is_hu_card": ["INT32", 99], "fun_index": ["STRING", ""],
                               "fun_type": ["INT32", 99], "is_baojing": ["INT32", 99], "is_waiPai": ["INT32", 99],
                               "is_LiuPai": ["INT32", 99], "time": ["STRING", ""]}


# 益阳玩法广播谁可以做什么操作
class SCPlayerCanDoYiYang:
    def __init__(self):
        self.sc_entity_data = {"BaiLiuZi": ["INT16", 0], "seat_id": ["INT32", 0], "desktop_card": ["STRING", ""],
                               "sure_liu_card": ["STRING", ""], "sure_chi_card": ["STRING", ""],
                               "is_chu_card": ["INT32", 99], "is_peng_card": ["INT32", 99],
                               "is_chi_card": ["INT32", 99], "is_hu_card": ["INT32", 99], "fun_index": ["STRING", ""],
                               "fun_type": ["INT32", 99], "is_baojing": ["INT32", 99], "is_waiPai": ["INT32", 99],
                               "is_LiuPai": ["INT32", 99], "unused": ["STRING", ""]}


#   暂离房间
class SCStepOutRoom:
    def __init__(self):
        self.sc_entity_data = {'error_code': ['INT32', 100], "seat_id": ["INT32", 0]}


#   黑牌
class SCBlackCards:
    def __init__(self):
        self.sc_entity_data = {"card_num": ['INT32', 0], '_card_name': ['STRING', ""]}


#   广播结算（岳阳）
class SCSettlementYueYang:
    def __init__(self):
        self.sc_entity_data = {'ReservedWords': ['INT16', 0], "SettlementType": ["INT32", 0],
                               'PlayersNum': ["INT32", 0], "WinnerSeatId": ["INT32", 0], "WinnerIntegral": ["INT32", 0],
                               'BankerName': ['STRING', ''], 'Mid': ["INT32", 0], 'Icon': ["STRING", ''],
                               'TotalIntegral': ["INT32", 0], 'SentHomeSeatId_1': ["INT32", 0],
                               'SentHomeIntegral_1': ["INT32", 0], 'SentHomeName_1': ['STRING', ''],
                               'SHMid_1': ["INT32", 0], 'SHIcon_1': ["STRING", ''], 'SHTotalIntegral_1': ["INT32", 0],
                               'SentHomeSeatId_2': ["INT32", 0], 'SentHomeIntegral_2': ["INT32", 0],
                               'SentHomeName_2': ['STRING', ''], 'SHMid_2': ["INT32", 0], 'SHIcon_2': ["STRING", ''],
                               'SHTotalIntegral_2': ["INT32", 0], 'RemainCardNum': ['INT32', 0],
                               'RemainCards': ['STRING', ''], 'AllPlayerNum': ['INT32', 0], 'AllPlayerInfo': ['INT32', {
                'PlayerSeatId': ['INT32', 0], 'PlayerRemainCard': ['INT32', 0], 'Cards': ['STRING', '']}],
                               'ShapeTpyeNum': ['INT32', 0], 'ShapeNumInfo': ['INT32', {'CardTpye': ['INT32', 0],
                                                                                        'Huxi': ['INT32', 0],
                                                                                        'CardNum': ['INT32', 0],
                                                                                        'Cards': ['STRING', '']}],
                               'BonusTpyeNum': ['INT32', 0],
                               'BonusNumInfo': ['INT32', {'Tpye': ['INT32', 0], 'HuTpye': ['INT32', 0]}],
                               'WinnerHuXi': ['INT32', 0], 'WinCards': ['STRING', ''], 'HuPaiIndex': ['INT32', 0],
                               'BankerSeatId': ['INT32', 0], 'RoomId': ['INT32', 0], 'Time': ['INT32', 0]}


#   广播总结算（岳阳）
class SCTotalSettlementYueYang:
    def __init__(self):
        self.sc_entity_data = {'ReservedWords': ['INT16', 0], 'PlayerNum': ["INT32", 0], 'PlayerInfo': ["INT32", {
            'SeatID': ["INT32", 0], 'RoomIntegral': ["INT32", 0], 'WinIntegral': ["INT32", 0], 'Name': ['STRING', ''],
            'Mid': ["INT32", 0], 'Icon': ['STRING', '']}], 'HomeSeatID': ["INT32", 0], 'RoomID': ["INT32", 0],
                               'PlayerCount': ["INT32", 0], 'PlayerMsg': ["INT32", {'SeatID': ["INT32", 0],
                                                                                    'HuCount': ["INT32", 0],
                                                                                    'ZiMoCount': ["INT32", 0],
                                                                                    'LiuCount': ["INT32", 0],
                                                                                    'WaiCount': ["INT32", 0]}],
                               'CurrentRound': ["INT32", 0], 'TotalRound': ["INT32", 0], 'ClubID': ["INT32", 0],
                               'DissolveReason': ["INT32", 0],
                               'DissolveInfo': ["INT32", {'SeatID': ["INT32", 0], 'Operate': ["INT32", 0]}],
                               'PlayBack': ['STRING', '']}


# 死手<益阳>
class SCDeadHand:
    def __init__(self):
        self.sc_entity_data = {'sead_id': ['INT32', -100]}

# 神牌 <益阳>
class SCServerPushGodCards:
    def __init__(self):
        self.sc_entity_data = {'GodCard': ['STRING', ""], 'GodCardType': ['INT32', 0]}


# 臭牌 <益阳>
class SCSmellyCard:
    def __init__(self):
        self.sc_entity_data = {'AbsoluteCard': ['STRING', ''], 'IndirectCard': ['STRING', '']}