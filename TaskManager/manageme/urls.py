from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns in your project

    # Signup URL
    path('signup/', views.signup, name='signup'),

    # Login URL
    path('login/', views.login, name='login'),
]
