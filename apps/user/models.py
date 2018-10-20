from django.db import models
from django.conf import settings
import random
import string
import crypt


class User(models.Model):
    nickname = models.CharField('Никнейм(логин)', max_length=200, unique=True)
    email = models.EmailField('Email', max_length=200, unique=True)
    password = models.CharField('Пароль', max_length=30)
    code = models.CharField('Код активации', max_length=200, null=True)
    activate = models.BooleanField('Активный', default=False)

    # Генерирует случайный код
    def id_activate(self, size=15, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    # Хэширование пароля
    def hash_password(self):
        return crypt.crypt(str(self.password), settings.SECRET_KEY_2)

    def save(self, **kwargs):
        if self.id:
            pass
        else:
            self.code = self.id_activate()
            self.password = self.hash_password()
        return super(User, self).save(**kwargs)

    def __str__(self):
        return self.nickname