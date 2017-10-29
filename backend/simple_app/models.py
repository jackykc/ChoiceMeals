
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

# class Message(models.Model):
#     user = models.ForeignKey('auth.User')
#     message = models.TextField()
#     creation_date = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Ingredient(models.Model):
	name = models.CharField(max_length=100)
	notes = models.TextField()
	category = models.ForeignKey(Category, related_name='ingredients')

	def __str__(self):
		return self.name
	