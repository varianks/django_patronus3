from django.urls import path
from . import views

app_name = 'references'

urlpatterns = [
    path('', views.ReferenceListView.as_view(), name='reference_list'),
    path('reference/add/', views.ReferenceCreateView.as_view(), name='reference_create'),
    path('post/<int:pk>/update/', views.ReferenceUpdateView.as_view(), name='reference_update'),
    path('post/<int:pk>/delete/', views.ReferenceDeleteView.as_view(), name='reference_delete'),
]