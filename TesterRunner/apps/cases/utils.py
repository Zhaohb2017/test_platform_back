#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@ author: Hubery
@ create on: 2019/3/4 15:49
@ file: utils.py
@ site: 
@ purpose: 
"""
import os
import time
from runner.logger import *


def _log(str,*args):
    get_current_path() +  str + args


#   获取当前路径
def get_current_path():
    return os.getcwd()
    # return os.path.dirname(os.path.realpath(__file__))


def transform_create_room_options(c_play, c_option):
    switcher = {
      "邵阳字牌": ShaoYangZiPia,
    }

    try:
        print(1111, c_play)
        return switcher[c_play](c_option)
    except:
        print("没有找到对应玩法选项值替换: %s" % c_play)


def ShaoYangZiPia(options):
    #   前台传过来的数据
    if 'o_player' in options:
        options["人数"] = options.pop('o_player')
        options["局数"] = options.pop('o_round')
        options["胡一等"] = options.pop('o_huyideng')
        options["玩法"] = options.pop('o_wanfa')
        options["牌数"] = options.pop('o_card_num')
    #   后端返回前台的数据 - 中文友好创房提示
    else:
        options["o_player"] = options.pop('人数')
        options["o_round"] = options.pop('局数')
        options["o_huyideng"] = options.pop('胡一等')
        options["o_wanfa"] = options.pop('玩法')
        options["o_card_num"] = options.pop('牌数')

    return options


#   生成用例脚本命名转换
def transform_play(team, play):
    TeamData = {
        "超越项目组-主版本": "chaoyue_master_",
        "开心游戏项目组-鄱余万版本": "kaixinyouxi_poyuwan_",
    }
    PlayData = {
        "邵阳字牌": 'syzp',
        "邵阳剥皮":"sybp",
        "耒阳字牌":"lyzp",
        "娄底放炮罚":"ldfpf",
        "湘乡告胡子":"xxghz",
        "衡阳百胡":"hybh",
        "郴州字牌":"czzp",
        "衡阳六胡抢":"hylqh",
        "邵阳放炮罚":"syfpf",
        "衡阳十胡卡":"hyshk",
        "攸县碰胡子":"yxphz",
        "常德跑胡子":"cdphz",
        "怀化红拐弯":"hhhgw",
        "永丰跑胡子":"yfphz",
        "祁东十五胡":"qdswh",
        "益阳歪胡子":"yywhz",
        "长沙跑胡子":"ccphz",
        "四六八红拐弯":"slbhgw",
        "余干麻将": "ygmj",
        "跑得快15张":"runfast15",
        "跑得快16张": "runfast16",
        "红中麻将": "hzmj",
        '长沙麻将':'csmj',
        '转转麻将':"zzmj",
        '衡阳麻将':'hymj',
        '新宁麻将':'xnmj',
        '邵阳麻将':"symj",
        '靖州麻将':'jzmj',
    }
    try:
        return TeamData[team] + PlayData[play]
    except Exception as e:
        msg = ("未能找到 <%s> 玩法进行转换." % play)
        raise msg


#   创建测试脚本文件
def make_test_case_files(team, play, options, operates, cards,mids, _path=None):
    print("操作步骤: %s"%operates)
    file_name_prefix=transform_play(team, play)
    # print("文件名前缀: %s" % file_name_prefix)
    # print("当前文件路径: %s" % get_current_path())
    #   如果是编辑文件的话，先删除之前文件
    if _path != None and os.path.exists(_path):
        print("先删除之前文件.")
        os.remove(_path)
    #   生成文件路径
    generate_file_path = get_current_path() + '/TesterRunner/runner/testcases/'
    # print("generate_file_path: %s" % generate_file_path)
    import datetime
    # print("当前时间: %s" % time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time())))
    # print("当前时间2: %s" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    #   文件名字包含路径
    file_name = '%s_%s.py' % (file_name_prefix, time.strftime('%Y_%m_%d_%H_%M', time.localtime(time.time())))

    write_file(generate_file_path + file_name, team, play, options, operates, cards,mids)

    return generate_file_path + file_name



def update_test_case_file(_path,team, play, options, operates, cards,mids):
    write_file(_path,team, play, options, operates, cards,mids)




#   生成py脚本文件
def write_file(_path, team, play, options, operates, cards,mids):
    end_code = "if __name__=='__main__':\n" \
               "    unittest.main()"
    head_code, fixed_code, disconnect_code, operate_code = script_custom_made(team, play, options, operates, cards,mids)
    try:
        with open(_path, 'w', encoding='utf-8') as file:
            file.write(head_code)
            file.write(fixed_code)
            for code in operate_code:
                file.write(code)
            file.write(disconnect_code)
            file.write(end_code)
    except Exception as e:
        logging.info(e)
        print("in utils.py write_file. 文件写入错误。 <%s> " % _path)
    finally:
        file.close()


# 按照不同项目进行脚本定制化
def script_custom_made(team, play, options, operates, cards,mids):
    logging.info("options %s" % operates)
    TeamTransform = {
        "超越项目组-主版本": chaoyue_master_transform,
        # "超越项目组-岳阳版本": chaoyue_yueyang_transform,
        # "巨浪项目组-湖南麻将版本": julang_hunan_transform,
        #"开心游戏项目组-开心游戏版本": kaixinyouxi_kaixinyouxi_transform,
        # "开心游戏项目组-鄱余万版本": kaixinyouxi_poyuwan_transform,
        #"开心游戏项目组-鹰眼玩法版本": kaixinyouxi_kaixinyouxi_transform,
    }
    try:
        return TeamTransform[team](play, options, operates, cards,mids)
    except Exception as e:
        logging.info('err: {err} (无法找到对应的项目)'.format(err=e))


# 超越项目组脚本定制
def chaoyue_master_transform(play, options, operates, cards,mids):
    # 修改头部导包数据
    try:
        phz_api_import_data = {
            "邵阳字牌",
            "邵阳剥皮",
            "耒阳字牌",
            "娄底放炮罚",
            "湘乡告胡子",
            "衡阳百胡",
            "郴州字牌",
            "衡阳六胡抢",
            "邵阳放炮罚",
            "衡阳十胡卡",
            "攸县碰胡子",
            "常德跑胡子",
            "怀化红拐弯",
            "永丰跑胡子",
            "祁东十五胡",
            "益阳歪胡子",
            "长沙跑胡子",
            "四六八红拐弯",
            "红中麻将",
            "跑得快15张",
            "跑得快16张",
            "长沙麻将",
            "红中麻将",
            "转转麻将",
            "衡阳麻将",
            "新宁麻将",
            "邵阳麻将",
            "靖州麻将",

        }
        import_data = None
        if play in phz_api_import_data:
            import_data = "from chaoyue.master.phz.api import *"
        if import_data is None:
            logging.info("脚本定制: 导包失败.")
            return
        head_code = 'import sys\n' \
                    'import os\n' \
                    'cur_path = os.path.abspath(os.path.dirname(__file__))\n' \
                    'last_path = os.path.split(cur_path)[0]\n' \
                    'last_path_len = last_path.split("/")[-1]\n' \
                    'root_path = last_path[:len(last_path) - len(last_path_len)]\n' \
                    'sys.path.append(root_path)\n' \
                    'import time\n' \
                    'import unittest\n' \
                    '%s\n' \
                    'class PHZTestCase(unittest.TestCase):\n' \
                    '    def test_task(self):\n' % (import_data)
        # 修改fixed_code, 创房选项等
        fixed_code, disconnect_code = transform_fixed_data(options, play, cards, mids)
        logging.info("fixed_code: {}, disconnect_code: {}".format(fixed_code,disconnect_code))
        # 修改操作数据，operate_code
        operate_code = transform_operate_data(play,operates)
        print("ffffffffffffffffff",operate_code)
        return head_code, fixed_code, disconnect_code, operate_code
    except Exception as err:
        logging.info(err)




# 将创房选项进行转换
def transform_fixed_data(options, play, cards,mids):
    MajiangGameNameList = ["长沙麻将", "红中麻将", "转转麻将", "衡阳麻将", '新宁麻将', '邵阳麻将', '靖州麻将']
    logging.info("options: %s\n, play: %s\n,card: %s\n , mids: %s \n" % (options, play,cards,mids))
    users = eval(mids)
    user_mid = []
    create_key = None
    join_romm_type = 0
    if play == "耒阳字牌":
        create_key = "CreateRoomLeiYang(create_room_data)"
    elif play == "益阳歪胡子":
        create_key = "CreateRoomYiYang(create_room_data)"
    else:
        create_key = "CreateRoom(create_room_data)"

    for i in users:
        user_mid.append(int(i))
    if 'o_player' in options:
        player_num = options['o_player']
    else:
        player_num = options['人数']

    if options["roomTypeVuale"] == "俱乐部创房":
        join_romm_type = 1

    if player_num != len(users):
        return "用户mid 和选择人数不一致"
    #     while not player1.now_round_over:\n
    if player_num == 4:
        fixed_code = '        player1 = UserBehavior({user1},{user1},True)\n' \
                     '        player2 = UserBehavior({user2})\n' \
                     '        player3 = UserBehavior({user3})\n' \
                     '        player4 = UserBehavior({user4})\n' \
                     '        time.sleep(2)\n' \
                     '        player1.SetGameType = "{gameType}"\n' \
                     '        player2.SetGameType = "{gameType}"\n' \
                     '        player3.SetGameType = "{gameType}"\n' \
                     '        player4.SetGameType = "{gameType}"\n' \
                     '        create_room_data = {room_data}\n' \
                     '        player1.{room_key}\n' \
                     '        time.sleep(2)\n' \
                     '        cards_data = {card_data}\n' \
                     '        player1.maker_card(cards_data,player1.room_id)\n' \
                     '        time.sleep(2)\n' \
                     '        player2.ApplyEnterRoom(player1.room_id,{romm_type})\n' \
                     '        player3.ApplyEnterRoom(player1.room_id,{romm_type})\n' \
                     '        player4.ApplyEnterRoom(player1.room_id,{romm_type})\n'.format(user1=user_mid[0],
                                                                                user2=user_mid[1],
                                                                                user3=user_mid[2],
                                                                                user4=user_mid[3], gameType=play,
                                                                                room_data=options,
                                                                                room_key=create_key,
                                                                                card_data=cards,
                                                                                romm_type=join_romm_type
                                                                                            )
        disconnect_code = '        time.sleep(5)\n' \
                          '        player1.ConnectClose()\n' \
                          '        player2.ConnectClose()\n' \
                          '        player3.ConnectClose()\n' \
                          '        player4.ConnectClose()\n'

    elif player_num == 3:
        fixed_code = '        player1 = UserBehavior({user1},{user1},True)\n' \
                     '        player2 = UserBehavior({user2})\n' \
                     '        player3 = UserBehavior({user3})\n' \
                     '        time.sleep(2)\n' \
                     '        player1.SetGameType = "{gameType}"\n' \
                     '        player2.SetGameType = "{gameType}"\n' \
                     '        player3.SetGameType = "{gameType}"\n' \
                     '        create_room_data = {room_data}\n' \
                     '        player1.{room_key}\n' \
                     '        time.sleep(2)\n' \
                     '        cards_data = {card_data}\n' \
                     '        player1.maker_card(cards_data,player1.room_id)\n' \
                     '        time.sleep(2)\n' \
                     '        player2.ApplyEnterRoom(player1.room_id,{romm_type})\n' \
                     '        player3.ApplyEnterRoom(player1.room_id,{romm_type})\n'.format(user1=user_mid[0],
                                                                                user2=user_mid[1],
                                                                                user3=user_mid[2], gameType=play,
                                                                                room_data=options,
                                                                                room_key=create_key,
                                                                                card_data=cards,
                                                                                romm_type=join_romm_type)
        disconnect_code = '        time.sleep(5)\n' \
                          '        player1.ConnectClose()\n' \
                          '        player2.ConnectClose()\n' \
                          '        player3.ConnectClose()\n'

    else:
        fixed_code = '        player1 = UserBehavior({user1},{user1},True)\n' \
                     '        player2 = UserBehavior({user2})\n' \
                     '        time.sleep(2)\n' \
                     '        player1.SetGameType = "{gameType}"\n' \
                     '        player2.SetGameType = "{gameType}"\n' \
                     '        create_room_data = {room_data}\n' \
                     '        player1.{room_key}\n' \
                     '        time.sleep(2)\n' \
                     '        cards_data = {card_data}\n' \
                     '        player1.maker_card(cards_data,player1.room_id)\n' \
                     '        time.sleep(2)\n' \
                     '        player2.ApplyEnterRoom(player1.room_id,{romm_type})\n'.format(user1=user_mid[0],
                                                                                user2=user_mid[1], gameType=play,
                                                                                room_data=options,
                                                                                room_key=create_key,
                                                                                card_data=cards,
                                                                                romm_type=join_romm_type)

        disconnect_code = '        time.sleep(5)\n' \
                          '        player1.ConnectClose()\n' \
                          '        player2.ConnectClose()\n'

    return fixed_code, disconnect_code


# 将操作步骤进行转换
def transform_operate_data(play,operate_data):
    MajiangGameNameList = ["长沙麻将", "红中麻将", "转转麻将", "衡阳麻将", '新宁麻将', '邵阳麻将', '靖州麻将']
    operate_code = []
    for data in operate_data:
        print("xxxxx", data)
        if play in MajiangGameNameList:
            if len(data['card']) != 0:
                for i in range(len(data['card'])):
                    data['card'][i] =  data['card'][i] + '\x00'

            code = ''
            for k, v in data.items():

                if k == "users":
                    if '玩家1' == v:
                        code += '        player1.'
                    elif '玩家2' == v:
                        code += '        player2.'
                    elif '玩家3' == v:
                        code += '        player3.'
                    elif '玩家4' == v:
                        code += '        player4.'

                if k == "operation":
                    if v == "出牌":
                        code += "OperateApi('出', '', %s)\n" % data['card']
                    if v == "碰牌":
                        code += "OperateApi('碰')\n"
                    if v == "过牌":
                        code += "OperateApi('过')\n"
                    if v == "胡牌":
                        code += "OperateApi('胡')\n"
                    if v == "吃牌":
                        code += "OperateApi('吃', '', %s)\n" % data['card']
                    if v == "补杠":
                        code += "OperateApi('补杠', '', %s)\n" % data['card']
                    if v == "飘分":
                        code += "OperateApi('飘分', '', %d)\n" % int(data['card'][0])
                    if v =="加锤":
                        code += "OperateApi('加锤', '', %d)\n" % int(data['card'][0])


            operate_code.append(code)
        else:
            code = ''
            for k, v in data.items():
                if k == "users":
                    if '玩家1' == v:
                        code += '        player1.'
                    elif '玩家2' == v:
                        code += '        player2.'
                    elif '玩家3' == v:
                        code += '        player3.'
                    elif '玩家4' == v:
                        code += '        player4.'

                if k == "operation":
                    if v == "出牌":
                        code += "OperateApi('出', '', %s)\n" % data['card']
                        code += '        time.sleep(1)\n'
                    if v == "碰牌":
                        code += "OperateApi('碰')\n"
                        code += '        time.sleep(1)\n'
                    if v == "过牌":
                        code += "OperateApi('过')\n"
                        code += '        time.sleep(1)\n'
                    if v == "胡牌":
                        code += "OperateApi('胡')\n"
                        code += '        time.sleep(1)\n'
                    if v == "吃牌":
                        code += "OperateApi('吃', '', %s)\n" % data['card']
                        code += '        time.sleep(1)\n'
                    
                    if v =="加锤":
                        code += "OperateApi('加锤','','%s')\n" % data['card']
            operate_code.append(code)
    return operate_code



if __name__ == '__main__':
    result = transform_create_room_options("邵阳字牌", {'o_player': 3, 'o_round': 5, 'o_huyideng': '5息一囤', 'o_wanfa': '', 'o_card_num': '抽牌20张'})
    print(result)
