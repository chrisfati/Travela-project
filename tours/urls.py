from django.urls import path
from . import views

urlpatterns = [
    path('', views.tour_list, name='tour_list'),
    path('book_now/<int:tour_id>/', views.book_now, name='book_now'),
    path('booking_history/', views.booking_history, name='booking_history'),
]

