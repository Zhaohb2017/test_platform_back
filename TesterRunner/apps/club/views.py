import json
from .models import *
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from apps.utils.DataConversion import *

# Create your views here.
@require_http_methods(['POST'])
def AddPeople(request):
    Data = json.loads(request.body)
    clubid  = Data["c_ip"]
    mid = Data["c_port"]
    sesskey = Data["c_user"]
    _info = ClubInfo(
        t_clubid = clubid,
        t_mid = mid,
        t_sesskey = sesskey,

    )
    _info.save()
    return HttpResponse('添加成功', content_type="application/json,charset=utf-8")