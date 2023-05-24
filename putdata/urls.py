from django.urls import path
from . import views


#dont use verbs in endpoints as the HTTP methods are already in verb form

urlpatterns = [
    path('', views.getUsers),
    path('newuser', views.addUser),
    path('queryuser/<str:pk>', views.getUser),
    path('modifieduser/<str:pk>', views.updateUser),
    path('removeduser/<str:pk>', views.deleteUser)
]
