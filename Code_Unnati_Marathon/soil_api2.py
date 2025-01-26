import arrow
import requests

lat=float(input("Enter the latitude: "))
long=float(input("Enter the Longitude: "))

#Get first hour of today
start = arrow.now()
# end=arrow.now()


response = requests.get(
  'https://api.stormglass.io/v2/bio/point',
  params={
    'lat': lat,   
    'lng':  long,
    'params': ','.join(['soilMoisture40cm', 'soilTemperature']),
    'start': start.to('UTC').timestamp(),  # Convert to UTC timestamp
    'end': start.to('UTC').timestamp()  # Convert to UTC timestamp
  },
  headers={
    'Authorization': '2a1bfe30-cddb-11ef-ae24-0242ac130003-2a1bfec6-cddb-11ef-ae24-0242ac130003' #Using GMAIL:-namananil2005@gmail.com
  }
)

# Do something with response data.

# print(response.json())

Soil_Moisture=response.json()['hours'][0]['soilMoisture40cm']['noaa']
Soil_percentage=Soil_Moisture*100
print(f"Soil Moisture: {Soil_percentage}%")

Soil_Temp=response.json()['hours'][0]['soilTemperature']['noaa']
print(f"Soil Temperature: {Soil_Temp}C")
