# this program takes a location as input, makes a call to openweather.org,
#  gets weather data for the location and prettyprints it.


import json, requests

# APPID = 'be5ae0831dc93465c59daf6a11c2f03f'
location = input('Enter location: ' )
if (len(location) < 1 ):
    print('input a location')
    quit()

    # parsing the input location to the url.
url='https://api.openweathermap.org/data/2.5/weather?q=' +location+'&appid=be5ae0831dc93465c59daf6a11c2f03f'

    # getting the json data
response = requests.get(url)

response.raise_for_status()
parsed = json.loads(response.text)

print(json.dumps(parsed,indent=4))
main = parsed['main']['temp']
temp = round(main- 273.15,2)
print('it is ' + str(temp) + ' degrees')