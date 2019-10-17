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
        player1 = UserBehavior(6676,6676,True)
        player2 = UserBehavior(4545)
        player3 = UserBehavior(899)
        time.sleep(2)
        player1.SetGameType = "耒阳字牌"
        player2.SetGameType = "耒阳字牌"
        player3.SetGameType = "耒阳字牌"
        create_room_data = {'o_player': 3, 'o_round': 8, 'o_jszs': True, 'o_bdwh': False, 'o_bdydh': False, 'o_yxqp': False, 'o_dianpao_hu': 1, 'roomTypeVuale': '普通创房', 'clubRoomTypeVuale': '', 'o_club_id': ''}
        player1.CreateRoomLeiYang(create_room_data)
        time.sleep(2)
        cards_data = {}
        player1.maker_card(cards_data,player1.room_id)
        time.sleep(2)
        player2.ApplyEnterRoom(player1.room_id,0)
        player3.ApplyEnterRoom(player1.room_id,0)
        player1.OperateApi('过')
        time.sleep(1)
        time.sleep(5)
        player1.ConnectClose()
        player2.ConnectClose()
        player3.ConnectClose()
if __name__=='__main__':
    unittest.main()