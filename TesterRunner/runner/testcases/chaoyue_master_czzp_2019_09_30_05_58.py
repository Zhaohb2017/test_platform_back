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
        player1 = UserBehavior(127641,127641,True)
        player2 = UserBehavior(127643)
        player3 = UserBehavior(127853)
        time.sleep(2)
        player1.SetGameType = "郴州字牌"
        player2.SetGameType = "郴州字牌"
        player3.SetGameType = "郴州字牌"
        create_room_data = {'o_player': 3, 'o_round': 10, 'o_qihu': 9, 'o_double': 0, 'o_double_plus': 2, 'o_double_score': 0, 'o_tun': 3, 'o_zomoDouble': False, 'o_redBlack': False, 'o_maohu': True, 'o_dinapaobihu': 1, 'roomTypeVuale': '普通创房', 'clubRoomTypeVuale': '', 'o_club_id': ''}
        player1.CreateRoom(create_room_data)
        time.sleep(2)
        cards_data = {}
        player1.maker_card(cards_data,player1.room_id)
        time.sleep(2)
        player2.ApplyEnterRoom(player1.room_id,0)
        player3.ApplyEnterRoom(player1.room_id,0)
        player1.OperateApi('吃', '', ['1s'])
        time.sleep(1)
        time.sleep(5)
        player1.ConnectClose()
        player2.ConnectClose()
        player3.ConnectClose()
if __name__=='__main__':
    unittest.main()