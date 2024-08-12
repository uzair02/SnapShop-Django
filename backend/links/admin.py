from django.contrib import admin
from .models import SearchResult

class SearchResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'link']
    search_fields = ['description', 'link']

admin.site.register(SearchResult, SearchResultAdmin)
