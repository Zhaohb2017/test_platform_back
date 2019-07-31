from django.db import models
import django.utils.timezone as timezone
# Create your models here.


class BugProfile(models.Model):
    # b_id = models.AutoField(primary_key=True)
    b_date = models.DateTimeField(default=timezone.now, verbose_name="提交日期")
    b_user = models.CharField(max_length=30, null=True, verbose_name="提交人")
    b_type = models.CharField(max_length=100, null=True, verbose_name="Bug类型")
    b_result = models.CharField(max_length=2000, null=True, verbose_name="直接结果")
    b_reason = models.CharField(max_length=2000, verbose_name="原因")
    b_solve = models.IntegerField(verbose_name="是否解决", choices=(("0", u"否"), ("1", u"是")), default="0",)

    b_img = models.ImageField(null=True, upload_to='static/images')
    objects = models.Manager()

    class Meta:
        db_table = 't_bug'
        verbose_name = 'BugProfile'

    def __str__(self):
        return self.b_type

    def __unicode__(self):
        return self.b_type


