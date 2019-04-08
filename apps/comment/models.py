from django.db import models
from apps.publications.models import Public
from apps.user.models import User


class Comment(models.Model):
    public_comment = models.ForeignKey(Public, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    author_comment = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    answer = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text