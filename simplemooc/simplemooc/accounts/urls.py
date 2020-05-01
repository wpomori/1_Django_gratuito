from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
]
