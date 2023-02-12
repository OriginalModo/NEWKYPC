from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


# Create your models here.

class Article(models.Model):
    title = models.CharField('Название',max_length=50)
    anons = models.CharField('Аннос',max_length=250)
    full_text = RichTextField('Текст', max_length=2000)
    date = models.DateTimeField('Дата публикации')
    slug = models.SlugField('URL',max_length=250, unique=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def get_absolute_url(self):

        return reverse('slug:slug_update', kwargs={'slug': self.slug})