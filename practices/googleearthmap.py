import web_browser

def find_city_on_google_earth(city_name):
    google_earth.url = f'https://earth.google.com/web/search/(city_name)'
    webbrowser.open(google_earth_url)

city = input("Name of city: ")
find_city_on_google_earth(city)