# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models

# 创建文章类
class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')    # 文章标题属性
    content = models.TextField(null=True)                       # 文章内容属性

    def __unicode__(self):
        return self.title

