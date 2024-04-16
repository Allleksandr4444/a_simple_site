from django.db import models

class Table(models.Model):
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
