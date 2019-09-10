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
        player1 = UserBehavior(123,123,True)
        player2 = UserBehavior(321)
        player3 = UserBehavior(123)
        player4 = UserBehavior(1231321)
        time.sleep(2)
        player1.SetGameType = "攸县碰胡子"
        player2.SetGameType = "攸县碰胡子"
        player3.SetGameType = "攸县碰胡子"
        player4.SetGameType = "攸县碰胡子"
        create_room_data = {'o_player': 4, 'o_zhongzhuang': 2, 'o_jushu': 6, 'o_wanfa': 2, 'roomTypeVuale': '普通创房', 'clubRoomTypeVuale': '', 'o_club_id': ''}
        player1.CreateRoom(create_room_data)
        time.sleep(2)
        cards_data = 12
        player1.MakeCards(cards_data)
        time.sleep(2)
        player2.ApplyEnterRoom(player1.room_id,0)
        player3.ApplyEnterRoom(player1.room_id,0)
        player4.ApplyEnterRoom(player1.room_id,0)
        player1.OperateApi('胡')
        time.sleep(1)
        time.sleep(5)
        player1.ConnectClose()
        player2.ConnectClose()
        player3.ConnectClose()
        player4.ConnectClose()
if __name__=='__main__':
    unittest.main()