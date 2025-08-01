from django.urls import path
from . import views


urlpatterns = [
    path('add/',views.add,name='add'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('update/<int:pk>/',views.update,name='update'),
]