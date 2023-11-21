from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from .views import IngredientViewSet, RecipeViewSet, TagViewSet
from users.views import CustomUserViewSet

app_name = 'api'

router = DefaultRouter()

router.register('ingredients', IngredientViewSet)
router.register(r'tags', TagViewSet)
router.register(r'recipes', RecipeViewSet)
router.register('users', CustomUserViewSet)

urlpatterns = [
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'', include(router.urls)),
]
