from django.db import models

# Create your models here.
class RecipeDb(models.Model):
    recipe_name = models.CharField(max_length=150)
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.CharField(max_length=100)
    preparation_time = models.PositiveIntegerField(help_text= "(in minutes)")
    cooking_time = models.PositiveIntegerField(help_text= "(in minutes)")
    servings = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)