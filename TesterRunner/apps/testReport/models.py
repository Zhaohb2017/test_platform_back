from django.db import models
import django.utils.timezone as timezone



class AddTestReport(models.Model):
    c_versions = models.CharField(max_length=1000, verbose_name="版本游戏名称")
    c_phase = models.CharField(max_length=1000, verbose_name="测试阶段")
    c_date = models.DateTimeField(default=timezone.now, verbose_name="测试时间")
    release_note = models.CharField(max_length=1000, verbose_name="版本说明")
    testing_note = models.CharField(max_length=1000, verbose_name="测试说明")
    standard = models.CharField(max_length=1000, verbose_name="准出标准")
    tester = models.CharField(max_length=1000, verbose_name="测试人员")
    test_result = models.CharField(max_length=1000, verbose_name="测试结果")
    testing_items = models.CharField(max_length=1000, verbose_name="测试项")
    delay_note = models.CharField(max_length=1000, verbose_name="延期说明")
    bugsum = models.CharField(max_length=1000, verbose_name="bug汇总")
    legacy = models.CharField(max_length=1000, verbose_name="遗留问题")
    risk = models.CharField(max_length=1000, verbose_name="风险")
    report_path = models.CharField(max_length=1000, verbose_name="报告路径")

    class Mete:
        db_table = "testreport"
        verbose_name = 'AddVersionsProfile'

    def __str__(self):
        return self.c_versions

    def __unicode__(self):
        return self.c_versions


class Weekly(models.Model):
    date = models.DateField(default='')
    create_date = models.DateTimeField(auto_now_add=True) #创建时间
    week = models.CharField(max_length=100, verbose_name="月周数")
    user = models.CharField(max_length=1000, verbose_name="提交人")
    job_content = models.CharField(max_length=1000, verbose_name="工作内容")
    local_bug = models.CharField(max_length=1000, verbose_name="本地Bug")
    line_bug = models.CharField(max_length=1000, verbose_name="线上Bug")
    summary = models.CharField(max_length=1000, verbose_name="测试总结")
    report_path = models.CharField(max_length=1000, verbose_name="报告路径")