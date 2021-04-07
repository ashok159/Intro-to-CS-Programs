#Name: Ashok Surujdeo
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#Date: April 6, 2021
#This program runs: Textile Drop-off Map

import pandas as pd
import folium

file = input("Please enter the name of the input file: ")
html = input("Please enter the name of the output file: ")
borough = input("Please enter the name of the borough: ")

textile = pd.read_csv(file)
location = textile.groupby('Borough').get_group(borough)

mapTextile = folium.Map(location=[40.75, -74.125], zoom_start=10)

for index, row in location.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Address"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapTextile)

mapTextile.save(outfile=html)
