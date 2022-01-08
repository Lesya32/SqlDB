from django.db import models
from django.db.models.base import Model

class Articles(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    text = models.TextField('Текст')
    date = models.DateTimeField('Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'