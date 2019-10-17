
import json
import os
from .models import *
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
# Create your views here.

def Search(request):
    try:
        _set = []
        _list = LogInfo.objects.all().order_by('-id')
        for log in _list:
            _set.append({
                "c_id": log.id,
                'c_user': log.user,
                'c_date': log.date,
                'c_info':log.info
            })
        return JsonResponse(_set, safe=False)
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")