import googlemaps
import pandas as pd
# pip install openpyxl

#maps_client = googlemaps.Client(API_KEY);
def miles_to_meters(miles):
    try:
        return miles * 1_609.344
    except:
        return 0


API_KEY = 'AIzaSyBkggWLN5cIFpGJ1IjNSuw7oKUHfo1U5HY'
map_client = googlemaps.Client(API_KEY)

#address = '333 Market St, San Francisco, CA'
#geocode = map_client.geocode(address=address)
#(lat, lng) = map(geocode[0]['geometry']['location'].get, ('lat', 'lng'))

location = (37.77980361, -122.4386414) # long, lat
search_string = 'food' # keywords
radius = miles_to_meters(10) # radius
business_list = []

response = map_client.places_nearby(
    location=location,
    keyword=search_string,
    name='chinese', # ??? difference between keyword and name?
    radius=radius
)

business_list.extend(response.get('results'))
df = pd.DataFrame(business_list)
df['url'] = 'https://www.google.com/maps/place/?q=place_id:' + df['place_id']
df.to_excel('preferences.xlsx', index=False)



