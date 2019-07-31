from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    '''
    继承Django的AbstractUser，并向里面添加两条数据内容
    new user model
    '''
    account = models.EmailField(max_length=100, null=True, blank=True, verbose_name="账号-邮箱")
    nickname = models.CharField(max_length=30, null=True, blank=True, verbose_name="昵称")
    gender = models.CharField(max_length=6, null=True, choices=(("male", u"男"), ("female", u"女")), default="female", verbose_name="性别")

    class Meta:
        verbose_name = 'UserProfile'

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username



