import json
import os
from .models import *
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from .HTMLTestReport import *
from .summarReport import *



# Create your views here.
@require_http_methods(['POST'])
def Add_TestReport(request):
    Data = json.loads(request.body)
    parameter = Data["data"]
    print("测试报告: %s"%parameter)
    print("当前路径：%s"%os.getcwd())

    legacy_list = []
    for data in parameter['leftoverProblemList']:
        legacy = {}
        index = 1
        for k,v in data.items():
            legacy['id'] = index
            if k == "problem_description":
                legacy['ques_desc'] = v
            if k == "cause":
                legacy['reason'] = v
            if k == "Severity":
                legacy['severity'] = v
            if k == "Responsible":
                legacy['duty_officer'] = v
            if k == "address":
                legacy['address'] = v
        index += 1
        legacy_list.append(legacy)

    risk_list = []
    for data in parameter['riskList']:
        risk = {}
        index = 1
        for k, v in data.items():
            risk['id'] = index
            if k == "description":
                risk['risk_desc'] = v
            if k == "level":
                risk['deal_method'] = v
            if k == "countermeasures":
                risk['severity'] = v
            if k == "Responsible":
                risk['duty_officer'] = v
            if k == "remark":
                risk['note'] = v
        index += 1
        risk_list.append(risk)


    html_data = {
        "version_name": parameter['version_name'],
        "testing_phase": parameter['testing_phase'],
        "testing_time": parameter['t_date'],
        "release_note": parameter['release_note'],
        "testing_note": parameter['testing_note'],
        "testing_standard": parameter['testing_standard'],
        "tester": parameter['tester'],
        "test_result": parameter['test_result'],
        "testing_items": parameter['testing_items'],
        "delay_note": parameter['delay_note'],
        "bug_num": list(parameter['bug'][0].values()),
        "legacy":legacy_list ,
        "risk":risk_list,
    }
    write = WriteHtml(receive_data=html_data)
    print(write.write_HTML())

    try:
            info = AddTestReport(
                c_versions=parameter['version_name'],
                c_phase=parameter['testing_phase'],
                c_date=parameter['testing_time'],
                release_note=parameter['release_note'],
                testing_note = parameter['testing_note'],
                standard = parameter['testing_standard'],
                tester = parameter['tester'],
                test_result = parameter['test_result'],
                testing_items = parameter['testing_items'],
                delay_note = parameter['delay_note'],
                bugsum = parameter['bug'],
                legacy = parameter['leftoverProblemList'],
                risk = parameter['riskList'],
                report_path = write.write_HTML(),

            )
            info.save()
            return HttpResponse('添加成功', content_type="application/json,charset=utf-8")

    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")


def GetTestReport():
    _set = []
    _list = AddTestReport.objects.all().order_by('-id')
    for bug in _list:
        _set.append({
            "c_id":bug.id,
            'c_versions': bug.c_versions,
            'c_phase': bug.c_phase,
            'c_date': bug.c_date,
        })
    return _set


#   查询全部bug
def Query(request):
    try:
        _set = GetTestReport()
        return JsonResponse(_set, safe=False)
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")



def Delete(request):
    s_id = request.GET['t_id']
    report = AddTestReport.objects.filter(id=s_id)
    for c in report:
        local_path = os.getcwd()
        report_file_path = local_path + '/TesterRunner/static/reports/'
        os.remove(report_file_path + c.report_path)
    del_obj = AddTestReport.objects.filter(id=s_id).delete()
    if del_obj:
        _set = GetTestReport()
        return JsonResponse(_set, safe=False)
    else:
        return HttpResponse('删除失败.', content_type="application/json,charset=utf-8")




def Search(request):
    _set = []
    request_data = request.GET['data']
    search_data = eval(request_data)
    '''删除空值'''
    for key in list(search_data.keys()):
        if not search_data.get(key):
            search_data.pop(key)

    if len(search_data) is not 0:
        s_obj = AddTestReport.objects.filter(**search_data)
        for bug in s_obj:
            _set.append({
                "c_id": bug.id,
                'c_versions': bug.c_versions,
                'c_phase': bug.c_phase,
                'c_date': bug.c_date,
            })
        return JsonResponse(_set, safe=False)
    else:
        rep = GetTestReport()
        return JsonResponse(rep, safe=False)



