from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe 

from . fields import OrderField

class Subject(models.Model):
    """ Модуль темы курса """
    title = models.CharField("Заголовок", max_length=255)
    slug = models.SlugField("Слаг", max_length=255, unique=True)

    class Meta:
        ordering = ['title']
        verbose_name = "Тема"
        verbose_name_plural = "Темы"

    def __str__(self):
        return self.title


class Course(models.Model):
    """ Модель курса """
    owner = models.ForeignKey(User,
                            verbose_name='Автор курса', 
                            related_name='courses_created',
                            on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,
                            verbose_name='Предмет', 
                            related_name='courses',
                            on_delete=models.CASCADE)
    title = models.CharField("Заголовок", max_length=255)
    slug = models.SlugField("Слаг", max_length=255, unique=True)
    overview = models.TextField("Краткий обзор курса")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    students = models.ManyToManyField(User,
                                    related_name='courses_joined',
                                    blank=True)

    class Meta:
        ordering = ['-created']
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title


class Module(models.Model):
    """ Модель модуля курса """
    course = models.ForeignKey(Course,
                            verbose_name="Модуль",
                            related_name='modules',
                            on_delete=models.CASCADE)
    title = models.CharField("Заголовок", max_length=255)
    description = models.TextField("Описание", blank=True)
    order = OrderField(blank=True, for_fields=['course'])

    class Meta:
        ordering = ['order']
        verbose_name = "Модуль"
        verbose_name_plural = "Модули"

    def __str__(self):
        return f'{self.order}. {self.title}'


class Content(models.Model):
    """ Модель контента """
    module = models.ForeignKey(Module,
                            verbose_name='Модуль',
                            related_name='contents',
                            on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,
                                    verbose_name='Тип контента',
                                    on_delete=models.CASCADE,
                                    limit_choices_to={'model__in':(
                                            'text',
                                            'video',
                                            'image',
                                            'file')})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']


class ItemBase(models.Model):
    """ Базовая абстрактная модель контента """ 
    owner = models.ForeignKey(User,
                            verbose_name='Автор курса',
                            related_name='%(class)s_related',
                            on_delete=models.CASCADE)
    title = models.CharField("Заголовок", max_length=255)
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    updated = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def render(self):
        return render_to_string('courses/content/{}.html'.format(
                    self._meta.model_name), {'item': self})



class Text(ItemBase):
    """ Модель контента - текст """
    content = models.TextField()


class File(ItemBase):
    """ Модель контента - файл """
    file = models.FileField(upload_to='files')


class Image(ItemBase):
    """ Модель контента - изображения """
    file = models.FileField(upload_to='images')


class Video(ItemBase):
    """ Модель контента - видео """
    url = models.URLField()
