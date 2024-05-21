from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import User, Hotel, SampleImage, RoomType, Room, Owner, Staff
from .forms import RegisterHotelForm, RegisterRoomTypeForm, RegisterRoomForm, UploadRoomPicsForm


def dashboard(request):
    return render(request, 'account/dashboard.html', {})


def register_hotel(request):
    if request.method == "POST":
        form = RegisterHotelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Hotel registration was successful")
            return redirect("register-hotel")
        else:
            messages.error(
                request, "Sorry! The Hotel could not be registered. Please try again.")
            return render(request, 'account/register_hotel.html', {'form': form})
    else:
        form = RegisterHotelForm()
        return render(request, 'account/register_hotel.html', {'form': form})


def register_room_type(request):
    if request.method == "POST":
        form = RegisterRoomTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Hotel Room registration was successful")
            return redirect("register-room-type")
        else:
            messages.error(
                request, "Sorry! The Hotel Room could not be registered. Please try again.")
            return render(request, 'account/register_room_type.html', {'form': form})
    else:
        room_types = RoomType.objects.all().order_by('id')
        form = RegisterRoomTypeForm()
        return render(request, 'account/register_room_type.html', {'form': form, 'room_types': room_types})


def edit_room_type(request, id):
    if request.method == "POST":
        form = RegisterRoomTypeForm(request.POST or None,
                                    instance=RoomType.objects.get(id=id))
        if form.is_valid():
            form.save()
            messages.success(
                request, "Hotel Room Type has been updated successfully")
            return redirect("register-room-type")
        else:
            messages.error(
                request, "Sorry! The Hotel Room Type could not be changed. Please try again.")
            return render(request, 'account/register_room_type.html', {'form': form})
    else:
        room_type = RoomType.objects.get(id=id)
        return render(request, 'account/edit_room_type.html', {'room_type': room_type})


def delete_room_type(request, id):
    instance = RoomType.objects.get(id=id)
    if instance:
        instance.delete()
        messages.success(request, "Room Type was successfully deleted")
        return redirect("register-room-type")


def register_room(request):
    if request.method == "POST":
        form = RegisterRoomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Room registration was successful")
            return redirect("register-room")
        else:
            messages.error(
                request, "Sorry! The Room could not be registered. Please try again.")
            return render(request, 'account/register_room.html', {'form': form})
    else:
        form = RegisterRoomForm()
        return render(request, 'account/register_room.html', {'form': form})


def upload_room_pics(request):
    if request.method == "POST":
        files = request.FILES.getlist('sample_files')
        if files:
            form = UploadRoomPicsForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                for img_file in files:
                    new_file = SampleImage(
                        hotel=instance.hotel, room=instance.room, sample=img_file)
                    new_file.save()
                messages.success(request, "Rooms Pics upload was successful")
                return redirect("upload-room-pics")
            else:
                messages.error(
                    request, "Sorry! The Room Pics could not be uploaded. Please try again.")
                return render(request, 'account/upload_room_pics.html', {'form': form})
    else:
        form = UploadRoomPicsForm()
        return render(request, 'account/upload_room_pics.html', {'form': form})
