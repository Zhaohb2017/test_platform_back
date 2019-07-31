import json
from .models import *
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(['POST'])
def AddCasePoint(request):
    Data = json.loads(request.body)
    print("data: %s" % Data)
    _versions = Data["t_version"]  #版本
    _game_module = Data["t_module"]  #游戏模块
    _testcontent = Data["t_content"]  #测试点内容
    _user = Data["t_user"]
    _date = Data["t_date"]
    _storage = Data["t_storage"]
    _usable = Data["t_usable"]
    _img = Data["t_img"]
    _remark = Data["t_remark"]

    case = TestPoint(
        t_version = _versions,
        t_module = _game_module,
        t_content = _testcontent,
        t_user = _user,
        t_date=_date,
        t_storage=_storage,
        t_usable=_usable,
        t_img=_img,
        t_remark=_remark
    )
    case.save()
    return HttpResponse('添加成功', content_type="application/json,charset=utf-8")

def GetPoint():
    t_point_set = []
    t_point_list = TestPoint.objects.all()
    for point in t_point_list:
        t_point_set.append({
            "t_id":point.id,
            't_version': point.t_version,
            't_module': point.t_module,
            't_content': point.t_content,
            't_user': point.t_user,
            't_date': point.t_date,
            't_storage': point.t_storage,
            't_usable': point.t_usable,
            't_img': str(point.t_img),
            't_remark': point.t_remark
        })
    return t_point_set



def QueryTestPoint(request):
    try:
        point_set = GetPoint()
        return JsonResponse(point_set, safe=False)
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")


@require_http_methods(['POST'])
def AddKnowledge(request):
    Data = json.loads(request.body)
    print("data: %s" % Data)
    _data = Data["t_date"]
    _link = Data["t_link"]
    _title = Data["t_title"]

    k = Knowledge(
        t_date=_data,
        t_link=_link,
        t_title=_title,)

    k.save()
    return HttpResponse('添加成功', content_type="application/json,charset=utf-8")



def GetKnowledge():
    knowledge_set = []
    knowledge_list = Knowledge.objects.all()
    for knowledge in knowledge_list:
        knowledge_set.append({
            "t_id":knowledge.id,
            't_date': knowledge.t_date,
            't_link': knowledge.t_link,
            't_title': knowledge.t_title,

        })
    return knowledge_set
def QueryKnowledge(request):
    try:
        GetKnowledg_set = GetKnowledge()
        return JsonResponse(GetKnowledg_set, safe=False)
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")



def DeleteView(request):
    s_id = request.GET['t_id']
    print(1111111111111111111,s_id)

    del_obj = Knowledge.objects.filter(id=s_id).delete()
    if del_obj:
        Knowledge_set = GetKnowledge()
        return JsonResponse(Knowledge_set, safe=False)
    else:
        return HttpResponse('删除失败.', content_type="application/json,charset=utf-8")



def Searchskill(request):
    s_set = []
    title = request.GET['t_title']
    if title == "":
        s_obj = Knowledge.objects.all()
        for skill in s_obj:
            s_set.append({
                't_date': skill.t_date,
                't_link': skill.t_link,
                't_title': skill.t_title,

            })
    else:
        s_obj = Knowledge.objects.filter(t_title__contains=title)
        for skill in s_obj:
            s_set.append({
            't_date': skill.t_date,
            't_link': skill.t_link,
            't_title': skill.t_title,

            })
    try:
        return JsonResponse(s_set, safe=False)
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")



def UpdateSkill(request):
    Data = json.loads(request.body)
    print(1111111111,Data)
    t_id = Data["t_id"]
    _date = Data["t_date"]
    _link = Data["t_link"]
    _title = Data["t_title"]

    result = Knowledge.objects.filter(id=t_id).update(
            t_date=_date,
            t_link=_link,
            t_title=_title,
            )

    if result:
        print(22222222222222222222222)
        _set = GetKnowledge()
        return JsonResponse(_set, safe=False)
    else:
        return HttpResponse('修改失败.', content_type="application/json,charset=utf-8")




def DeleteTestPoint(request):
    s_id = request.GET['c_id']
    print(1111111111111111111,s_id)

    del_obj = TestPoint.objects.filter(id=s_id).delete()
    if del_obj:
        Knowledge_set = GetPoint()
        return JsonResponse(Knowledge_set, safe=False)
    else:
        return HttpResponse('删除失败.', content_type="application/json,charset=utf-8")