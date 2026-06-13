from django.urls import path

from . import views


urlpatterns = [

    path('', views.home, name='home'),
    path('recipes/create/', views.create_recipe, name='create_recipe'),
]