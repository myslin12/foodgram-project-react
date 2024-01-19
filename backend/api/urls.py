from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from .views import (CustomUserViewSet, IngredientViewSet, RecipeViewSet,
                    TagViewSet)

app_name = 'api'

router = DefaultRouter()

router.register('ingredients', IngredientViewSet)
router.register('tags', TagViewSet)
router.register('recipes', RecipeViewSet)
router.register('users', CustomUserViewSet)


urlpatterns = [
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'', include(router.urls)),
]
