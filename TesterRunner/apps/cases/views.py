import json
import os
import datetime
import time
import subprocess
from .models import *
from .utils import *
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
# Create your views here.

@require_http_methods(['POST'])
def AddCaseView(request):
    Data = json.loads(request.body)
    _mid = None
    not_Paohuzi = ['红中麻将',"长沙麻将","转转麻将","衡阳麻将","新宁麻将","邵阳麻将","靖州麻将","跑得快15张","跑得快16张"]
    runfast = ["跑得快15张","跑得快16张"]

    print("data: %s" % Data)
    _date = Data['c_date']  # 提交日期
    _name = Data['c_name']  # 提交人
    _project = Data['c_project']  # 项目组
    _play = Data['c_play']  # 项目玩法
    _purpose = Data['c_purpose']  # 测试目的
    _options = Data['c_options']  # 创房选项
    _steps = Data['c_steps']  # 操作步骤
    _remake = Data['c_remake']  # 备注
    _cards = Data['c_cards']  # 做牌数据

    print("ffffffffff",_steps,type(_steps))



    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  用户mid校验  <<<<<<<<<<<<<<<<<<<<<<<<
    try:
        _accounts = Data["c_account"]  # 用户mid
        mid = _accounts.replace(" ","")
        _mid = mid   #赋值
        users = eval(mid)

        if type(users) is not list:
            resp = {"code":300,"Msg":"用户mid错误!请输入例:[127843,127864]"}
            return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")
        else:
            if len(users) != _options["o_player"]:
                resp = {"code": 300, "Msg": "用户mid数量和创房选项人数不一致"}
                return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")
            for i in users:
                if type(i) is not int:
                    resp = {"code": 300, "Msg": "mid请输入数字类型"}
                    return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")
    except Exception as err:
        resp = {"code":300,"Msg":err}  #"用户mid错误!请输入例:[127843,123465]"
        return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  牌数据校验  <<<<<<<<<<<<<<<<<<<<<<<<
    try:
        card = _cards.replace(" ", "")
        if type(eval(card)) != dict:
            resp = {"code": 300, "Msg": "牌数据请输入JSON格式数据"}
            return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")

    except Exception as errro:
        resp = {"code": 300, "Msg": "牌数据请输入JSON格式数据"}
        return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  操作步骤牌数据  <<<<<<<<<<<<<<<<<<<<<<<<
    index = 0
    if _play not in runfast: # 非跑得快玩法
        for data in _steps:
            index += 1
            for k, v in data.items():
                if k == "operation":
                    if data['users'] == "":
                        resp = {"code": 300, "Msg": "操作步骤:第{}列，请选择玩家 ".format(index)}
                        return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")

                    if v == "出牌" or v =="补杠":
                        if len(data['card']) != 1:
                            resp = {"code": 300, "Msg": "操作步骤:第{}列， {}:{},牌数据只能为一张".format(index,data['users'], v)}
                            return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")
                    elif v == "吃牌":
                        if len(data['card']) not in [3,6,9]:
                            resp = {"code": 300, "Msg": "操作步骤:第{}列， {}:{},牌数据只能为3,6,9张".format(index, data['users'], v)}
                            return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")

                elif k == "in_jiachui":
                    data['card'] = v


    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>跑胡子操作步骤牌数据校验<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # 判断是否有加锤

    options_dict = None  # #创房选项
    operate_list = None  # 操作步骤
    if type(_options) is dict:
        options_dict = _options
    else:
        options_dict = eval(_options)

    if type(_steps) is list:
        operate_list = _steps
    else:
        operate_list = eval(_steps)

    for k, v in options_dict.items():
        if k == "o_jiachui":
            if v is True:
                if len(operate_list) is 0:
                    resp = {"code": 300, "Msg": "有加锤选项，请玩家选择是否加锤"}
                    return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")
                else:

                    try:
                        index = 0
                        for i in range(len(users)):
                            index += 1
                            for k, v in operate_list[i].items():
                                if k == "operation":
                                    if v != "加锤":
                                        resp = {"code": 300, "Msg": "第{}个玩家请选择是否加锤".format(i + 1)}
                                        return HttpResponse(json.dumps(resp),
                                                            content_type="application/json,charset=utf-8")

                    except IndexError:
                        resp = {"code": 300, "Msg": "玩家{}没有选择加锤".format(index)}
                        return HttpResponse(json.dumps(resp),
                                            content_type="application/json,charset=utf-8")




    print(2222222222222222222222222222)
    #   创建测试用例脚本文件
    file_name = make_test_case_files(_project, _play, _options, _steps, _cards, _mid)
    if file_name:
        is_local = 1
    else:
        is_local = 0



    case = CasesProfile(
        c_date=_date,
        c_user=_name,
        c_project=_project,
        c_purpose=_purpose,
        c_play=_play,
        c_cards=_cards,
        c_option=_options,
        c_operate=_steps,
        c_is_local=is_local,
        c_remake=_remake,
        c_name=file_name,
        c_account=_mid,
    )
    case.save()

    if case.c_operate == _steps:
        return HttpResponse('添加成功', content_type="application/json,charset=utf-8")
    else:
        return HttpResponse('添加失败', content_type="application/json,charset=utf-8")





