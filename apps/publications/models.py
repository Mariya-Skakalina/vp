from django.db import models
from apps.user.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Topic(models.Model):
    title = models.CharField('Раздел', max_length=200, unique=True, null=True, blank=True)

    def __str__(self):
        return self.title


class Section(models.Model):
    name = models.CharField('Подраздел', max_length=255, unique=True, null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Public(models.Model):
    title = models.CharField('Заголовок', max_length=255, unique=False)
    ctx = RichTextUploadingField(db_index=True)
    section = models.ManyToManyField(Section)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    date_time = models.DateTimeField(auto_now_add=True)
    publication = models.BooleanField(default=False)

    def __str__(self):
        return self.title
