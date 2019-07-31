from django.db import models
import django.utils.timezone as timezone
# Create your models here.



#IP表
class DeployIP(models.Model):
    t_ip = models.CharField(max_length=1000, verbose_name="IP")
    t_port= models.CharField(max_length=1000, verbose_name="port")
    t_remark = models.CharField(max_length=1000, verbose_name="备注", null=True)
    class Mete:
        db_table = "t_deployip"
        verbose_name = 'DeployIPProfile'

    def __str__(self):
        return self.t_remark

    def __unicode__(self):
        return self.t_remark