def GetAllCase():
    case_set = []
    option_dict = []
    case_list = CasesProfile.objects.all().order_by('-id')
    for case in case_list:
        case_set.append({
            'c_id': case.id,
            'c_date': case.c_date,
            'c_name': case.c_user,
            'c_project': case.c_project,
            'c_purpose': case.c_purpose,
            'c_play': case.c_play,
            'c_cards': case.c_cards,
            'c_option': case.c_option,
            'c_operate': case.c_operate,
            'c_is_local': case.c_is_local,
            'c_remake': case.c_remake,
            'c_file_name': case.c_name,
            'isRunning': False,
        })
    return case_set


def QueryAllView(request):
    try:
        case_set = GetAllCase()
        return JsonResponse(case_set, safe=False)
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")


def QueryByParams(request):
    try:
        project = request.GET['c_project']
        version = request.GET['c_version']
        play = request.GET['c_play']
        project = project + '-' + version  # 数据库中c_project字段值是 project_version拼接起来的
        case_list = CasesProfile.objects.filter(c_project=project, c_play=play).order_by('-id')
        case_set = []
        option = None
        if len(case_list) == 0:
            for case in case_list:
                case_set.append({
                    'c_id': case.id,
                    'c_date': case.c_date,
                    'c_name': case.c_user,
                    'c_project': case.c_project,
                    'c_purpose': case.c_purpose,
                    'c_play': case.c_play,
                    'c_cards': case.c_cards,
                    'c_option': case.c_option,
                    'c_operate': case.c_operate,
                    'c_is_local': case.c_is_local,
                    'c_remake': case.c_remake,
                    'c_file_name': case.c_name,
                    'isRunning': False,
                    'c_mid': case.c_account,
                })
            return JsonResponse(case_set, safe=False)

        else:
            for case in case_list:
                option = case.c_option
                print(case)
                case_set.append({
                    'c_id': case.id,
                    'c_date': case.c_date,
                    'c_name': case.c_user,
                    'c_project': case.c_project,
                    'c_purpose': case.c_purpose,
                    'c_play': case.c_play,
                    'c_cards': case.c_cards,
                    'c_option': eval(case.c_option),
                    'c_operate': eval(case.c_operate),
                    'c_is_local': case.c_is_local,
                    'c_remake': case.c_remake,
                    'c_file_name': case.c_name,
                    'isRunning': False,
                    'c_mid': case.c_account,
                })
            return JsonResponse(case_set, safe=False)


    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")


def QueryByName(request):
    try:
        c_names = []
        c_play = request.GET['c_play']
        for i in json.loads(request.GET['data']).values():
            c_names.append(i)
        case_set = []
        case_list = CasesProfile.objects.filter(c_user__in=c_names, c_play=c_play).order_by('-id')
        case_set = []
        option = None
        if len(case_list) == 0:
            for case in case_list:
                case_set.append({
                    'c_id': case.id,
                    'c_date': case.c_date,
                    'c_name': case.c_user,
                    'c_project': case.c_project,
                    'c_purpose': case.c_purpose,
                    'c_play': case.c_play,
                    'c_cards': case.c_cards,
                    'c_step': case.c_option,
                    'c_operate': case.c_operate,
                    'c_is_local': case.c_is_local,
                    'c_remake': case.c_remake,
                    'c_file_name': case.c_name,
                    'isRunning': False,
                    'c_mid': case.c_account,
                })
            return JsonResponse(case_set, safe=False)

        else:
            for case in case_list:
                option = case.c_option
                print(case)
                case_set.append({
                    'c_id': case.id,
                    'c_date': case.c_date,
                    'c_name': case.c_user,
                    'c_project': case.c_project,
                    'c_purpose': case.c_purpose,
                    'c_play': case.c_play,
                    'c_cards': case.c_cards,
                    'c_option': eval(case.c_option),
                    'c_operate': eval(case.c_operate),
                    'c_is_local': case.c_is_local,
                    'c_remake': case.c_remake,
                    'c_file_name': case.c_name,
                    'isRunning': False,
                    'c_mid': case.c_account,
                })
            return JsonResponse(case_set, safe=False)
    
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")


