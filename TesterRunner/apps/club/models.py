from django.db import models
import django.utils.timezone as timezone
# Create your models here.



#club信息表
class ClubInfo(models.Model):
    t_clubid = models.CharField(max_length=1000, verbose_name="俱乐部ID")
    t_mid= models.CharField(max_length=1000, verbose_name="加入俱乐部ID")
    t_sesskey = models.CharField(max_length=1000, verbose_name="sesskey ")
    class Mete:
        db_table = "t_clubinfo"
        verbose_name = 'ClubInfoProfile'

    def __str__(self):
        return self.t_sesskey

    def __unicode__(self):
        return self.t_sesskey

