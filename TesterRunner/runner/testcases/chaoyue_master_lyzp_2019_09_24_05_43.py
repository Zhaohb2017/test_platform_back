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
        player1 = UserBehavior(888,888,True)
        player2 = UserBehavior(99)
        player3 = UserBehavior(0)
        time.sleep(2)
        player1.SetGameType = "耒阳字牌"
        player2.SetGameType = "耒阳字牌"
        player3.SetGameType = "耒阳字牌"
        create_room_data = {'o_player': 3, 'o_round': 10, 'o_jszs': True, 'o_bdwh': False, 'o_bdydh': False, 'o_yxqp': False, 'o_dianpao_hu': 1, 'roomTypeVuale': '普通创房', 'clubRoomTypeVuale': '', 'o_club_id': ''}
        player1.CreateRoomLeiYang(create_room_data)
        time.sleep(2)
        cards_data = {"1":["1W","2W","3W","1S","2S","3S","1T","2T","3T","4W","4W","7W","8W","HZ"], "2":["1W","2W","3W","1S","2S","3S","1T","2T","3T","4S","4S","7W","8W"], "3":["1W","2W","3W","1S","2S","3S","1T","2T","3T","4T","4T","7W","8W"], "4":["HZ","HZ","1W","2W","3W","1S","2S","3S","1T","2T","3T","7W","8W"], "5":["HZ","HZ","9W","6W","6W","6W","6W","9S","9T","9S","9T","6T","6S"]}
        player1.MakeCards(cards_data)
        time.sleep(2)
        player2.ApplyEnterRoom(player1.room_id,0)
        player3.ApplyEnterRoom(player1.room_id,0)
        player3.OperateApi('补杠', '', '2S')
        time.sleep(1)
        time.sleep(5)
        player1.ConnectClose()
        player2.ConnectClose()
        player3.ConnectClose()
if __name__=='__main__':
    unittest.main()