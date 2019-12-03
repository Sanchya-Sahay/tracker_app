from django.urls import path
from . import views
urlpatterns = [
    path('',views.sightings),
    path('add/', views.new_sighting),
    path('stats/', views.stats),
    path('<str:unique_squirrel_id>/', views.sighting_update),
    path('<str:unique_squirrel_id>/delete', views.sighting_delete),
]

