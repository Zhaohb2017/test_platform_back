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
        player1 = UserBehavior(127843, True)
        player2 = UserBehavior(127641)
        player3 = UserBehavior(127866)
        time.sleep(2)
        player1.SetGameType = "邵阳放炮罚"
        create_room_data = {'人数': 3, '局数': 10, '胡一等': '5息一囤'}
        player1.CreateRoom(create_room_data)
        time.sleep(2)
        cards_data = [[['1s,1s,1s,1b,1b,1b,2s,2s,2s,2b,2b,2b,3s,3s,3s,3b,3b,3b,7s,7b'], ['4s,4s,4s,4b,4b,4b,5s,5s,5s,5b,5b,5b,6s,6s,6s,6b,6b,6b,7s,7b'], ['8s,8s,8s,8b,8b,8b,9s,9s,9s,9b,9b,9b,Ts,Ts,Ts,Tb,Tb,Tb,7s,7b'], ['7s,7b,1s,1b,2s,2b,3s,3b,4s,4b,5s,5b,6s,6b,8s,8b,9s,9b,Ts,Tb']]]
        player1.MakeCards(cards_data)
        time.sleep(2)
        player2.ApplyEnterRoom(player1.room_id)
        player3.ApplyEnterRoom(player1.room_id)
        while not player1.now_round_over:
            time.sleep(0.01)
        time.sleep(2)
        player1.ConnectClose()
        player2.ConnectClose()
        player3.ConnectClose()
if __name__=='__main__':
    unittest.main()