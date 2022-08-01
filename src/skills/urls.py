from django.urls import path, include

from skills import views

app_name = 'skills'

urlpatterns = [
	path('', views.index, name='index'),
	path('add/<int:pk>/', views.add, name='add'),
	path('reduce/<int:pk>/', views.reduce, name='reduce')
]