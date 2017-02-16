import folium
import pandas

df=pandas.read_csv('all_india.csv')

map=folium.Map(location=[12.9298,77.676],zoom_start=7)
for lat,lon,name in zip(df['latitude'],df['longitude'],df['officename']):
    map.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color='red')))



map.save(outfile='India.html')
