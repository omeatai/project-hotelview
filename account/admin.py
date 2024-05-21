from django.contrib import admin
from .models import User, Hotel, SampleImage, RoomType, Room, Owner, Staff


class UserAdmin(admin.ModelAdmin):
    exclude = ("groups", "user_permissions")
    list_display = ["username", "first_name", "last_name", "email", "gender"]


class HotelAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ["name", "location", "latitude",
                    "longitude", "description", "image"]


class RoomTypeAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ["name"]


class RoomAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ["name", "number", "room_type", "hotel"]


class SampleImageAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ["hotel", "room", "sample"]


class OwnerAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ["user", "hotel"]


class StaffAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ["user", "hotel"]


admin.site.register(User, UserAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(RoomType, RoomTypeAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(SampleImage, SampleImageAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Staff, StaffAdmin)
