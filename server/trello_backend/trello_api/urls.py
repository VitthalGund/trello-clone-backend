from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome, name="welcome-default route"),
    path("columns/", views.column_list_create, name="column-list-create"),
    path("columns/<int:pk>/", views.column_detail, name="column-detail"),
    path("columns/reorder/", view=views.reorder_columns, name="reorder_columns"),
    path("cards/", views.create_card, name="card_list_create"),
    path(
        "cards/<int:card_id>/",
        views.card_retrieve_update_delete,
        name="card_retrieve_update_delete",
    ),
    path("cards/move/<int:card_id>/", views.move_card, name="move_card"),
]
