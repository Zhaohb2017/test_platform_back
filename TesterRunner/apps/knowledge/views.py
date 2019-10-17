import json
from .models import *
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.db.models import Q

# Create your views here.
@require_http_methods(['POST'])
def AddCasePoint(request):
    Data = json.loads(request.body)
    _versions = Data["t_version"]  #版本
    _game_module = Data["t_module"]  #游戏模块
    _testcontent = Data["t_content"]  #测试点内容
    _user = Data["t_user"]
    _date = Data["t_date"]
    _storage = Data["t_storage"]
    _usable = Data["t_usable"]
    _img = Data["t_img"]
    _remark = Data["t_remark"]


    if _storage == "未入库":
        _storage = 1
    else:
        _storage = 0

    if _usable == "未失效":
        _usable = 1
    else:
        _usable = 0


    case = TestPoint(
        t_version = _versions,
        t_module = _game_module,
        t_content = _testcontent,
        t_user = _user,
        t_date=_date,
        t_storage=_storage,
        t_usable=_usable,
        t_img=_img,
        t_remark=_remark,
    )
    case.save()
    return HttpResponse('添加成功', content_type="application/json,charset=utf-8")

def GetPoint():
    t_point_set = []
    t_storage = ''
    t_usable = ""
    t_point_list = TestPoint.objects.all().order_by('-id')
    for point in t_point_list:
        if point.t_storage is 1:
            t_storage = "未入库"
        else:
            t_storage = "已入库"

        if point.t_usable is 1:
            t_usable = "未失效"
        else:
            t_usable = "已失效"
        t_point_set.append({
            "t_id":point.id,
            't_version': point.t_version,
            't_module': point.t_module,
            't_content': point.t_content,
            't_user': point.t_user,
            't_date': point.t_date,
            't_storage': t_storage,
            't_usable': t_usable,
            't_img': str(point.t_img),
            't_remark': point.t_remark
        })
    return t_point_set

def UpdateTestPoint(request):
    Data = json.loads(request.body)
    _versions = Data['data']["t_version"]  # 版本
    _game_module = Data['data']["t_module"]  # 游戏模块
    _testcontent = Data['data']["t_content"]  # 测试点内容
    _user = Data['data']["t_user"]
    _date = Data['data']["t_date"]
    _storage = Data['data']["t_storage"]
    _usable = Data['data']["t_usable"]
    _img = Data['data']["t_img"]
    _remark = Data['data']["t_remark"]
    t_id = Data['data']["t_id"]

    if _storage == "未入库":
        _storage = 1
    else:
        _storage = 0

    if _usable == "未失效":
        _usable = 1
    else:
        _usable = 0
    result = TestPoint.objects.filter(id=t_id).update(
        t_version=_versions,
        t_module=_game_module,
        t_content=_testcontent,
        t_user=_user,
        t_date=_date,
        t_storage=_storage,
        t_usable=_usable,
        t_img=_img,
        t_remark=_remark
            )

    if result:
        _set = GetPoint()
        return JsonResponse(_set, safe=False)
    else:
        return HttpResponse('修改失败.', content_type="application/json,charset=utf-8")

def SearchTestPoint(request):
    try:
        s_set = []
        s_obj = None
        t_storage = ""
        t_usable = ""
        request_data = request.GET['data']
        if request_data == "未入库":
            s_obj = TestPoint.objects.filter(t_storage=1)
        elif request_data == "已入库":
            s_obj = TestPoint.objects.filter(Q(t_storage__contains=0))
        elif request_data == "未失效":
            s_obj = TestPoint.objects.filter(Q(t_usable__contains=1))
        elif request_data == "已失效":
            s_obj = TestPoint.objects.filter(Q(t_usable__contains=0))

        if s_obj is not None:
            for point in s_obj:
                if point.t_storage is 1:
                    t_storage = "未入库"
                else:
                    t_storage = "已入库"

                if point.t_usable is 1:
                    t_usable = "未失效"
                else:
                    t_usable = "已失效"
                s_set.append({
                    "t_id": point.id,
                    't_version': point.t_version,
                    't_module': point.t_module,
                    't_content': point.t_content,
                    't_user': point.t_user,
                    't_date': point.t_date,
                    't_storage': t_storage,
                    't_usable': t_usable,
                    't_img': str(point.t_img),
                    't_remark': point.t_remark
                })
            return JsonResponse(s_set, safe=False)

        if request_data == "":
            s_set = GetPoint()
        else:
            s_obj = TestPoint.objects.filter(Q(t_version__contains=request_data) | Q(t_module__contains=request_data)|Q(t_content__contains=request_data)
                                           )
            for point in s_obj:
                if point.t_storage is 1:
                    t_storage = "未入库"
                else:
                    t_storage = "已入库"

                if point.t_usable is 1:
                    t_usable = "未失效"
                else:
                    t_usable = "已失效"
                s_set.append({
                    "t_id": point.id,
                    't_version': point.t_version,
                    't_module': point.t_module,
                    't_content': point.t_content,
                    't_user': point.t_user,
                    't_date': point.t_date,
                    't_storage': t_storage,
                    't_usable': t_usable,
                    't_img': str(point.t_img),
                    't_remark': point.t_remark

                })
        return JsonResponse(s_set, safe=False)
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")

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
    knowledge_list = Knowledge.objects.all().order_by('-id')
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
        s_obj = Knowledge.objects.all().order_by('-id')
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
        _set = GetKnowledge()
        return JsonResponse(_set, safe=False)
    else:
        return HttpResponse('修改失败.', content_type="application/json,charset=utf-8")




