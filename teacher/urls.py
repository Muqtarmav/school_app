
from django.urls  import path
from .import views


urlpatterns = [

    path('create-teacher/', views.createTeacher, name="create-teacher"),
    path('get-teacher/', views.getTeacher, name="get-teacher")


]