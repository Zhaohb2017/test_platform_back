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
        player1 = UserBehavior(127643,127643,True)
        player2 = UserBehavior(127641)
        time.sleep(2)
        player1.SetGameType = "衡阳十胡卡"
        player2.SetGameType = "衡阳十胡卡"
        create_room_data = {'o_player': 2, 'o_round': '6', 'o_dianpao_hu': '', 'o_dianpao_None': '', 'o_fanxing': '不带醒', 'o_tunshu': '3息1囤', 'o_qihu': '6息起胡', 'o_hu_pao': '有胡必胡', 'o_mingwei': '', 'o_difen': '', 'o_yiwushi': '', 'o_red_black': '', 'o_hu_public': '', 'o_piaohu': '', 'o_tdhdh': '', 'o_fengding': '不封顶', 'o_cards_num': '21张', 'o_chou_card': '20', 'o_double': 0, 'o_double_score': '', 'o_doublePlusNewScore': 5, 'o_huyideng': '5息一囤', 'o_jiachui': '', 'o_card_num': '抽牌20张', 'roomTypeVuale': '普通创房', 'clubRoomTypeVuale': '', 'o_club_id': ''}
        player1.CreateRoom(create_room_data)
        time.sleep(2)
        cards_data = {}
        player1.maker_card(cards_data,player1.room_id)
        time.sleep(2)
        player2.ApplyEnterRoom(player1.room_id,0)
        player1.OperateApi('胡')
        time.sleep(1)
        time.sleep(5)
        player1.ConnectClose()
        player2.ConnectClose()
if __name__=='__main__':
    unittest.main()