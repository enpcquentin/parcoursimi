from django.urls import path
from parcours import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home', views.home, name='home'),
    path('connexion', views.connexion, name='connexion'),
    path('mdp_oublie', auth_views.password_reset, name='password_reset'),
    path('mdp_oublie/done', auth_views.password_reset_done, name='password_reset_done'),
    path('inscription', views.inscription, name='inscription'),
    path('deconnexion', views.deconnexion, name='deconnexion'),

]
