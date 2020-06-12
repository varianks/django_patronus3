from django.urls import path
from . import views


app_name = 'references'
urlpatterns = [
    path('references/', views.ReferenceListView.as_view(), name ='api_reference_list'),
]