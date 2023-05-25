from django.urls import path

from .views import (
    HomeView,
    ProjectView,
    ProjectByTag,
    get_category
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<str:slug>/', get_category, name='category'),
    path('tag/<str:slug>/', ProjectByTag.as_view(), name='tag'),
    path('single/<str:slug>/', ProjectView.as_view(), name='single'),
]