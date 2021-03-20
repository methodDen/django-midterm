from django.db import models

# Create your models here.
class BookJournalBase(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    price = models.FloatField(default=0.0, verbose_name='Стоимость')
    description = models.TextField(max_length=500, blank=True, verbose_name='Описание')
    dateOfCreation = models.DateField(null=True, blank=True, verbose_name='Дата Создания')

    class Meta:
        verbose_name = 'База книги и журналов'
        verbose_name_plural = 'Базы книг и журналов'
        abstract = True

class Book(BookJournalBase):
    numpages = models.IntegerField(default=0, verbose_name='Количество страниц')
    genre = models.CharField(max_length=30, verbose_name='Жанр')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

class Journal(BookJournalBase):
    type = models.CharField(max_length=20, verbose_name='Тип')
    publisher = models.CharField(max_length=50, verbose_name='Издатель')

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'