def DeleteTestPoint(request):
    s_id = request.GET['c_id']

    del_obj = TestPoint.objects.filter(id=s_id).delete()
    if del_obj:
        Knowledge_set = GetPoint()
        return JsonResponse(Knowledge_set, safe=False)
    else:
        return HttpResponse('删除失败.', content_type="application/json,charset=utf-8")

@require_http_methods(['POST'])
def AddTestCase(request):
    try:
        Data = json.loads(request.body)
        versions = Data["s_versions"]
        module = Data["s_module"]
        testpointVal = Data["s_testpointVal"]
        precondition = Data["s_precondition"]
        step = Data["s_step"]
        expectedResult = Data["s_expectedResult"]
        actualResults = Data["s_actualResults"]
        _pass = Data["s_pass"]
        s_effective = Data["s_effective"]
        remark = Data["s_remark"]
        username = Data['s_username']
        k = AddCase.objects.get_or_create(
            t_versions=versions,
            t_module=module,
            t_testpointVal=testpointVal,
            t_precondition=precondition,
            t_step = step,
            t_expectedResult = expectedResult,
            t_actualResults = actualResults,
            t_pass = _pass,
            t_effective = s_effective,
            t_remark = remark,
            t_username = username

        )
        if k[1] is True:
            return HttpResponse('添加成功', content_type="application/json,charset=utf-8")
        else:
            return HttpResponse('重复数据，添加失败！', content_type="application/json,charset=utf-8")


    except Exception as e:
        return HttpResponse('添加失败: %s'%e, content_type="application/json,charset=utf-8")

def GetTestCaseList():
    _set = []
    c_list = AddCase.objects.all().order_by('-id')
    for case in c_list:
        _set.append({
            "t_id": case.id,
            "t_versions": case.t_versions,
            't_module': case.t_module,
            't_testpointVal': case.t_testpointVal,
            't_precondition': case.t_precondition,
            't_step': case.t_step,
            't_expectedResult': case.t_expectedResult,
            't_actualResults': case.t_actualResults,
            't_pass': case.t_pass,
            't_effective': str(case.t_effective),
            't_remark': case.t_remark,
            "t_username": case.t_username
        })
    return _set


def QueryTestCase(request):
    try:
        case_set = GetTestCaseList()
        return JsonResponse(case_set, safe=False)
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")

def DeleteCase(request):
    try:
        id = request.GET['t_id']
        del_obj = AddCase.objects.filter(id=id).delete()
        if del_obj:
            _set = GetTestCaseList()
            return JsonResponse(_set, safe=False)
        else:
            return HttpResponse('删除失败.', content_type="application/json,charset=utf-8")
    except Exception as e:
        return HttpResponse('error: %s'%e, content_type="application/json,charset=utf-8")


def UpdateTestCase(request):
    try:
        Data = json.loads(request.body)
        t_id = Data["data"]["id"]
        versions = Data["data"]["s_versions"]
        module = Data["data"]["s_module"]
        precondition = Data["data"]["s_precondition"]
        step = Data["data"]["s_step"]
        expectedResult = Data["data"]["s_expectedResult"]
        actualResults = Data["data"]["s_actualResults"]
        _pass = Data["data"]["s_pass"]
        s_effective = Data["data"]["s_effective"]
        remark = Data["data"]["s_remark"]
        result = AddCase.objects.filter(id=t_id).update(
            t_versions=versions,
            t_module=module,
            t_precondition=precondition,
            t_step=step,
            t_expectedResult=expectedResult,
            t_actualResults=actualResults,
            t_pass=_pass,
            t_effective=s_effective,
            t_remark=remark
        )
        if result:
            return HttpResponse('修改成功.', content_type="application/json,charset=utf-8")
        else:
            return HttpResponse('修改失败.', content_type="application/json,charset=utf-8")

    except Exception as e:
        return HttpResponse('error: %s'%e, content_type="application/json,charset=utf-8")



