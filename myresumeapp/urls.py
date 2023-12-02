# yourapp/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact_form, name='contact_form'),
    # Add more paths for other pages as needed
]
