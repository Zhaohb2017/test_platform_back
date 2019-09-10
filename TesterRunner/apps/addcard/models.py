from django.db import models
import django.utils.timezone as timezone




class AddGameCard(models.Model):
    c_versions = models.CharField(max_length=1000, verbose_name="版本")
    c_method = models.CharField(max_length=1000, verbose_name="游戏玩法")
    c_card = models.CharField(max_length=1000, verbose_name="牌数据")
    c_remark = models.CharField(max_length=1000, verbose_name="备注")
    class Mete:
        db_table = "gamecard"
        verbose_name = 'AddcardProfile'

    def __str__(self):
        return self.c_card

    def __unicode__(self):
        return self.c_card

