from django.urls import path
from basic_app import views
urlpatterns = [
    path('registration/',views.registration,name = 'registration'),
    path('user_login/',views.user_login,name = 'user_login')
]
