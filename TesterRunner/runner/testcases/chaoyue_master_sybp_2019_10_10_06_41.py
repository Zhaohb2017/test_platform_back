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
        player1 = UserBehavior(456,456,True)
        player2 = UserBehavior(4564)
        time.sleep(2)
        player1.SetGameType = "邵阳剥皮"
        player2.SetGameType = "邵阳剥皮"
        create_room_data = {'o_player': 2, 'o_round': 10, 'o_huyideng': '5息一囤', 'o_card_num': '抽牌20张', 'o_RedAndBlack': True, 'o_lianzhuang': False, 'o_0fen': False, 'o_jiachui': '', 'o_integral': '', 'o_NoShow_dipai': False, 'o_fengdinghuxi': '', 'o_double': 0, 'o_fanbei': '', 'o_doubleNew': False, 'o_double_score': '', 'o_double_plus': 0, 'roomTypeVuale': '普通创房', 'clubRoomTypeVuale': '', 'o_club_id': ''}
        player1.CreateRoom(create_room_data)
        time.sleep(2)
        cards_data = {"1":["1W","2W","3W","1S","2S","3S","1T","2T","3T","4W","4W","7W","8W","HZ"], "2":["1W","2W","3W","1S","2S","3S","1T","2T","3T","4S","4S","7W","8W"], "3":["1W","2W","3W","1S","2S","3S","1T","2T","3T","4T","4T","7W","8W"], "4":["HZ","HZ","1W","2W","3W","1S","2S","3S","1T","2T","3T","7W","8W"], "5":["HZ","HZ","9W","6W","6W","6W","6W","9S","9T","9S","9T","6T","6S"]}
        player1.maker_card(cards_data,player1.room_id)
        time.sleep(2)
        player2.ApplyEnterRoom(player1.room_id,0)
        player1.OperateApi('出', '', ['8s'])
        time.sleep(1)
        time.sleep(5)
        player1.ConnectClose()
        player2.ConnectClose()
if __name__=='__main__':
    unittest.main()