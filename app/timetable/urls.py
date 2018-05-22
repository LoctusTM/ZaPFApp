from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('aktable/', views.ak_table, name='ak_table'),
    path('timetable/', views.timetable, name='index'),
    path('database.json', views.timetable, name='index'),
]