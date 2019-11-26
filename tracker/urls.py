from django.urls import path
from . import views
urlpatterns = [
       path('',views.sightings),
       path('<int:unique_squirrel_id/>', views.sighting_update),
       path('add/', views.new_sighting),
       path('stats/', views.stats),
]

