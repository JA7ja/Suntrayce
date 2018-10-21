import googlemaps
import json
import pytz
import os
from sunposition import sunpos
from datetime import datetime
from timezonefinder import TimezoneFinder

#API Key for Google Geocoding
gmaps = googlemaps.Client(key=os.environ['GEOCODE_KEY'])
tf = TimezoneFinder()

#variable initization
address = '144 East Ave., Ithaca, NY 148530'
print(address)

#Gets latitude and longitude from enteted address
geocode_result = gmaps.geocode(address)
latitude = geocode_result[0]['geometry']['location']['lat']
longitude = geocode_result[0]['geometry']['location']['lng']
print('Latitude: ' + str(latitude))
print('Longitude: ' + str(longitude))

#Gets timezone of location
timezone_str = tf.certain_timezone_at(lng=longitude, lat=latitude)
print(timezone_str)

#Conerts timezone to utc
timezone = pytz.timezone(timezone_str)
utc = datetime.utcnow()
timezone = utc + timezone.utcoffset(utc)
print(timezone)

#uses sunposition's sunpos function to get angles
Azimuth = sunpos(utc, latitude, longitude, 0)[0]
Zenith = sunpos(utc, latitude, longitude, 0)[1]
Elevation = 90 - Zenith

print("Sun Azimuth angle (east to west): " + str(Azimuth) + "\nSun Zenith angle: " + str(Zenith) + "\nSun Elevation angle from horizon: " + str(Elevation))