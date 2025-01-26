
# import arrow
import requests


lat=float(input("Enter the latitude: "))
long=float(input("Enter the Longitude: "))

latitude=lat
longitude=long

response=requests.get('https://rest.isric.org/soilgrids/v2.0/properties/query?',
                    params={'lat':latitude,'lon':longitude}
                    )

# print(response.status_code)
# print(response.json())

soil_Nitrogen = response.json()['properties']['layers'][4]['depths'][3]['values']['Q0.5']
# soil_Nitrogen_ppm=soil_Nitrogen*10
print(f"nitrogen at 15-30cm: {soil_Nitrogen} ppm")

soil_Ph = response.json()['properties']['layers'][7]['depths'][2]['values']['Q0.5']
soil_Ph=float(soil_Ph/10)
print(f"PH at 5-15cm: {soil_Ph}")

# soil_SOC= response.json()['properties']['layers'][10]['depths'][1]['values']['Q0.5']
# print(f"SOC at 5-15cm: {soil_SOC} dg/kg")