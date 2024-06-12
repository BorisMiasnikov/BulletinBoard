from django.db import models

from django.contrib.auth.models import User



class Category(models.Model): # сущность категории
    #атрибуты категории
    name = models.TextField(unique=True)# атрибут категории - имя
    subscriber = models.ManyToManyField(User, related_name="name")
    pass


class Bulletin(models.Model): # сущность объявления
    #атрибуты объявления
    title = models.TextField(null=False)
    text = models.TextField(max_length=3000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_in = models.DateTimeField(auto_now_add=True)
    pass


class Feedback(models.Model):  # сущность отклика
    #атрибуты отклика
    text = models.TextField(max_length=3000)
    bulletin = models.ForeignKey(Bulletin, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pass
