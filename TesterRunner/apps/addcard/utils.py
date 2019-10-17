from collections import Counter
def checkout_repeating_data(_data):
        try:
            data = eval(_data)
            error_data = []
            data_list = []
            if type(data) is dict:
                for k, v in data.items():
                    if type(v) is not list:
                        return '牌数据错误,不为列表类型'
                    else:
                        for i in v:
                            data_list.append(i)

            elif type(data) is list:
                try:
                    for i in data[0]:
                        for card in i:
                            _card = card.replace(" ","")
                            for num in range(2,len(_card),3):
                                data_list.append(_card[num-2:num])
                except Exception:
                    return "牌数据格式错误"
            count_data = Counter(data_list)
            for val, count_val in count_data.items():
                if count_val > 4:
                    error_data.append(val)
            if len(error_data) is 0:
                return True
            else:
                return ",".join(error_data) + ": 牌数据大于4张"
        except NameError:
            return "不支持该牌数据!"



def Remove_duplicate_data(cards):
    '''去除重复数据'''
    result = {}
    data = []
    if type(cards) is dict:
        for k, v in cards.items():
            for i in v:
                data.append(i[1])
    card_type = list(result.fromkeys(data))
    return sorted(card_type)


