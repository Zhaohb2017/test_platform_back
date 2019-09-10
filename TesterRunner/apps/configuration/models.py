from django.db import models

# Create your models here.

from django.db import models
import django.utils.timezone as timezone
# Create your models here.

#服务器表
class Server(models.Model):
    t_ip = models.CharField(max_length=1000, verbose_name="IP")
    t_port= models.CharField(max_length=1000, verbose_name="port")
    t_remark = models.CharField(max_length=1000, verbose_name="备注", null=True)
    class Mete:
        db_table = "t_server"
        verbose_name = 'ServerProfile'

    def __str__(self):
        return self.t_remark

    def __unicode__(self):
        return self.t_remark

