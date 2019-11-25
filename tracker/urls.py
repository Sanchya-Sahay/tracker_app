from django.urls import path
from . import views
urlpatterns = [
       path('',views.sightings),
       path(<'int:unique_squirrel_id/'>, views.sighting_update),
       path('add/', view.new_sighting),
       path('stats/', view.stats),
]

