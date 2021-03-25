from django.db import models

class Cooker(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=250)
    prepationMode = models.CharField(max_length=250)
    prepationTime = models.IntegerField()
    cooker = models.ForeignKey(Cooker, on_delete=models.CASCADE)

    def __str__(self):
        return self.name