def SearchTestCase(request):
    try:
        s_set = []
        request_data = request.GET['data']

        search_data = eval(request_data)
        if request_data == "":
            pass

        else:

            versions = ""
            module = ""
            testpoint = ""
            for k,v in search_data.items():
                if k=="versions":
                    versions = v
                elif k == "module":
                    module = v
                elif k =="testpoint":
                    testpoint= v

            data = {}
            if versions != "":
                data["t_versions"] = versions
            if module != "":
                data["t_module"] = module
            if testpoint != "":
                data["t_testpointVal"] = testpoint

            if len(data) is not 0:
                s_obj = AddCase.objects.filter(**data)
                for case in s_obj:
                    s_set.append({
                        "t_id": case.id,
                        "t_versions": case.t_versions,
                        't_module': case.t_module,
                        't_testpointVal': case.t_testpointVal,
                        't_precondition': case.t_precondition,
                        't_step': case.t_step,
                        't_expectedResult': case.t_expectedResult,
                        't_actualResults': case.t_actualResults,
                        't_pass': case.t_pass,
                        't_effective': str(case.t_effective),
                        't_remark': case.t_remark
                    })
            else:
                s_set = GetTestCaseList()
              
        return JsonResponse(s_set, safe=False)
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")


@require_http_methods(['POST'])
def BatchProduce(request):
    caseFactor = ["版本","模块","测试点","前置条件","操作步骤","预期结果","实际结果","是否通过","是否有效","备注"]
    try:
        excel_null = []
        Data = json.loads(request.body)
        excel_data = Data["data"]
        username = Data['username']
        index = 1
        for d_excel in excel_data:
            index += 1
            retD = list(set(caseFactor).difference(set(list(d_excel.keys()))))
            print("retD,,,,,,",retD)
            if "版本" in retD:
                resp = {"code": 200, "msg": "excel<{index}>行没有<版本>这个数据".format(index=index)}
                return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")
            if "模块"  in retD:
                resp = {"code": 200, "msg": "excel<{index}>行没有<模块>这个数据".format(index=index)}
                return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")
            if "测试点"  in retD:
                resp = {"code": 200, "msg": "excel<{index}>行没有<测试点>这个数据".format(index=index)}
                return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")
            if "操作步骤"  in retD:
                resp = {"code": 200, "msg": "excel<{index}>行没有<操作步骤>这个数据".format(index=index)}
                return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")
            if "预期结果"  in retD:
                resp = {"code": 200, "msg": "excel<{index}>行没有<预期结果>这个数据".format(index=index)}
                return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")
            if "备注" in retD:
                d_excel["备注"] = ""

            if "是否通过" in retD:
                d_excel["是否通过"] = ""

            if "前置条件" in retD:
                d_excel["前置条件"] = ""

            if "是否有效" in retD:
                d_excel["是否有效"] = ""

            if "预期结果" in retD:
                d_excel["预期结果"] = ""
            if "实际结果" in retD:
                d_excel["实际结果"] = ""
            excel_null.append(d_excel)

        add_index = 0
        add_list = []
        for data in excel_null:
            add_index += 1
            versions = data["版本"]
            module = data["模块"]
            testpointVal = data["测试点"]
            precondition = data["前置条件"]
            step = data["操作步骤"]
            expectedResult = data["预期结果"]
            actualResults = data["实际结果"]
            is_pass = data["是否通过"]
            effective = data["是否有效"]
            remark = data["备注"]
            # get_or_create 防止提交重复数据
            k = AddCase.objects.get_or_create(
                t_versions=versions,
                t_module=module,
                t_testpointVal=testpointVal,
                t_precondition=precondition,
                t_step=step,
                t_expectedResult=expectedResult,
                t_actualResults=actualResults,
                t_pass=is_pass,
                t_effective=effective,
                t_remark=remark,
                t_username = username,
            )
            if k[1] is False:
                add_list.append(str(add_index))

        if len(add_list) is 0:
            resp = {"code": 200, "msg": "批量导入成功", }
            return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")
        else:
            print("FFFF",add_list)
            resp = {"code": 200, "msg": ','.join(add_list)+'列：数据重复!，其余数据导入成功！' }
            return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")

    except Exception as err:
        resp = {"code": 301, "msg": err, }
        return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")


def PageDelete(request):
    try:
        id_list = eval(request.GET["id"])
        for id in id_list:
            del_obj = AddCase.objects.filter(id=id).delete()
        _set = GetTestCaseList()
        return JsonResponse(_set, safe=False)
    except Exception as err:
        return HttpResponse(err, content_type="application/json,charset=utf-8")











