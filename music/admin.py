from django.contrib import admin
from .models import Album,Song

class ListAdmin(admin.ModelAdmin):
  list_display=['artist','album_title','genre']

admin.site.register(Album,ListAdmin)
admin.site.register(Song)
