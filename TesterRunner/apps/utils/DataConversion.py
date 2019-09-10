def conversion_list(msg):
    _list = [[]]
    try:
        m = msg.replace(" ","")
        dict_msg = eval(m)
        for k , v in dict_msg.items():
            definition_list = []
            _val = ",".join(v)
            definition_list.append(_val)
            _list[0].append(definition_list)
        return _list
    except Exception as e:
        return False




