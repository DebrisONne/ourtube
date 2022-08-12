from django.contrib import admin
from .models import Video, Category, Tag

class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'category',
    )
    search_fields = ('title','category__name')
    list_filter = ('category',)

admin.site.register(Video, VideoAdmin)
admin.site.register(Category)
admin.site.register(Tag)

