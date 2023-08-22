from django.urls import path

from . import views

app_name = "dashboard"
urlpatterns = [
    path("", views.index, name="index"),
    path("new_room/", views.new_room, name="new_room"),
    path("room/<int:room_id>", views.room, name="room"),
    path("edit_room/<int:room_id>", views.edit_room, name="edit_room"),
]