from django.db import models
import django.utils.timezone as timezone


# Create your models here.

#   用例表
class CasesProfile(models.Model):
    c_date = models.DateTimeField(default=timezone.now, verbose_name="提交日期")
    c_user = models.CharField(max_length=30, verbose_name="提交人", default="")
    c_project = models.CharField(max_length=100,  verbose_name="用例所属项目", default="")
    c_purpose = models.CharField(max_length=200, verbose_name="测试目的", default="")
    c_play = models.CharField(max_length=100, null=True, verbose_name="对应玩法", default="")
    c_option = models.CharField(max_length=1000, verbose_name="创房选项", default="")
    c_operate = models.TextField(verbose_name="操作步骤", default="")
    c_is_local = models.IntegerField(null=True, verbose_name="是否在本地已生成文件")
    c_remake = models.CharField(max_length=200, null=True, verbose_name="备注")
    c_name = models.CharField(max_length=1000,  verbose_name="用例生成文件名字", default="")
    # c_account = models.IntegerField(null=True,verbose_name="用户mid")
    c_account = models.CharField(max_length=100,null=True,verbose_name='用户mid',default="")
    c_cards = models.CharField(max_length=500, null=True, verbose_name="牌型数据", default="")

    c_status = models.IntegerField(null=True, verbose_name="用例运行状态", default=0)
    objects = models.Manager()

    class Meta:
        db_table = 't_cases'
        verbose_name = 'CasesProfile'

    def __str__(self):
        return self.c_project

    def __unicode__(self):
        return self.c_project


#   报告表
class ReportProfile(models.Model):
    #  报告表-- 测试用例id与  用例表-- 本身生成的id 外键关系
    c_case_id = models.ForeignKey(CasesProfile, on_delete=True)
    r_end_time = models.DateTimeField(default=timezone.now, verbose_name="用例运行结束时间")
    r_save_dir = models.CharField(max_length=250, verbose_name="用例存放路径")
    r_name = models.CharField(max_length=200, null=True, verbose_name="报告名字")
    objects = models.Manager()
    class Meta:
        ordering = ('-r_end_time',)  #时间倒序存在
        db_table = 't_report'
        verbose_name = 'ReportProfile'

    def __str__(self):
        return self.r_save_dir

    def __unicode__(self):
        return self.r_save_dir
