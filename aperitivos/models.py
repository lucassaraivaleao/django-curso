from django.db import models
from django.urls import reverse


class Video(models.Model):
    titulo = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    youtube_link = models.CharField(max_length=50)
    creation = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))

    def __str__(self):
        return f'Video: {self.titulo}'
