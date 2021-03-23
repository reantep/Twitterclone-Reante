from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('edit-tweet/<int:id>/', views.edit_tweet, name='edit-tweet'),

]