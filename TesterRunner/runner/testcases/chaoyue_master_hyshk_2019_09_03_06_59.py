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
        player2 = UserBehavior(321)
        player3 = UserBehavior(321)
        time.sleep(2)
        player1.SetGameType = "衡阳十胡卡"
        player2.SetGameType = "衡阳十胡卡"
        player3.SetGameType = "衡阳十胡卡"
        create_room_data = {'o_player': 3, 'o_round': '6', 'o_chou_card': '抽牌20张', 'o_double': 0, 'o_double_score': '', 'o_doublePlusNewScore': 5, 'o_double_plus': 2, 'o_card_num': '抽牌20张', 'roomTypeVuale': '普通创房', 'clubRoomTypeVuale': '', 'o_club_id': ''}
        player1.CreateRoom(create_room_data)
        time.sleep(2)
        cards_data = cs
        player1.MakeCards(cards_data)
        time.sleep(2)
        player2.ApplyEnterRoom(player1.room_id,0)
        player3.ApplyEnterRoom(player1.room_id,0)
        player1.OperateApi('碰')
        time.sleep(1)
        time.sleep(5)
        player1.ConnectClose()
        player2.ConnectClose()
        player3.ConnectClose()
if __name__=='__main__':
    unittest.main()