from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('register_hotel', views.register_hotel, name="register-hotel"),
    path('register_room_type', views.register_room_type, name="register-room-type"),
    path('edit_room_type/<int:id>', views.edit_room_type,
         name="edit-room-type"),
    path('delete_room_type/<int:id>', views.delete_room_type,
         name="delete-room-type"),
    path('register_room', views.register_room, name="register-room"),
    path('upload_room_pics', views.upload_room_pics, name="upload-room-pics"),
]
