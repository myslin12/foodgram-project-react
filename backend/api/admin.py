# Register your models here.
from recipes.models import Ingredient, IngredientInRecipe, Recipe, Tag
from django.contrib import admin

admin.register(Recipe)
admin.register(Ingredient)
admin.register(IngredientInRecipe)
admin.register(Tag)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(IngredientInRecipe)
class IngredientInRecipeAdmin(admin.ModelAdmin):
    model = IngredientInRecipe
