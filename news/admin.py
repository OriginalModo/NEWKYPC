from django.contrib import admin
from django.contrib.auth.models import User

from .models import *


# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('date',)
    # paginator = 5
    # paginator = 5





