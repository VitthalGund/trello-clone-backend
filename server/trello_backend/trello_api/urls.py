from django.urls import path
from . import views

urlpatterns = [
    path("columns/", views.column_list_create, name="column-list-create"),
    path("columns/<int:pk>/", views.column_detail, name="column-detail"),
    path("columns/reorder/", view=views.reorder_columns, name="reorder_columns"),
]
