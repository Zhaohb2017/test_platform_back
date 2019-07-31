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
        player1 = UserBehavior(1111, True)
        player2 = UserBehavior(222)
        time.sleep(2)
        player1.SetGameType = "娄底放炮罚"
        create_room_data = {'o_player': 2, 'o_round': 10, 'o_huxi': 100, 'o_fan_2': '', 'o_fan_3': '', 'o_fan_4': '', 'o_choupai': '抽牌20张', 'o_qihu': 15, 'o_piaohu': True, 'o_fanbei': 0, 'o_fanbei_score': 2, 'o_huyideng': '5息一囤', 'o_jiachui': '', 'o_card_num': '抽牌20张', 'o_integral': '', 'o_NoShow_dipai': '', 'c_fanbei_score': '21'}
        player1.CreateRoom(create_room_data)
        time.sleep(2)
        cards_data = 321
        player1.MakeCards(cards_data)
        time.sleep(2)
        player2.ApplyEnterRoom(player1.room_id)
        while not player1.now_round_over:
            time.sleep(0.01)
        time.sleep(2)
        player1.ConnectClose()
        player2.ConnectClose()
if __name__=='__main__':
    unittest.main()