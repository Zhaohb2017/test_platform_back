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
        player1.SetGameType = "转转麻将"
        player2.SetGameType = "转转麻将"
        create_room_data = {'o_player': 2, 'o_round': 5, 'o_double_plus_new': False, 'o_zimohu': '可抢杠胡', 'o_sevenPair': True, 'o_xianjia': False, 'o_hongzhonglaizi': False, 'o_youpaibihu': False, 'o_qigang': False, 'o_zhuaMa': 2, 'o_double': 0, 'o_double_score': '', 'o_double_plus': 2, 'o_doublePlusNewScore': 10, 'o_159zhongma': False, 'o_bankerzhongniao': False, 'roomTypeVuale': '普通创房', 'clubRoomTypeVuale': '', 'o_club_id': ''}
        player1.CreateRoom(create_room_data)
        time.sleep(2)
        cards_data = {"1":["1W","1W","2W","2W","3W","3W","4W","4W","5W","5W","6W","6W","7W","7W","8W","8W","9W","9W","HZ","HZ"],
"2":["1S","1S","3S","3S","5S","5S","1T","1T","3T","3T","5T","5T","6W","6T"],                                                                    
"3":["2S","2S","4S","4S","6S","6S","2T","2T","4T","4T","6T","6T","6T"],
"4":["1T","1T","2S","2W","2T","2S","3W","3T","3S","4W","4T","4S","8W"],
"5":["HZ","HZ","9W","6W","6W","6W","6W","9S","9T","9S","9T","6T","6S"]}
        player1.maker_card(cards_data,player1.room_id)
        time.sleep(2)
        player2.ApplyEnterRoom(player1.room_id,0)
        player1.OperateApi('胡')
        time.sleep(5)
        player1.ConnectClose()
        player2.ConnectClose()
if __name__=='__main__':
    unittest.main()