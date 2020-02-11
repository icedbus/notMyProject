import googlemaps
import pandas as pd

data = pd.read_csv("orderZip copy.csv")
gmaps = googlemaps.Client(key='AIzaSyAi-MdES9xokd7nH2MtLehlPqQbA9c6r_E') 
#I don't do illegal stuff with my key lol I will give you out if they caught me
data["address"] = None
address = pd.DataFrame(columns=['address'])
for i in range(0, len(data), 1):
  reverse_geocode_result = gmaps.reverse_geocode((data.loc[i,'latitude'], data.loc[i,'longitude']))
  data.loc[i, 'address'] = reverse_geocode_result[0]["formatted_address"]


#print(reverse_geocode_result.loc[data.loc[0,'city'], "formatted_address"])

pd.DataFrame(data).to_csv("orderAddress.csv", encoding='utf8')