import json
from .models import *
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(['POST'])
def AddDeployIP(request):
    Data = json.loads(request.body)
    print("data: %s" % Data)
    c_ip = Data["c_ip"]
    c_port = Data["c_port"]
    _remark = Data["c_remake"]

    _info = DeployIP(
        t_ip = c_ip,
        t_port = c_port,
        t_remark = _remark,
    )
    _info.save()
    return HttpResponse('添加成功', content_type="application/json,charset=utf-8")

def GetDeployIP():
    _set = []
    _list = DeployIP.objects.all()
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
        _set = GetDeployIP()
        return JsonResponse(_set, safe=False)
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")


def DeleteView(request):
    s_id = request.GET['t_id']
    print(1111111111111111111,s_id)

    del_obj = DeployIP.objects.filter(id=s_id).delete()
    if del_obj:
        _set = GetDeployIP()
        return JsonResponse(_set, safe=False)
    else:
        return HttpResponse('删除失败.', content_type="application/json,charset=utf-8")


def GetIPList(request):
    try:
        deoloy_data =[]
        _set = GetDeployIP()
        for _ip_dict in _set:
            for k,v in _ip_dict.items():
                if k == "t_ip":
                    data = v + ":" + _ip_dict["t_port"]
                    deoloy_data.append(data)

        return JsonResponse(deoloy_data, safe=False)
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")