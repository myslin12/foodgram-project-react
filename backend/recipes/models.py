from colorfield.fields import ColorField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import UniqueConstraint

from users.models import User


class Ingredient(models.Model):

    name = models.CharField('Название', max_length=200)
    measurement_unit = models.CharField('Единица измерения', max_length=200)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ['name']
        constraints = [
            UniqueConstraint(
                fields=['name', 'measurement_unit'],
                name='ingredient_name_measurement_unit'
            )
        ]

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class Tag(models.Model):

    name = models.CharField('Название', max_length=200)
    color = ColorField('Цветовой код', unique=True, max_length=10)
    slug = models.SlugField('Уникальный слаг', unique=True, max_length=200)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Recipe(models.Model):

    author = models.ForeignKey(
        User,
        related_name='recipes',
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Автор публикации',
    )
    name = models.CharField('Название', max_length=200)
    image = models.ImageField(
        'Изображение',
        upload_to='recipes/'
    )
    text = models.TextField('Текстовое описание')
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientInRecipe',
        related_name='recipes',
        verbose_name='Ингредиенты'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='Теги'
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления',
        validators=[MinValueValidator(
            1, message='Время приготовления не менее 1 минуты!'
        ), MaxValueValidator(
            1440, message='Время приготовления не более 24 часов!'
        )]
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class IngredientInRecipe(models.Model):

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredient_list',
        verbose_name='Рецепт',
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент',
    )
    amount = models.PositiveSmallIntegerField('Количество')

    class Meta:
        verbose_name = 'Ингредиент в рецепте'
        verbose_name_plural = 'Ингредиенты в рецептах'

    def __str__(self):
        return (f'{self.ingredient.name} \
                ({self.ingredient.measurement_unit}) - {self.amount}')


class Favourite(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Рецепт',
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'

    def __str__(self):
        return f'{self.user} добавил "{self.recipe}" в Избранное'


class ShoppingCart(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Рецепт',
    )

    class Meta:
        verbose_name = 'Корзина покупок'
        verbose_name_plural = 'Корзина покупок'

    def __str__(self):
        return f'{self.user} добавил "{self.recipe}" в Корзину покупок'
