from django.contrib.admin import ModelAdmin, register

from aperitivos.models import Video


@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ('titulo', 'slug', 'creation', 'youtube_link')
    ordering = ('creation',)
    prepopulated_fields = {'slug':('titulo',)}
