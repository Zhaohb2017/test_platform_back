import json
import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse, JsonResponse
from rest_framework import serializers
from .models import *
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
class UsersSerializer(serializers.Serializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


def index(request):
    return render(request, 'index.html')


#   用户登录
@require_http_methods(["POST"])
def LoginView(request):
    LoginData = json.loads(request.body)
    username = LoginData['username']
    password = LoginData['pwd']

    user = authenticate(request, username=username, password=password)

    if request.user.is_authenticated:
        print("user: %s" % user)
        response_data = {'data': user.username, 'msg': "用户已登录，请勿重复登录"}
        return JsonResponse(response_data, safe=False)

    if user is not None and user.is_active:
        print("aaaaaaaaaa")
        login(request, user)
        # 不分离跳转到成功页面.
        # return HttpResponseRedirect("/")
        # 前后端分离, 返回数据告诉前端已经登录成功
        response_data = {'data': user.username, 'msg': "登录成功"}
        return JsonResponse(response_data, safe=False)
    else:
        print("bbbbbbbbb")
        # 返回一个无效帐户的错误
        response_data = {'adata': "", 'msg': "登录失败"}
        return JsonResponse(response_data, safe=False)


@require_http_methods(['POST'])
def LogoutView(request):
    try:
        print("a: %s" % request.user)
        logout(request)
        return HttpResponse('登出成功', content_type="application/json,charset=utf-8")
    except Exception as e:
        return HttpResponse('登出失败', content_type="application/json,charset=utf-8")


#   注册或添加用户
@require_http_methods(["POST"])
def UserAddView(request):
    current_time = timezone.now()
    #   注册：审核
    try:
        AddUserData = json.loads(request.body)
        u_name = AddUserData["username"]

        info = UserProfile.objects.filter(username=u_name)
        if len(info) > 0:
            response_data = {'data': u_name, 'msg': "注册失败, 该用户已存在."}
            return JsonResponse(response_data, safe=False)

        u_pwd = AddUserData['pwd']
        u_email = u_name

        if 'staff' not in AddUserData:
            u_is_staff = 0
        else:
            u_is_staff = AddUserData['staff']

        if 'active' not in AddUserData:
            u_is_active = 1
        else:
            u_is_active = AddUserData['active']

        if 'join_time' not in AddUserData:
            u_joined = current_time
        else:
            u_joined = AddUserData['join_time']

        u_first_name = u_name
        u_last_name = u_first_name

        if 'super' not in AddUserData:
            u_super_user = 0
        else:
            u_super_user = AddUserData['super']

        print("name: %s, pwd: %s" % (u_name, u_pwd))

        print('pwd: %s' % make_password(u_pwd, None, 'pbkdf2_sha256'))

        user, created = UserProfile.objects.filter(username=u_name).get_or_create(
            username=u_name, password=make_password(u_pwd, None, 'pbkdf2_sha256'), is_active=u_is_active, is_staff=u_is_staff,
            date_joined=u_joined, is_superuser=u_super_user, email=u_email,
            first_name=u_first_name, last_name=u_last_name)

        print("UserAddView: user: %s, created: %s" % (user, created))

        if created:
            login(request, user)
            response_data = {'data': user.username, 'msg': "注册成功"}
            return JsonResponse(response_data, safe=False)
        else:
            response_data = {'data': user.username, 'msg': "注册失败"}
            return JsonResponse(response_data, safe=False)

    except Exception as e:
        result = {'reason': e}
        return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")

# @require_http_methods(['GET'])
def UserQueryAllView(request):
    try:
        UsersList = UserProfile.objects.all()

        for user in UsersList:
            print(user.username, user.password, user.is_active)

        return HttpResponse(UsersList, content_type="application/json,charset=utf-8")
    except Exception as e:
        return HttpResponse(e, content_type="application/json,charset=utf-8")

#   根据用户名来查询
@require_http_methods(['POST'])
def UserQueryView(request):
    try:
        user = UserProfile.objects.filter(name__iexact=request.POST['username'])
        return HttpResponse(user, content_type="application/json,charset=utf-8")
    except Exception as e:
        return HttpResponse('User does not exist', content_type="application/json,charset=utf-8")


#   用户删除
@require_http_methods(['POST'])
def UserDeleteView(request):
    try:
        if not request.user.is_authenticated:
            return HttpResponse(u'%s 用户未登录, 请登录!' % request.user, content_type="application/json,charset=utf-8")

        if request.user.is_superuser != True:
            return HttpResponse(u'%s 用户没有此权限, 请登录!' % request.user, content_type="application/json,charset=utf-8")

        username = request.POST['username']
        del_result = UserProfile.objects.filter(username=username).delete()
        if del_result:
            return HttpResponse('Delete %s OK!' % username, content_type="application/json,charset=utf-8")
        else:
            return HttpResponse('Delete %s Error!' % username, content_type="application/json,charset=utf-8")
    except Exception as e:
        return HttpResponse('User does not exist', content_type="application/json,charset=utf-8")


#   用户修改
@require_http_methods(['POST'])
def UserUpdateView(request):
    try:
        if not request.user.is_authenticated:
            return HttpResponse(u'%s 用户未登录, 请登录!' % request.user, content_type="application/json,charset=utf-8")

        u_id = request.POST['u_id']
        if u_id is None:
            return HttpResponse('No user id.', content_type="application/json,charset=utf-8")

        u_pwd = request.POST['pwd']
        u_nickname = request.POST['nickname']
        if u_pwd != None or u_pwd != "":
            UserProfile.objects.filter(id=u_id).update(password=make_password(u_pwd, None, 'pbkdf2_sha256'), last_name=u_nickname)

        if u_nickname != None or u_nickname != "":
            UserProfile.objects.filter(id=u_id).update(last_name=u_nickname)

        check_user = UserProfile.objects.filter(id=u_id)
        if check_user.password == u_pwd or check_user.last_name == u_nickname:
            return HttpResponse('Update user info is OK!', content_type="application/json,charset=utf-8")
        else:
            return HttpResponse('Update user info is Error!', content_type="application/json,charset=utf-8")

    except Exception as e:
        return HttpResponse('Had Error by %s' % e, content_type="application/json,charset=utf-8")