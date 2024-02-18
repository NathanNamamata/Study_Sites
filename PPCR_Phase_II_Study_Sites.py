import folium
import os
import geopandas as gpd

# Load shapefile
shapefile_path = r'F:\Collecting and Analysing Data\Maps\Shapefiles\Selection of Study Sites\Study_Sites_V1.shp'
gdf = gpd.read_file(shapefile_path)
# Create a Folium map centered at a specific location
m = folium.Map(location=[-15, 30], zoom_start=6)

# Add shapefile data to the map
folium.GeoJson(gdf, tooltip=folium.GeoJsonTooltip(fields=['DistName', 'WardNm2020'], labels=True, sticky=True)).add_to(m)

# Add tiles as background
folium.TileLayer('OpenStreetMap').add_to(m)

# Add attribute information to the map
html = gdf.to_html()
popup = folium.Popup(html)
popup.add_to(m)

# Specify the path where you want to save the map HTML file
output_path = r'C:\Users\Naznamz\anaconda3\envs\study_sites_folium_project\PPCR_Phase_II_Study_Sites\PPCR_Phase_II_Study_Sites.html'
# Ensure the directory exists, if not create it
output_dir = os.path.dirname(output_path)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# Save the map to an HTML file
m.save(output_path)