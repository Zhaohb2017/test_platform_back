import json
from .models import *
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from .set_cardtype_utils import *

# Create your views here.
@require_http_methods(['POST'])
def Add_Card(request):
    Data = json.loads(request.body)
    c_versions = Data["c_vsersion"]
    c_method = Data["c_gameMethod"]
    c_card = Data["c_gameCard"]
    c_remark = Data["c_remark"]
    try:
        if type(eval(c_card.replace(" ", ""))) is dict:
            card = AddGameCard(
                c_versions=c_versions,
                c_method=c_method,
                c_card=c_card,
                c_remark=c_remark,
            )
            card.save()
            return HttpResponse('添加成功', content_type="application/json,charset=utf-8")
        else:
            card = AddGameCard(
                c_versions=c_versions,
                c_method=c_method,
                c_card=c_card,
                c_remark=c_remark,
            )
            card.save()
            return HttpResponse('添加非JSON格式成功', content_type="application/json,charset=utf-8")
            # return HttpResponse('请输入json格式数据', content_type="application/json,charset=utf-8")
    except Exception as e:
        return HttpResponse('请输入json格式数据', content_type="application/json,charset=utf-8")



def GetAllCard():
    _set = []
    Addcard_list = AddGameCard.objects.all()
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
    if method == "":
        s_obj = AddGameCard.objects.all()
        for card in s_obj:
            s_set.append({
                't_method': card.c_method,
                't_card': card.c_card,
            })
    else:
        s_obj = AddGameCard.objects.filter(c_method__contains=method)
        for card in s_obj:
            s_set.append({
                't_method': card.c_method,
                't_card': card.c_card,
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
        card = c_card.replace(" ","")
        put_in_ = put_in_the_room(c_server,c_port,json.loads(card),c_roomID)
        if put_in_:
            return HttpResponse('配置成功', content_type="application/json,charset=utf-8")
        else:
            return HttpResponse(put_in_the_room, content_type="application/json,charset=utf-8")
    except Exception as Err:
        return HttpResponse(Err, content_type="application/json,charset=utf-8")



