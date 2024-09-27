from django.urls import path
from . import views

urlpatterns = [
    path('signup/cliente/', views.signup_cliente, name='signup_cliente'),
    path('signup/medico/', views.signup_medico, name='signup_medico'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
]
