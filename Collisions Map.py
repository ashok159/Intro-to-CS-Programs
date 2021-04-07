#Name: Ashok Surujdeo
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#Date: April 6, 2021
#This program runs: Collisions Map

import folium
import pandas as pd

name = input("Enter CSV file name: ")
html = input("Enter output file: ")
collisions = pd.read_csv(name)

mapNYC = folium.Map(location=[40.75, -74.125], zoom_start=10)
for index,row in collisions.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    newMarker = folium.Marker([lat,lon])
    newMarker.add_to(mapNYC)

mapNYC.save(outfile=html)