def DeleteView(request):
    c_id = request.GET['c_id']
    try:
        case = CasesProfile.objects.filter(id=c_id)
        for c in case:
            print("delete case: %s" % c.c_name)
            os.remove(c.c_name)
        # 报告case
        reportCase = ReportProfile.objects.filter(c_case_id_id=c_id)
        for name in reportCase:
            report_path = name.r_save_dir + "/" + name.r_name
            os.remove(report_path)
        ReportProfile.objects.filter(c_case_id_id=c_id).delete()
        CasesProfile.objects.filter(id=c_id).delete()
    except FileNotFoundError:
        ReportProfile.objects.filter(c_case_id_id=c_id).delete()
        del_obj = CasesProfile.objects.filter(id=c_id).delete()
        if del_obj:
            case_set = GetAllCase()
            return JsonResponse(case_set, safe=False)
        else:
            return HttpResponse('删除失败.', content_type="application/json,charset=utf-8")
    else:
        return HttpResponse('删除成功.', content_type="application/json,charset=utf-8")

#   根据id修改bug内容
@require_http_methods(['POST'])
def UpdateCase(request):
    runfast = ["跑得快15张", "跑得快16张"]
    Data = json.loads(request.body)
    print("UpdateCase data : %s"%Data)
    _id = Data['c_id']
    _date = Data['c_date']  # 提交日期
    _name = Data['c_name']  # 提交人
    _project = Data['c_project']  # 项目组
    _play = Data['c_play']  # 项目玩法
    _purpose = Data['c_purpose']  # 测试目的c_cards
    option = Data['c_option']
    _options = option  # 创房选项
    _operate = Data['c_operate']  # 操作步骤
    _remake = Data['c_remake']  # 备注
    _file_name = Data['c_file_name'] # 文件路径
    _is_local = Data['c_is_local']
    _cards = Data['c_cards']    # 做牌数据
    _mids = Data["c_account"]

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  用户mid校验  <<<<<<<<<<<<<<<<<<<<<<<<
    try:
        _accounts = Data["c_account"]  # 用户mid
        mid = _accounts.replace(" ", "")
        users = eval(mid)

        if type(users) is not list:
            resp = {"code": 300, "Msg": "用户mid错误!请输入例:[127843,127864]"}
            return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")
        else:
            if len(users) != _options["o_player"]:
                resp = {"code": 300, "Msg": "用户mid数量和创房选项人数不一致"}
                return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")
            for i in users:
                if type(i) is not int:
                    resp = {"code": 300, "Msg": "mid请输入数字类型"}
                    return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")
    except Exception as err:
        resp = {"code": 300, "Msg": err}  # "用户mid错误!请输入例:[127843,123465]"
        return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  牌数据校验  <<<<<<<<<<<<<<<<<<<<<<<<
    try:
        card = _cards.replace(" ", "")
        if type(eval(card)) != dict:
            resp = {"code": 300, "Msg": "牌数据请输入JSON格式数据"}
            return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")


    except Exception as errro:
        resp = {"code": 300, "Msg": "牌数据请输入JSON格式数据"}
        return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")
    

    # 判断是否有加锤
    options_dict = None  # #创房选项
    operate_list  =  None #操作步骤
    if type(_options) is dict:
        options_dict = _options
    else:
        options_dict = eval(_options)

    if type(_operate) is list:
        operate_list = _operate
    else:
        operate_list = eval(_operate)


    for k,v in options_dict.items():
        if k == "o_jiachui":
            if v is True:
                if len(operate_list) is 0:
                    resp = {"code": 300, "Msg": "有加锤选项，请玩家选择是否加锤"}
                    return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")
                else:

                    try:
                        index = 0
                        for i in range(len(users)):
                            index += 1
                            for k, v in operate_list[i].items():
                                if k == "operation":
                                    if v != "加锤":
                                        resp = {"code": 300, "Msg": "第{}个玩法请选择是否加锤".format(i + 1)}
                                        return HttpResponse(json.dumps(resp),
                                                            content_type="application/json,charset=utf-8")

                    except IndexError:
                        resp = {"code": 300, "Msg": "玩家{}没有选择加锤".format(index)}
                        return HttpResponse(json.dumps(resp),
                                            content_type="application/json,charset=utf-8")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  操作步骤牌数据  <<<<<<<<<<<<<<<<<<<<<<<<
    index = 0
    if _play not in runfast:  # 非跑得快玩法
        for data in _operate:
            index += 1
            for k, v in data.items():
                if k == "operation":
                    if v == "出牌":
                        if len(data['card']) != 1:
                            resp = {"code": 300, "Msg": "操作步骤:第{}列， {}:{},牌数据只能为一张".format(index, data['users'], v)}
                            return HttpResponse(json.dumps(resp), content_type="application/json,charset=utf-8")
                elif k == "in_jiachui":
                    data['card'] = v

    #   创建测试用例脚本文件
    file_name = update_test_case_file(_path=_file_name,team=_project, play=_play, options=_options, operates=_operate, cards=_cards,mids=_mids)

    #
    result = CasesProfile.objects.filter(id=_id).update(
        c_date=_date,
        c_user=_name,
        c_project=_project,
        c_purpose=_purpose,
        c_play=_play,
        c_cards=_cards,
        c_option=_options,
        c_operate=_operate,
        c_remake=_remake,
        c_account=_mids,
    )
    if result:
        case_set = GetAllCase()
        return JsonResponse(case_set, safe=False)
        # return HttpResponse('创建成功', content_type="application/json,charset=utf-8")
    else:
        return HttpResponse('修改失败.', content_type="application/json,charset=utf-8")


