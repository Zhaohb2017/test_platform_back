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
        time.sleep(2)
        player1.SetGameType = "长沙跑胡子"
        player2.SetGameType = "长沙跑胡子"
        create_room_data = {'o_player': 2, 'o_double': 0, 'o_double_score': '', 'o_doublePlusNewScore': 100, 'o_double_plus_new': 0, 'o_double_plus_score': '', 'o_yiwushi': False, 'o_mingwei': False, 'o_shuahou': False, 'o_haidi': False, 'o_difen': 1, 'o_fengding': '1', 'o_qihu': 9, 'o_fanshu': '5番', 'o_zimo': 1, 'o_honghu': '红胡2加红加番', 'o_shiba': '十八小5加小番', 'o_shibada': '十八大5大加番', 'o_zhaniao': 1, 'o_round': 10, 'roomTypeVuale': '普通创房', 'clubRoomTypeVuale': '', 'o_club_id': ''}
        player1.CreateRoom(create_room_data)
        time.sleep(2)
        cards_data = {}
        player1.maker_card(cards_data,player1.room_id)
        time.sleep(2)
        player2.ApplyEnterRoom(player1.room_id,0)
        player1.OperateApi('碰')
        time.sleep(1)
        time.sleep(5)
        player1.ConnectClose()
        player2.ConnectClose()
if __name__=='__main__':
    unittest.main()