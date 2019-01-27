from django.contrib import admin

from ..models import ParsedData


@admin.register(ParsedData)
class ParsedDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip_addr', 'log_date', )
