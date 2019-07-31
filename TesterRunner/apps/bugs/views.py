import json
from django.shortcuts import render
from .models import *
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods


# Create your views here.

#   添加Bug
@require_http_methods(['POST'])
def AddBug(request):
    AddData = json.loads(request.body)
    print('request: %s' % AddData)
    date = AddData['b_date']
    user = AddData['b_name']
    _type = AddData['b_type']
    result = AddData['b_result']
    reason = AddData['b_reason']
    solve = AddData['b_solve']

    bug = BugProfile(
        b_date=date,
        b_user=user,
        b_type=_type,
        b_result=result,
        b_reason=reason,
        b_solve=solve
    )
    bug.save()

    print(bug.b_type, _type)
    if bug.b_type == _type:
        return HttpResponse('添加成功', content_type="application/json,charset=utf-8")
    else:
        return HttpResponse('添加失败', content_type="application/json,charset=utf-8")


def GetAllBugs():
    bug_set = []
    bug_list = BugProfile.objects.all()
    for bug in bug_list:
        bug_set.append({
            'b_id': bug.id,
            'b_date': bug.b_date,
            'b_name': bug.b_user,
            'b_type': bug.b_type,
            'b_result': bug.b_result,
            'b_reason': bug.b_reason,
            'b_solve': bug.b_solve,
        })
    return bug_set


#   查询全部bug
def QueryBug(request):
    try:
        bug_set = GetAllBugs()
        # print("query data: %s" % bug_set)
        return JsonResponse(bug_set, safe=False)
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")


def QueryByName(request):
    try:
        name = request.GET['b_name']
        print("name",  name)
        bug_set = []
        bug_list = BugProfile.objects.filter(b_user=name)
        print("bug_list", bug_list)
        for bug in bug_list:
            bug_set.append({
                'b_id': bug.id,
                'b_date': bug.b_date,
                'b_name': bug.b_user,
                'b_type': bug.b_type,
                'b_result': bug.b_result,
                'b_reason': bug.b_reason,
                'b_solve': bug.b_solve,
            })

        print("bug_set: %s" % bug_set)
        return JsonResponse(bug_set, safe=False)
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")

#   根据id修改bug内容
@require_http_methods(['POST'])
def UpdateBug(request):
    AddData = json.loads(request.body)
    print('edit request: %s' % AddData)
    b_id = AddData['b_id']
    date = AddData['b_date']
    user = AddData['b_name']
    _type = AddData['b_type']
    result = AddData['b_result']
    reason = AddData['b_reason']
    solve = AddData['b_solve']

    result = BugProfile.objects.filter(id=b_id).update(
        b_date=date,
        b_user=user,
        b_type=_type,
        b_result=result,
        b_reason=reason,
        b_solve=solve
    )

    if result:
        bug_set = GetAllBugs()
        return JsonResponse(bug_set, safe=False)
    else:
        return HttpResponse('修改失败.', content_type="application/json,charset=utf-8")


def DeleteBug(request):
    b_id = request.GET['b_id']
    del_obj = BugProfile.objects.filter(id=b_id).delete()
    if del_obj:
        bug_set = GetAllBugs()
        print("del-- data: %s" % bug_set)
        return JsonResponse(bug_set, safe=False)
    else:
        return HttpResponse('删除失败.', content_type="application/json,charset=utf-8")
