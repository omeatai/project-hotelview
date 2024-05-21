from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django_resized import ResizedImageField


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=10, blank=True, null=True, choices=[
                              ('MALE', 'MALE'), ('FEMALE', 'FEMALE')])
    phone = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.username

    class Meta:
        ordering = ['username']
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Hotel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True)
    image = ResizedImageField(upload_to='hotels_profile_pic')

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'

    # def save(self):
    #     super().save()
    #     img = Image.open(self.image.path)
    #     landscape = (1200, 628)
    #     portrait = (628, 1200)
    #     square = (1200, 1200)
    #     output_size = None
    #     if img.width > img.height and (img.width > 1200 or img.height > 628):
    #         output_size = landscape
    #     elif img.width < img.height and (img.width > 628 or img.height > 1200):
    #         output_size = portrait
    #     elif img.width == img.height and (img.width > 1200 or img.height > 1200):
    #         output_size = square
    #     img.thumbnail(output_size)
    #     img.save(self.image.path)


class RoomType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Room Type'
        verbose_name_plural = 'Room Types'


class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)
    number = models.CharField(max_length=100, unique=True)
    room_type = models.ForeignKey(
        RoomType, on_delete=models.CASCADE, related_name="room_type")
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, related_name="room_hotel")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'


class SampleImage(models.Model):
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, related_name='sample_hotel')
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name='sample_room')
    sample = ResizedImageField(upload_to='hotels_sample_pics')

    def __str__(self) -> str:
        return self.hotel.name

    class Meta:
        ordering = ['hotel']
        verbose_name = 'Sample Image'
        verbose_name_plural = 'Sample Images'


class Owner(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='owner_user', unique=True)
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, related_name='owner_hotel')

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        ordering = ['user']
        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'


class Staff(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='staff_user', unique=True)
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, related_name='staff_hotel')

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        ordering = ['user']
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'
