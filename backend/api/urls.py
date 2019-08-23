from django.urls import path
from . import views

urlpatterns = [
    path('flights/', views.FlightList.as_view()),
    path('flights/<int:pk>/', views.FlightDetail.as_view()),
    path('seats/', views.SeatList.as_view()),
    path('seats/<int:pk>/', views.SeatDetail.as_view()),
    path('passengers/', views.PassengerList.as_view()),
    path('passengers/<int:pk>/', views.PassengerDetail.as_view()),
    path('gameboard', views.get_gameboard, name='get_gameboard')

]
