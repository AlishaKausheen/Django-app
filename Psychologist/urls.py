from django.contrib import admin
from django.urls import path, include
from django.urls import reverse
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetConfirmView

urlpatterns = [
    path('', views.home, name = 'home'),
    path('signup', views.signup, name ='signup'),
    path('signin', views.signin, name ='signin'),
    path('signout', views.signout, name ='signout'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name = "activate"),
    path('psychology', views.psychology, name = 'psychology'),
    path('contact', views.contact, name='contact'), 
    path('analyze/', views.analyze_sentiment_emotion, name='analyze_sentiment_emotion'),


]

