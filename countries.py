import requests

resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()

for country in sorted(countries,key=lambda d : d['population'], reverse=True):
    print(f"{country['name']:50} {country['capital']:30}  {country['population']:12}")