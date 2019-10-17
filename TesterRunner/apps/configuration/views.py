import json
from .models import *
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from apps.utils.DataConversion import *

# Create your views here.
@require_http_methods(['POST'])
def Addcfg(request):
    Data = json.loads(request.body)
    try:
        c_ip = Data["c_ip"]
        c_port = Data["c_port"]
        _remark = Data["c_remake"]
        _info = Server(
            t_ip=c_ip,
            t_port=c_port,
            t_remark=_remark,
        )
        _info.save()
        return HttpResponse('添加成功', content_type="application/json,charset=utf-8")
    except Exception as  err:
        return HttpResponse(err, content_type="application/json,charset=utf-8")


def GetServer():
    _set = []
    _list = Server.objects.all().order_by('-id')
    for ip in _list:
        _set.append({
            "t_id":ip.id,
            "t_ip": ip.t_ip,
            't_port': ip.t_port,
            't_remark': ip.t_remark,
        })
    return _set

def QueryList(request):
    try:
        _set = GetServer()
        return JsonResponse(_set, safe=False)
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")


def Update(request):
    try:
        Data = json.loads(request.body)
        t_id = Data["data"]["id"]
        t_ip = Data["data"]["t_ip"]
        t_port = Data["data"]["t_port"]
        t_remark = Data["data"]["t_remark"]

        result = Server.objects.filter(id=t_id).update(
            t_ip=t_ip,
            t_port=t_port,
            t_remark=t_remark,
        )
        if result:
            return HttpResponse('修改成功.', content_type="application/json,charset=utf-8")
        else:
            return HttpResponse('修改失败.', content_type="application/json,charset=utf-8")

    except Exception as e:
        return HttpResponse('error: %s'%e, content_type="application/json,charset=utf-8")