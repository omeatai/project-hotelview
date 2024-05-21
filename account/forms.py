from django import forms
from .models import Hotel, RoomType, Room, SampleImage


class RegisterHotelForm(forms.ModelForm):

    image = forms.ImageField(label='Upload Hotel Profile Pic', required=True)

    class Meta:
        model = Hotel
        exclude = []
        # fields = '__all__'


class RegisterRoomTypeForm(forms.ModelForm):

    class Meta:
        model = RoomType
        exclude = []
        # fields = '__all__'


class RegisterRoomForm(forms.ModelForm):

    class Meta:
        model = Room
        exclude = []
        # fields = '__all__'


class UploadRoomPicsForm(forms.ModelForm):

    class Meta:
        model = SampleImage
        exclude = ['sample']
        # fields = '__all__'
