import json
from .models import *
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from .set_cardtype_utils import *
from .utils import *
from django.db.models import Q
from apps.log.models import *

def searchCard(request):
    #<供游戏前端使用>
    try:
        s_set = {}
        key = None
        c_id = request.GET['api']
        for k, v in eval(c_id).items():
            if k == "t_play":
                key = v
        s_obj = AddGameCard.objects.filter(id__contains=key)
        for card in s_obj:
            s_set = {
                "msg": "",
                "t_id": card.id,
                "t_versions": card.c_versions,
                "t_method": card.c_method,
                't_card': card.c_card,
                "t_remark": card.c_remark,
            }
        if len(s_set) is 0:
            if key is not None:
                if type(int(key)) is not int:
                    rep = {"msg": "查询id不能为非数字"}
                    return JsonResponse(rep, safe=False)

            rep = {"msg": "id 找不到"}
            return JsonResponse(rep, safe=False)

        else:
            card_type = Remove_duplicate_data(s_set["t_card"])
            if len(card_type) is 2:
                s_set["card_type"] = 1   # 1代表跑胡子    2，代表麻将    3 代表跑得快
            elif len(card_type) is 4:
                if card_type == ['c', 'd', 'h', 's']:
                    s_set["card_type"] = 3
            else:
                s_set["card_type"] = 2


            return JsonResponse(s_set, safe=False)
    except ValueError:
        rep = {"msg": "查询id不能为非数字"}
        return JsonResponse(rep, safe=False)


def addCard(request):
    # <供游戏前端使用>
    data = request.GET['api']
    request_data = ""
    str_data = data
    index = data.find("card")
    index += 6
    request_data += str_data[:index]
    request_data +="'"
    request_data += str_data[index+1:-2]
    request_data += "'"
    request_data += str_data[-1]


    c_versions = None
    c_method = None
    c_card = None
    c_remark = ""
    try:
        for k, v in eval(request_data).items():
            if k == "versions":
                c_versions = v
            if k == "title":
                c_method = v
            if k == "card":
                c_card = v
            if k == "remark":
                c_remark = v

        if c_versions is None or c_versions is "":
            rep = {"code": 300, "msg": '游戏版本不能为空'}
            return JsonResponse(rep, safe=False)
        elif c_method is None or c_method is "":
            rep = {"code": 300, "msg": '标题不能为空'}
            return JsonResponse(rep, safe=False)
        elif c_card is None or c_card is "":
            rep = {"code": 300, "msg": '牌数据不能为空'}
            return JsonResponse(rep, safe=False)

        # 判断是否存在该数据
        is_card = AddGameCard.objects.filter(c_card=c_card)
        if len(is_card) is not 0:
            rep = {"code": 300, "msg": "牌数据重复，不能添加！"}
            return JsonResponse(rep, safe=False)

        card = AddGameCard.objects.get_or_create(
            c_versions=c_versions,
            c_method=c_method,
            c_card=c_card,
            c_remark=c_remark,
        )
        if card[1] is True:
            rep = {"code": 200, "msg": ""}
            return JsonResponse(rep, safe=False)
        elif card[1] is False:
            rep = {"code": 200, "msg": "改数据已存在"}
            return JsonResponse(rep, safe=False)

    except Exception as err:
        rep = {"code": 300, "msg": err}
        return JsonResponse(rep, safe=False)



# Create your views here.
@require_http_methods(['POST'])
def Update_Card(request):
    Data = json.loads(request.body)
    Data = Data['data']
    _id = Data["t_id"]
    c_versions = Data["t_versions"]
    c_method = Data["t_method"]
    c_card = Data["t_card"]
    c_remark = Data["t_remark"]
    c_card = c_card.replace(" ", "")
    result = AddGameCard.objects.filter(id=_id).update(
        c_versions=c_versions,
        c_method=c_method,
        c_card=c_card,
        c_remark=c_remark,
    )
    if result:
        case_set = GetAllCard()
        return JsonResponse(case_set, safe=False)
    else:
        return HttpResponse('修改失败.', content_type="application/json,charset=utf-8")



