from django.db import models
import django.utils.timezone as timezone
# Create your models here.


#测试点表
class TestPoint(models.Model):
    #从表
    t_version= models.CharField(max_length=100, null=True, verbose_name="版本")
    t_module = models.CharField(max_length=100, verbose_name="模块", default="0", )
    t_content = models.CharField(max_length=1000,verbose_name="内容")
    t_user = models.CharField(max_length=10,verbose_name="创建姓名")
    t_date = models.DateTimeField("创建时间",default=timezone.now)
    t_storage = models.IntegerField(verbose_name="是否入库", default="0", null=True)
    t_usable = models.IntegerField(verbose_name="是否失效", default="0", null=True)
    t_img = models.ImageField(upload_to='../../static/img/',null=True)
    t_remark = models.CharField(max_length=1000, verbose_name="影响范围",null=True)
    class Mete:
        db_table = "t_point"
        verbose_name = 'TestPointProfile'

    def __str__(self):
        return self.t_content

    def __unicode__(self):
        return self.t_content


#知识库
class Knowledge(models.Model):
    t_date = models.DateTimeField("创建时间", default=timezone.now)
    t_link = models.CharField(max_length=1000, verbose_name="链接")
    t_title= models.CharField(max_length=1000, verbose_name="说明",null=True)
    class Mete:
        db_table = "t_knowledge"
        verbose_name = 'knowledgeProfile'

    def __str__(self):
        return self.t_link

    def __unicode__(self):
        return self.t_link

