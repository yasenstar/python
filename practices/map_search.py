import folium
from geopy.geocoders import Nominatim
from IPython.display import display, HTML

location_name = input("Enter a location: ")

geolocator = Nominatim(user_agent="geoapi")
location = geolocator.geocode(location_name)

if location:

    # Create a map centered on the user's location
    latitude = location.latitude
    longitude = location.longitude
    clcoding = folium.Map(
        location = [latitude, longitude],
        zoom_start = 12
    )

    marker = folium.Marker(
        [latitude, longitude],
        popup = location_name
    )
    marker.add_to(clcoding)

    display(HTML(clcoding._repr_html_()))

else:
    print("Location not found, please try again.")