from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()


router.register('films', views.FilmViewSet)
router.register('screens', views.ScreenViewSet)


urlpatterns = [
    path('', include(router.urls)),    
]