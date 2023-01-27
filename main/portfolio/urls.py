from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('category/<str:slug>/', get_category, name='category'),
    path('tag/<str:slug>/', ProjectByTag.as_view(), name='tag'),
    path('single/<str:slug>/', ProjectView.as_view(), name='single'),
]