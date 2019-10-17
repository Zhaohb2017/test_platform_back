from django.db import models

# Create your models here.
class LogInfo(models.Model):
    date = models.DateTimeField(auto_now_add=True)  #时间
    user = models.CharField(max_length=1000, verbose_name="操作人")
    info = models.CharField(max_length=1000, verbose_name="操作信息")
    class Mete:
        db_table = "loginfo"
        verbose_name = 'LogInfoProfile'

    def __str__(self):
        return self.user

    def __unicode__(self):
        return self.info