def QueryReport(request):
    r_id = request.GET['r_id']
    report_list = AddTestReport.objects.all().filter(id=r_id).order_by('-id')
    report_set = []
    for report in report_list:
        report_set.append({
            'r_id': report.id,
             'r_end_time':report.c_date,
            'r_name': report.report_path
        })
    return JsonResponse(report_set[:20], safe=False)  #返回20条数据




#   周报
#----------------------------------------------------------------------------------------------------
# Create your views here.
@require_http_methods(['POST'])
def Add_weekly(request):
    Data = json.loads(request.body)
    parameter = Data["data"]
    print("测试报告: %s" % Data, type(Data))
    _summary = parameter['summary']
    _job_content = parameter['job_content']
    _local_bug = parameter['localbugList']
    _lineBug = parameter['linebugList']
    _week_num = parameter['week_num']
    _account = parameter['account']
    print("_summary",_summary)
    print("_job_content", _job_content)
    print("_local_bug", _local_bug)
    print("_lineBug", _lineBug)
    date = parameter['t_date']
    _time = str(date[:4]) + "-" +str(date[5:7]) + "-" +str(date[8:10])
    html = WriteSummarHtml(parameter)  #                user = _user,
    file_path = html.write_HTML()

    info = Weekly(
                date = _time,
                user = _account,
                job_content = _job_content,
                local_bug=_local_bug,
                line_bug = _lineBug,
                summary = _summary,
                week = _week_num,
                report_path = file_path,
            )
    info.save()
    return HttpResponse('添加成功', content_type="application/json,charset=utf-8")





def GetWeeklReport():
    _set = []
    _list = Weekly.objects.all().order_by('id')
    for Week in _list:
        _set.append({
            "c_id":Week.id,
            'c_date': Week.date,
            'c_user': Week.user,
            'c_report_path': Week.report_path,
            'c_job_content': Week.job_content,
            'c_line_bug': Week.line_bug,
            'c_local_bug': Week.local_bug,
            'c_summary': Week.summary,
            'c_week':Week.week
        })
    return _set


#   查询全部
def QueryWeekly(request):
    try:
        _set = GetWeeklReport()
        return JsonResponse(_set, safe=False)
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")




def WeeklyDelete(request):
    s_id = request.GET['t_id']
    report = Weekly.objects.filter(id=s_id)
    for c in report:
        local_path = os.getcwd()
        report_file_path = local_path + '/TesterRunner/static/reports/'
        os.remove(report_file_path + c.report_path)
    del_obj = Weekly.objects.filter(id=s_id).delete()
    if del_obj:
        _set = GetWeeklReport()
        return JsonResponse(_set, safe=False)
    else:
        return HttpResponse('删除失败.', content_type="application/json,charset=utf-8")

def QueryWeekReport(request):
    r_id = request.GET['r_id']
    report_list = Weekly.objects.all().filter(id=r_id).order_by('-id')
    report_set = []
    for report in report_list:
        report_set.append({
            'r_id': report.id,
             'r_end_time':report.create_date,
            'r_name': report.report_path
        })
    return JsonResponse(report_set[:20], safe=False)  #返回20条数据




def WeekSearch(request):
    _set = []
    request_data = request.GET['data']
    search_data = eval(request_data)
    '''删除空值'''
    for key in list(search_data.keys()):
        if not search_data.get(key):
            search_data.pop(key)
    print(list(search_data.keys()))
    if 'date' in list(search_data.keys()):
        search_data['date'] = str(search_data['date'][:4]) + "-" + str(search_data['date'][5:7]) + "-" + str(search_data['date'][8:10])


    print("fffffffff",search_data)

    if len(search_data) is not 0:
        _list = Weekly.objects.filter(**search_data)
        for Week in _list:
            _set.append({
                "c_id": Week.id,
                'c_date': Week.date,
                'c_user': Week.user,
                'c_report_path': Week.report_path,
                'c_job_content': Week.job_content,
                'c_line_bug': Week.line_bug,
                'c_local_bug': Week.local_bug,
                'c_summary': Week.summary,
                'c_week': Week.week
            })
        return JsonResponse(_set, safe=False)
    else:
        rep = GetWeeklReport()
        return JsonResponse(rep, safe=False)