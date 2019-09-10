from django.db import models
import django.utils.timezone as timezone




class AddVersions(models.Model):
    c_versions = models.CharField(max_length=1000, verbose_name="版本游戏名称")
    c_link = models.CharField(max_length=1000, verbose_name="版本游戏链接")
    c_remark = models.CharField(max_length=1000, verbose_name="版本后台说明")
    class Mete:
        db_table = "versions"
        verbose_name = 'AddVersionsProfile'

    def __str__(self):
        return self.c_versions

    def __unicode__(self):
        return self.c_versions

