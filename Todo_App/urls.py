from django.urls import path
from Todo_App.views import *

urlpatterns = [
    path('', home, name='home'),
    path('update/<int:pk>', update, name='update'),
    path('delete/<int:pk>', delete, name='delete'),
]