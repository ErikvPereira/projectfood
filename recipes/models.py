from django.db import models

from django.contrib.auth.models import User


class Recipe(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=200
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.title
    
class Ingredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )

    name = models.CharField(max_length=200)

    quantity = models.CharField(max_length=100)

class Step(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='steps'
    )

    order = models.PositiveIntegerField()

    description = models.TextField()

