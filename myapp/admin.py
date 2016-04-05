from django.contrib import admin

# Register your models here.

from .models import Board


class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'recorded_date')

admin.site.register(Board, BoardAdmin)
