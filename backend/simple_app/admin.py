

from __future__ import unicode_literals
from django.contrib import admin
from . import models

admin.site.register(models.Category)
admin.site.register(models.Ingredient)