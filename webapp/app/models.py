from django.db import models 


class App(models.Model): 
    app = models.CharField('App', max_length=100, blank=False)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時',auto_now=True)

    def __str__(self):
        return self.app
















"""
from django.db import models

class App(models.Model):
    product_name = models.CharField('商品名',max_length=255, blank=False)
    price = models.CharField('値段',max_length=255, blank=False)
    url = models.URLField('URL',max_length=255, blank=False)
"""