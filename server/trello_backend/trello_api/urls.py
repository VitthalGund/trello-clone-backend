from django.urls import path
from . import views

urlpatterns = [
    path("columns/", views.column_list_create, name="column-list-create"),
    path("columns/<int:pk>/", views.column_detail, name="column-detail"),
]
