import json
from .models import *
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(['POST'])
def Add_Card(request):
    Data = json.loads(request.body)
    print("data: %s" % Data)
    c_method = Data["c_gameMethod"]
    c_card = Data["c_gameCard"]
    c_remark = Data["c_remark"]
    card = AddGameCard(
        c_method = c_method,
        c_card = c_card,
        c_remark = c_remark,
    )
    card.save()
    return HttpResponse('添加成功', content_type="application/json,charset=utf-8")


def GetAllCard():
    _set = []
    Addcard_list = AddGameCard.objects.all()
    for Addcard in Addcard_list:
        _set.append({
            "t_id":Addcard.id,
            "t_method":Addcard.c_method,
            't_card': Addcard.c_card,
            "t_remark":Addcard.c_remark,
        })
    return _set
def QueryAllCard(request):
    try:
        GetCard_set = GetAllCard()
        print("11111111111",GetCard_set)
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