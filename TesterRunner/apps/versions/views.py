import json
from .models import *
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods


# Create your views here.
@require_http_methods(['POST'])
def Add_Versions(request):
    Data = json.loads(request.body)
    c_title = Data["t_title"]
    c_link = Data["t_link"]
    c_remark = Data["t_remark"]
    try:
            info = AddVersions(
                c_versions=c_title,
                c_link=c_link,
                c_remark=c_remark,
            )
            info.save()
            return HttpResponse('添加成功', content_type="application/json,charset=utf-8")

    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")


def GetAllVersions():
    _set = []
    _list = AddVersions.objects.all()
    for bug in _list:
        _set.append({
            "t_id":bug.id,
            't_link': bug.c_link,
            't_title': bug.c_versions,
            't_remark': bug.c_remark,
        })
    return _set


#   查询全部bug
def Query(request):
    try:
        _set = GetAllVersions()
        return JsonResponse(_set, safe=False)
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")

def Search(request):
    title = request.GET['t_title']
    s_set = []
    if title == "":
        s_set = GetAllVersions()
    else:
        s_obj = AddVersions.objects.filter(c_versions__contains=title)
        for s in s_obj:
            s_set.append({
                "t_id": s.id,
                't_link': s.c_link,
                't_title': s.c_versions,
                't_remark': s.c_remark,
            })
    try:
        return JsonResponse(s_set, safe=False)
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")


def DeleteView(request):
    s_id = request.GET['t_id']

    del_obj = AddVersions.objects.filter(id=s_id).delete()
    if del_obj:
        _set = GetAllVersions()
        return JsonResponse(_set, safe=False)
    else:
        return HttpResponse('删除失败.', content_type="application/json,charset=utf-8")