from django.db import models


# Create your models here.
class Problem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    solutions = models.TextField()
    signs = models.ManyToManyField("Sign", related_name="problems")

    def __str__(self):
        return self.name


class Sign(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
