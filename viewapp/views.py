from django.shortcuts import render
from django.http import HttpResponse
import folium
# import geocoder

from account.models import Hotel


def home(request):

    hotels = Hotel.objects.all()
    base_path = request.build_absolute_uri()

    # Create Map Object
    mapper = folium.Map(location=[5.8, 7],
                        zoom_start=10, tiles="OpenStreetMap")

    for hotel in hotels:
        # Variables
        place = hotel.name
        latitude = hotel.latitude
        longitude = hotel.longitude
        booking_link = f"{base_path}booking/{hotel.id}"
        google_maps_link = f"https://www.google.com/maps/@{
            latitude},{longitude},17z?entry=ttu"
        search_term = hotel.name.replace(" ", "+")
        search_link = f"https://www.google.com/search?q={search_term}"
        popup_text = f"""
        <button class="btn btn-secondary"><span class="text-light">{place}</span></button>
        <a href='{booking_link}' target="_top"><button class='btn btn-primary my-2'>Make a Booking</button></a>
        <a href='{google_maps_link}' target='_blank'><button class='btn btn-danger'>View on Google MAP</button></a>
        <a href='{search_link}' target='_blank'><button class='btn btn-warning my-2'>Search on Google</button></a>
        """

        folium.Marker(location=[latitude, longitude], tooltip="Click for Info",
                      popup=popup_text, icon=folium.Icon(icon="glyphicon-home", color="red")).add_to(mapper)

    # Get HTML Representation of Map Object
    m = mapper._repr_html_()
    # 6.22066, 7.06609 (De Santos Hotel, Awka)

    # Get the latitude and longitude with Geocoder
    # location = geocoder.osm(place)
    # lat = location.lat
    # lng = location.lng
    # country = location.country

    # https://www.google.com/search?q=de+Santos+Hotel+Awka
    # https://www.google.com/maps/@49.6987316,-112.8968462

    # m.save(footprint.html)

    # m = folium.Map(location=[41, 29], width="%100", height="%100")
    # for i in range(len(locations)):
    #     folium.CircleMarker(location=locations[i], radius=1).add_to(m)
    # m

    # Place Latitude Longitude Icon Color Link
    # Veena Stores 13.005995 77.569346 star green https: // goo.gl/maps/UZMSRAbTMzaCkAwCA
    # Refreshments 12.908313 77.587063 star green https: // goo.gl/maps/pMgKBK5FTDGdaRDr9

    context = {
        'm': m,
        'title': 'HotelView',
        'content_text': 'Welcome to the Home Page!'
    }
    return render(request, 'viewapp/home.html', context)


def contact(request):
    context = {
        'title': 'Hotel View',
        'content_text': 'Talk to us!'
    }
    return render(request, 'viewapp/contact.html', context)


def booking(request, id):
    hotel = Hotel.objects.get(id=id)
    context = {
        'title': 'Hotel View',
        'content_text': f'Make a Booking @ {hotel.name}'
    }
    return render(request, 'viewapp/booking.html', context)