# Create your views here.
@require_http_methods(['POST'])
def Add_Card(request):
    Data = json.loads(request.body)
    c_versions = Data["c_vsersion"]
    c_method = Data["c_gameMethod"]
    c_card = Data["c_gameCard"]
    c_remark = Data["c_remark"]
    c_card = c_card.replace(" ", "")
    try:
        # 判断该牌数据是否存在
        is_card = AddGameCard.objects.filter(c_card=c_card)
        if len(is_card) is not 0:
            rep = {"code": 300, "msg": "牌数据重复，不能添加！"}
            return JsonResponse(rep, safe=False)

        if type(eval(c_card)) is dict:
            # checkout = checkout_repeating_data(c_card)
            # if checkout is True:

            card = AddGameCard.objects.get_or_create(
                c_versions=c_versions,
                c_method=c_method,
                c_card=c_card,
                c_remark=c_remark,
            )
            if card[1] is True:
                rep = {"code": 200, "msg": "添加成功"}
                return HttpResponse(json.dumps(rep), content_type="application/json,charset=utf-8")
            elif  card[1] is False:
                rep = {"code": 200, "msg": "改数据已存在"}
                return HttpResponse(json.dumps(rep), content_type="application/json,charset=utf-8")

            # else:
            #     rep = {"code": 300, "msg": checkout}
            #     return HttpResponse(json.dumps(rep), content_type="application/json,charset=utf-8")

        else:
            # checkout = checkout_repeating_data(c_card)   #校验牌数据是否大于4张
            # if checkout is True:
            card = AddGameCard.objects.get_or_create(
                c_versions=c_versions,
                c_method=c_method,
                c_card=c_card,
                c_remark=c_remark,
            )
            if card[1] is True:
                rep = {"code": 200, "msg": '添加非JSON格式成功'}
                return HttpResponse(json.dumps(rep), content_type="application/json,charset=utf-8")
            elif  card[1] is False:
                rep = {"code": 200, "msg": "改数据已存在"}
                return HttpResponse(json.dumps(rep), content_type="application/json,charset=utf-8")

            # else:
            #     rep = {"code": 300, "msg": checkout}
            #     return HttpResponse(json.dumps(rep), content_type="application/json,charset=utf-8")

    except Exception as e:
        rep = {"code": 300, "msg": '请输入json格式数据'}
        return HttpResponse( json.dumps(rep), content_type="application/json,charset=utf-8")



def GetAllCard():
    _set = []
    Addcard_list = AddGameCard.objects.all().order_by('-id')
    for Addcard in Addcard_list:
        _set.append({
            "t_id":Addcard.id,
            "t_versions":Addcard.c_versions,
            "t_method":Addcard.c_method,
            't_card': Addcard.c_card,
            "t_remark":Addcard.c_remark,
        })
    return _set
def QueryAllCard(request):
    try:
        GetCard_set = GetAllCard()
        return JsonResponse(GetCard_set, safe=False)
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")


def Search(request):
    s_set = []
    method = request.GET['t_play']
    search_data = eval(method)
    '''删除空值'''
    for key in list(search_data.keys()):
        if not search_data.get(key):
            search_data.pop(key)

    if len(search_data) is not 0:
        '''<功能>支持模糊查询'''
        if len(search_data) is 1 and list(search_data.keys())[0] == "c_remark":
            s_obj = AddGameCard.objects.filter(Q(c_remark__contains=list(search_data.values())[0]))
            for card in s_obj:
                s_set.append({
                    "t_id": card.id,
                    "t_versions": card.c_versions,
                    "t_method": card.c_method,
                    't_card': card.c_card,
                    "t_remark": card.c_remark,
                })
        
        else:
            print("fffffffffff",search_data)
            s_obj = AddGameCard.objects.filter(**search_data)
            for card in s_obj:
                s_set.append({
                    "t_id": card.id,
                    "t_versions": card.c_versions,
                    "t_method": card.c_method,
                    't_card': card.c_card,
                    "t_remark": card.c_remark,
                })
    try:
        return JsonResponse(s_set, safe=False)
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")


def DeleteView(request):
    s_id = request.GET['t_id']

    del_obj = AddGameCard.objects.filter(id=s_id).delete()
    if del_obj:
        _set = GetAllCard()
        return JsonResponse(_set, safe=False)
    else:
        return HttpResponse('删除失败.', content_type="application/json,charset=utf-8")
@require_http_methods(['POST'])
def putCardInTheRoom(request):
    try:
        c_server = request.GET['c_server']
        c_port = request.GET['c_port']
        c_roomID = request.GET["c_roomID"]
        c_card = request.GET["c_card"]
        c_user = request.GET["c_user"]

        info_data = "{0}:{1}--------->> send room id<{2}> the card: {3}".format(c_server,c_port,c_roomID,c_card)
        info = LogInfo(user=c_user,info=info_data)
        info.save()

        card = c_card.replace(" ","")
        if type(eval(card)) is list:
            card = data_list(eval(card))
            if card is False:
                return HttpResponse('list错误,配置失败. 找平台开发寻求帮助！', content_type="application/json,charset=utf-8")

        runfast_player = runfast_checkout(eval(card))
        if runfast_player is False:
            return HttpResponse('跑得快数据不能进行配置', content_type="application/json,charset=utf-8")

        put_in_ = put_in_the_room(c_server,c_port,json.loads(card),c_roomID)
        if put_in_:

            return HttpResponse('配置成功', content_type="application/json,charset=utf-8")
        else:
            return HttpResponse(put_in_the_room, content_type="application/json,charset=utf-8")
    except Exception as Err:
        return HttpResponse(Err, content_type="application/json,charset=utf-8")



