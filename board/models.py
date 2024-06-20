from django.db import models

from django.contrib.auth.models import User



class Category(models.Model): # сущность категории
    #атрибуты категории
    name = models.TextField(unique=True)# атрибут категории - имя
    subscriber = models.ManyToManyField(User, related_name="name")

    def __str__(self):
        return f'{self.name}'


class Bulletin(models.Model): # сущность объявления
    #атрибуты объявления
    title = models.CharField(max_length=255,default="Этот заголовок загловляет")
    text = models.TextField(default="Это объявление объявляет")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


class Feedback(models.Model):  # сущность отклика
    #атрибуты отклика
    text = models.TextField(default="Этот отклик откликивает")
    bulletin = models.ForeignKey(Bulletin, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    accepted = models.BooleanField(null=True)


