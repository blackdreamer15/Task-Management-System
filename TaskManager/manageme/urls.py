from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns in your project

    # Signup URL
    path('signup/', views.signup, name='signup'),

    # Login URL
    path('login/', views.login, name='login'),

    # Tasks URL
    path('tasks/', views.tasks, name='tasks'),

    #home URL
    path('', views.index, name='index'),

    #about URL
    path('about/', views.about, name='about'),
]
