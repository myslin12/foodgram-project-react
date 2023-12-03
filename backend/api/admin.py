from django.contrib import admin

# Register your models here.
from api.models import Recipe, Ingredient, IngredientInRecipe, Tag


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
