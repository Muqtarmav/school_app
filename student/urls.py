from django.urls import path
from . import views

urlpatterns = [
    path('create-student/', views.createStudent, name="create-student"),
    path('get-student/', views.getStudentList, name="get-student")

]
