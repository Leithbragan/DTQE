from django.db import models

import user_management.models


class Word(models.Model):
    class Meta:
        verbose_name = u'слово'
        verbose_name_plural = u'слова'

    word = models.CharField(max_length=30, verbose_name=u'слово')
    transcription = models.CharField(max_length=35, verbose_name=u'транскрипция')

    def __str__(self):
        return self.word


class Translation(models.Model):
    class Meta:
        verbose_name = u'перевод'
        verbose_name_plural = u'переводы'

    word = models.CharField(max_length=30, verbose_name=u'перевод слова')
    word_value = models.ForeignKey(Word, verbose_name=u'слово')

    def __str__(self):
        return '%s - %s' % (self.word_value, self.word)


class UserDictionary(models.Model):
    class Meta:
        verbose_name = u'словарь пользователя'
        verbose_name_plural = u'словари пользователя'

    name = models.CharField(null=True, verbose_name=u'название', max_length=300)
    word = models.ForeignKey(Word, verbose_name=u'словарь')
    user = models.ForeignKey(user_management.models.User, verbose_name=u'пользователь')
    quantity = models.SmallIntegerField(verbose_name=u'количество')

    def __str__(self):
        return '%s количество слов: %s' % (self.name, self.quantity)






