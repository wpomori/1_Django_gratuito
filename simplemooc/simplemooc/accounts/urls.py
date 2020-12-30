from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include, re_path
from . import views
from simplemooc.accounts import views

app_name = "accounts"
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('sair/', LogoutView.as_view(next_page='core:home'), name='logout'),
    path('cadastra-se/', views.register, name='register'),
    path('nova-senha/', views.password_reset, name='password_reset'),
    #path('confirmar-nova-senha/', views.password_reset_confirm, name='password_reset_confirm'),
    #re_path(r'^(?P<slug>[\w_-]+)/$', views.details, name='details')
    re_path(r'^confirmar-nova-senha/(?P<key>[\w_-]+)/$', views.password_reset_confirm, name='password_reset_confirm'),
    path('editar/', views.edit, name='edit'),
    path('editar-senha/', views.edit_password, name='edit_password'),
]

