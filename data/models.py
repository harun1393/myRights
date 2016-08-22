from __future__ import unicode_literals

from django.db import models

class Info(models.Model):
    title = models.CharField(max_length=50,)
    description = models.TextField()
    category = models.ForeignKey('Category',db_column='category')

    class Meta:
        db_table = 'info'

'''
class SubCategory(models.Model):
    title = models.CharField(max_length=50,)
    category = models.ForeignKey('Category',db_column='category')

    class Meta:
        db_table = 'sub_cat`'
        '''

class Category(models.Model):
    title = models.CharField(max_length=50,)

    class Meta:
        db_table = 'category'
