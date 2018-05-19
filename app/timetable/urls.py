from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('timetable/', views.timetable, name='index'),
    path('database.json', views.timetable, name='index'),
]