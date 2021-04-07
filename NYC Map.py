#Name: Ashok Surujdeo
#Email: Ashok.Surujdeo65@myhunter.cuny.edu
#Date: April 6, 2021
#This program runs: NYC Map

import folium

mapNYC = folium.Map(location=[40.75, -74.125], zoom_start=10)
folium.Marker(location=[40.768731, -73.964915], popup = "Hunter College").add_to(mapNYC)

mapNYC.save(outfile='nycMap.html')
