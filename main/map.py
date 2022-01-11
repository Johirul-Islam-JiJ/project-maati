import folium
from folium.map import Tooltip

m = folium.Map(location=[24.250360916148043, 90.37652803770108],tiles="Stamen Terrain", zoom_start=12)

Tooltip='Click for more info'

folium.Marker([24.250360916148043, 90.37652803770108], 
              popup='<strong>Location One</strong>',
              tooltip=Tooltip).add_to(m)

folium.CircleMarker(
    location=[24.24772831760126, 90.37429927454673],
    radius=50,
    popup='My area',
    color ='#428bca',
    fill = True,
    fill_color ='#428bca'
).add_to(m)

m.save('map.html')