def RunView(request):
    c_id = request.GET['c_id']
    case = CasesProfile.objects.filter(id=c_id)
    file_name = None
    report_name = None
    for c in case:
        file_name = c.c_name
        now = datetime.datetime.now()
        otherStyleTime = now.strftime("%Y--%m--%d %H:%M:%S")

        report_name = c.c_play + str(int(time.time()))+'.html'
        print("时间戳转换: %s" % otherStyleTime)

    print("report_name   %s" %report_name)
    print("时间戳: %s"%time.time())
    local_dir_path = file_name.split(file_name.split("/")[-1])[0]
    if os.path.exists(file_name) is False:
        return HttpResponse('执行文件不存在', content_type="application/json,charset=utf-8")
    print("Local: %s, 本地文件路径: %s" % (os.path.exists(file_name), file_name))
    #   如果本地文件存在
    if file_name != None and os.path.exists(file_name):
        init_path = '/home/phonetest/gale/TesterRunner/runner/run_case.py'
        # command = "nohup python %s %s >/dev/null 2>&1" % (init_path, file_name)
        command = "python %s %s %s" % (init_path, file_name, report_name)
        print("command: %s" % command)
        run_task = subprocess.Popen(command, shell=True)
        stdout = None

        report_path = "/home/phonetest/gale/TesterRunner/static/reports"

        is_over = None
        sing = True
        while sing:
            for i in os.listdir(report_path):
                if i == report_name: #如果文件存在
                    is_over = 0
                    sing = False

        if is_over == 0:
            # 证明子进程已经跑完
            report, created = ReportProfile.objects.filter(r_name=report_name).get_or_create(
                c_case_id_id = c_id, r_save_dir=report_path, r_name=report_name)

            if created:
                return HttpResponse('执行成功,稍等请查看运行报告', content_type="application/json,charset=utf-8")
            else:
                return HttpResponse('执行失败.', content_type="application/json,charset=utf-8")

        else:
            return HttpResponse('执行失败.', content_type="application/json,charset=utf-8")


def QueryReport(request):
    r_id = request.GET['r_id']
    report_list = ReportProfile.objects.all().filter(c_case_id=r_id).order_by('-id')
    report_set = []
    for report in report_list:
        report_set.append({
            'r_id': report.id,
            'r_end_time': report.r_end_time,
            'r_save_dir': report.r_save_dir,
            'r_name': report.r_name,
            'r_case_id': report.c_case_id_id
        })
    print("report_list: %s" % report_set)
    print("report_list_len: %s" % len(report_set))
    return JsonResponse(report_set[:20], safe=False)  #返回20条数据

