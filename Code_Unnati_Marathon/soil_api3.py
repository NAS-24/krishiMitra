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
    'Authorization': '7046b922-cfe8-11ef-9159-0242ac130003-7046b9c2-cfe8-11ef-9159-0242ac130003'  #Using GMAIL:-aryananil2005@gmail.com
  }
)

# Do something with response data.
# print(response.json())

Soil_Moisture=response.json()['hours'][0]['soilMoisture40cm']['noaa']
Soil_percentage=int(Soil_Moisture*100)
print(f"Soil Moisture: {Soil_percentage}%")


Soil_Temp=response.json()['hours'][0]['soilTemperature']['noaa']
print(f"Soil Temperature: {Soil_Temp}C")
