from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('AirMg/list/', views.flight_list, name='flight_list'),
    path('AirMg/search/', views.flight_search, name='flight_search'),
    path('AirMg/add/', views.flight_add, name='flight_add'),
    path('AirMg/edit/<int:flight_id>/', views.flight_edit, name='flight_edit'),
]