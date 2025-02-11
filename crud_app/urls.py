
from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home_page'),
    path('delete/<int:id>/',deletion,name='delete_page'),
    path('update/<int:id>/',updation,name='edit_page'),
]
