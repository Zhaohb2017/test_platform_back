import json
from .models import *
from .conn_server import *
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from apps.utils.DataConversion import *

# Create your views here.
@require_http_methods(['POST'])
def AddDeployIP(request):
    Data = json.loads(request.body)
    c_ip = Data["c_ip"]
    c_port = Data["c_port"]
    c_user = Data["c_user"]
    c_pswd = Data["c_pwd"]
    c_path = Data["c_path"]
    c_filename = Data["c_filename"]
    _remark = Data["c_remake"]
    _info = DeployIP(
        t_ip = c_ip,
        t_user = c_user,
        t_pswd = c_pswd,
        t_path = c_path,
        t_port = c_port,
        t_filename = c_filename,
        t_remark = _remark,
    )
    _info.save()
    return HttpResponse('添加成功', content_type="application/json,charset=utf-8")


@require_http_methods(['POST'])
def Send(request):
    try:
        on = request.GET['on']
        ip = request.GET['ip']
        port = request.GET["port"]
        user = request.GET["user"]
        pwd = request.GET["pwd"]
        path = request.GET["path"]
        filename = request.GET["filename"]
        card = request.GET["card"]

        if filename == "":
            filename = "testcard.json"

        if on == "true":
            card = conversion_list(card)

        comm = "cd {path}/; echo '{data}' >{file}".format(path=path, data=card, file=filename)
        ssh = ssh_connect(ip=str(ip), port=int(port), user=str(user), pswd=str(pwd), command=comm)
     
        if ssh is True:
            return HttpResponse('发送成功', content_type="application/json,charset=utf-8")
        else:
            return HttpResponse(ssh, content_type="application/json,charset=utf-8")
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")



def GetDeployIP():
    _set = []
    _list = DeployIP.objects.all()
    for ip in _list:
        _set.append({
            "t_id":ip.id,
            "t_ip": ip.t_ip,
            't_port': ip.t_port,
            "t_user":ip.t_user,
            "t_pwd": ip.t_pswd,
            "t_path": ip.t_path,
            "t_filename": ip.t_filename,
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
                    data = "ip%s"%_ip_dict["t_id"] +"-"+ v + ":" + _ip_dict["t_port"]
                    deoloy_data.append(data)
        return JsonResponse(deoloy_data, safe=False)
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")

def Search(request):
    ip = request.GET['t_ip']
    s_set = []
    if ip == "":
        s_set = GetDeployIP()
    else:
        s_obj = DeployIP.objects.filter(t_ip__contains=ip)
        for ip in s_obj:
            s_set.append({
                "t_id": ip.id,
                "t_ip": ip.t_ip,
                't_port': ip.t_port,
                "t_user": ip.t_user,
                "t_pwd": ip.t_pswd,
                "t_path": ip.t_path,
                "t_filename": ip.t_filename,
                't_remark': ip.t_remark,
            })
    try:
        return JsonResponse(s_set, safe=False)
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")

