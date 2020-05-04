from django.contrib.auth.views import LoginView
from django.urls import path, include
from . import views
from simplemooc.accounts import views

app_name = "accounts"
urlpatterns = [
    #path('conta/', include(('simplemooc.accounts.urls'), namespace='accounts')),
    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('cadastra-se/', views.register, name='register'),
]
