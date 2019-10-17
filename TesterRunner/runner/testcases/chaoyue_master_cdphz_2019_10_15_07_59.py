import sys
import os
cur_path = os.path.abspath(os.path.dirname(__file__))
last_path = os.path.split(cur_path)[0]
last_path_len = last_path.split("/")[-1]
root_path = last_path[:len(last_path) - len(last_path_len)]
sys.path.append(root_path)
import time
import unittest
from chaoyue.master.phz.api import *
class PHZTestCase(unittest.TestCase):
    def test_task(self):
        player1 = UserBehavior(2342,2342,True)
        player2 = UserBehavior(4232)
        time.sleep(2)
        player1.SetGameType = "常德跑胡子"
        player2.SetGameType = "常德跑胡子"
        create_room_data = {'o_player': 2, 'o_round': 8, 'o_card_num': '抽牌20张', 'o_mingwei': True, 'o_mingtang': '全名堂', 'o_difen': 1, 'o_wanfa': '', 'o_fengding': '100', 'o_datuanyuan': True, 'o_xingxingxi': True, 'o_shuahou': True, 'o_tinghu': '', 'o_huangfanDouble': '', 'o_jiaxingxing': '', 'o_siqihong': '', 'o_yikuaibian': '', 'roomTypeVuale': '普通创房', 'clubRoomTypeVuale': '', 'o_club_id': '', 'o_double': 0}
        player1.CreateRoom(create_room_data)
        time.sleep(2)
        cards_data = {}
        player1.maker_card(cards_data,player1.room_id)
        time.sleep(2)
        player2.ApplyEnterRoom(player1.room_id,0)
        player1.OperateApi('碰')
        time.sleep(1)
        player2.OperateApi('胡')
        time.sleep(1)
        time.sleep(5)
        player1.ConnectClose()
        player2.ConnectClose()
if __name__=='__main__':
    unittest.main()