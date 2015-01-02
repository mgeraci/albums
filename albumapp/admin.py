from django.contrib import admin

from albumapp.models import Album, AlbumList, AlbumSelection


class AlbumAdmin(admin.ModelAdmin):
  pass


class AlbumListAdmin(admin.ModelAdmin):
  pass


class AlbumSelectionAdmin(admin.ModelAdmin):
  pass


admin.site.register(Album, AlbumAdmin)
admin.site.register(AlbumList, AlbumListAdmin)
admin.site.register(AlbumSelection, AlbumSelectionAdmin)
