# importing geopy library
from geopy.geocoders import Nominatim
import pandas as pd


# Activity to Locations
df = pd.read_excel('Activity.xlsx')
df =  df.truncate(after = 56)

geolocator = Nominatim(user_agent="locs_py")

for i in range(len(df['Location/Place (Beta)'])):
    print(df.loc[i,'Location/Place (Beta)'])

    location = geolocator.geocode(df.loc[i,'Location/Place (Beta)'] + " Brisbane Queensland")
    if location is None:
        location = geolocator.geocode(df.loc[i,'Location/Place (Beta)'] +  " Queensland")
    df.loc[i,'latitude'] = location.latitude
    df.loc[i,'longitude'] = location.longitude
    print(location)
df.to_excel('NewActivity.xlsx')
df = pd.read_excel('NewActivity.xlsx')

price = df['Price'].unique()

print(price)
# New to Analysis
# geolocator = Nominatim(user_agent="locs_py")
# location = geolocator.geocode("Mount Coot-tha Brisbane QLD")
# print(location.address)


