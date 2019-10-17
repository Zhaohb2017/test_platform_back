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
        player1 = UserBehavior(1235,1235,True)
        player2 = UserBehavior(6578657)
        time.sleep(2)
        player1.SetGameType = "红中麻将"
        player2.SetGameType = "红中麻将"
        create_room_data = {'o_player': 2, 'o_round': 5, 'o_zimohu': '可抢杠胡', 'o_sevenPair': True, 'o_zhongMa': False, 'o_piaofen': False, 'o_eighthongzhong': False, 'o_integral': '', 'o_kejiepao': False, 'o_jiama': '不加码', 'o_zhuaMa': 2, 'o_double': 0, 'o_fanbei': '', 'o_doubleNew': False, 'o_double_score': '', 'o_double_plus': 2, 'o_doublePlusNewScore': 10, 'roomTypeVuale': '普通创房', 'clubRoomTypeVuale': '', 'o_club_id': ''}
        player1.CreateRoom(create_room_data)
        time.sleep(2)
        cards_data = {}
        player1.maker_card(cards_data,player1.room_id)
        time.sleep(2)
        player2.ApplyEnterRoom(player1.room_id,0)
        player2.OperateApi('补杠', '', ['8S\x00'])
        time.sleep(5)
        player1.ConnectClose()
        player2.ConnectClose()
if __name__=='__main__':
    unittest.main()