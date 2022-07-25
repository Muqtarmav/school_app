from django.urls import path

from school import views

urlpatterns = [
    path('create-school/', views.createSchool, name="create-school"),
    path('list-school', views.listSchool, name="list-school"),
]