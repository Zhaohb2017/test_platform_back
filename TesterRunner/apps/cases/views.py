import json
import os
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
    print("data: %s" % Data)
    _date = Data['c_date']          # 提交日期
    _name = Data['c_name']          # 提交人
    _project = Data['c_project']    # 项目组
    _mid = Data["c_account"]        #用户mid
    _play = Data['c_play']          # 项目玩法
    _purpose = Data['c_purpose']    # 测试目的
    _options = Data['c_options']    # 创房选项
    _steps = Data['c_steps']        # 操作步骤
    _remake = Data['c_remake']      # 备注
    _cards = Data['c_cards']        # 做牌数据
    _log="addcaseview----->"
    print("mid___________",type(_mid))
    print("提交时间,",_date)
    print(_log + "玩法选项" + "%s"%_options)
    #   创建测试用例脚本文件
    file_name = make_test_case_files(_project, _play, _options, _steps, _cards,_mid)
    if file_name:
        is_local = 1
    else:
        is_local = 0
    print(1111111111111111111111111)
    case = CasesProfile(
        c_date=_date,
        c_user=_name,
        c_project=_project,
        c_purpose=_purpose,
        c_play=_play,
        c_cards = _cards,
        c_option=_options,
        c_operate=_steps,
        c_is_local=is_local,
        c_remake=_remake,
        c_name=file_name,
        c_account = _mid ,
    )
    case.save()
    print("1111111111",case.c_operate)
    print("22222222222",_steps)
    if case.c_operate == _steps:
        return HttpResponse('添加成功', content_type="application/json,charset=utf-8")
    else:
        return HttpResponse('添加失败', content_type="application/json,charset=utf-8")


def GetAllCase():
    case_set = []
    case_list = CasesProfile.objects.all()
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
        print("project",project)
        print("version",version)
        print("play",play)
        project = project + '-' + version  # 数据库中c_project字段值是 project_version拼接起来的
        case_list = CasesProfile.objects.filter(c_project=project, c_play=play)
        case_set = []
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
                'c_mid':case.c_account,
            })
        return JsonResponse(case_set, safe=False)
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")


def QueryByName(request):
    try:
        name = request.GET['c_name']
        case_set = []
        case_list = CasesProfile.objects.filter(c_user=name)
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
        return JsonResponse(case_set, safe=False)
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")


def DeleteView(request):
    c_id = request.GET['c_id']

    case = CasesProfile.objects.filter(id=c_id)
    for c in case:
        os.remove(c.c_name)

    del_obj = CasesProfile.objects.filter(id=c_id).delete()
    if del_obj:
        case_set = GetAllCase()
        return JsonResponse(case_set, safe=False)
    else:
        return HttpResponse('删除失败.', content_type="application/json,charset=utf-8")


#   根据id修改bug内容
@require_http_methods(['POST'])
def UpdateCase(request):
    Data = json.loads(request.body)
    print("Data: %s" % Data)
    _id = Data['c_id']
    _date = Data['c_date']  # 提交日期
    _name = Data['c_name']  # 提交人
    _project = Data['c_project']  # 项目组
    _play = Data['c_play']  # 项目玩法
    _purpose = Data['c_purpose']  # 测试目的c_cards
    option = transform_create_room_options(_play, Data['c_option'])
    _options = option  # 创房选项
    _operate = Data['c_operate']  # 操作步骤
    _remake = Data['c_remake']  # 备注
    _file_name = Data['c_file_name'] # 文件路径
    _is_local = Data['c_is_local']
    _cards = Data['c_cards']    # 做牌数据
    print("_file_name: %s" % _file_name)
    print("project: %s, play: %s" % (_project, _play))
    #   创建测试用例脚本文件
    file_name = make_test_case_files(_project, _play, _options, _operate, _cards, _file_name)

    result = CasesProfile.objects.filter(id=_id).update(
        c_date=_date,
        c_user=_name,
        c_project=_project,
        c_purpose=_purpose,
        c_play=_play,
        c_cards=_cards,
        c_option=_options,
        c_operate=_operate,
        c_is_local=_is_local,
        c_remake=_remake,
        c_name=file_name,
    )

    if result:
        case_set = GetAllCase()
        return JsonResponse(case_set, safe=False)
    else:
        return HttpResponse('修改失败.', content_type="application/json,charset=utf-8")


def RunView(request):
    c_id = request.GET['c_id']
    case = CasesProfile.objects.filter(id=c_id)
    file_name = None
    report_name = None
    for c in case:
        file_name = c.c_name
        print('file_name: %s' % c.c_name)
        report_name = c.c_play + time.strftime("_%Y_%m_%d_%H_%M_%S", time.localtime(time.time())) + '.html'

    local_dir_path = file_name.split(file_name.split("/")[-1])[0]
    print("Local: %s, 本地文件路径: %s" % (os.path.exists(file_name), file_name))

    #   如果本地文件存在
    if file_name != None and os.path.exists(file_name):
        init_path = '/home/phonetest/gale/TesterRunner/runner/run_case.py'
        # command = "nohup python %s %s >/dev/null 2>&1" % (init_path, file_name)
        command = "python %s %s %s" % (init_path, file_name, report_name)
        print("command: %s" % command)
        run_task = subprocess.Popen(command, shell=True)
        stdout = None
        # stdout, stderr = run_task.communicate()
        # print("stdout",run_task.returncode)
        # is_over = run_task.poll()
        # print("is_over1111111111111111111111111111111111111111111: %s" % is_over)

        #   return_code = {0: "成功"}
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
    report_list = ReportProfile.objects.filter(c_case_id_id=r_id)

    report_set = []
    for report in report_list:
        report_set.append({
            'r_id': report.id,
            'r_end_time': report.r_end_time,
            'r_save_dir': report.r_save_dir,
            'r_name': report.r_name,
            'r_case_id': report.c_case_id_id
        })
    print("report_list: %s" % report_list)
    return JsonResponse(report_set, safe=False)

