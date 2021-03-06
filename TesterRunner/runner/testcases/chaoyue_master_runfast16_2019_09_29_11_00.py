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
        player1 = UserBehavior(321,321,True)
        player2 = UserBehavior(312)
        time.sleep(2)
        player1.SetGameType = "跑得快16张"
        player2.SetGameType = "跑得快16张"
        create_room_data = {'o_player': 2, 'o_round': 10, 'o_showCard': True, 'o_zhuaNiao': False, 'o_outBig': True, 'o_nonSeparability': True, 'o_gaiPai': False, 'o_outThree': True, 'o_double_plus_new': False, 'o_double': 0, 'roomTypeVuale': '普通创房', 'clubRoomTypeVuale': '', 'o_club_id': ''}
        player1.CreateRoom(create_room_data)
        time.sleep(2)
        cards_data = {}
        player1.maker_card(cards_data,player1.room_id)
        time.sleep(2)
        player2.ApplyEnterRoom(player1.room_id,0)
        player1.OperateApi('出', '', ['2s', '3s', '4s', '5s', '6s'])
        time.sleep(1)
        time.sleep(5)
        player1.ConnectClose()
        player2.ConnectClose()
if __name__=='__main__':
    unittest.main()