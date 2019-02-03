
from django.urls import path
from .import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('contact_us/',views.contact),
    path('count/',views.count, name='count')
]
