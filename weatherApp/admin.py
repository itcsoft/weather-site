from calendar import c
from dataclasses import field
from re import search
from django.contrib import admin
from weatherApp.models import SearchedCity


class SearchedCityAdmin(admin.ModelAdmin):
    list_display = ('city', 'temperature', 'sent_at', 'updated')
    search_fields = ['city']
    list_filter = ('sent_at', 'updated')
    list_editable = ['temperature']
    readonly_fields = ['city', 'sent_at', 'updated']


admin.site.register(SearchedCity, SearchedCityAdmin)