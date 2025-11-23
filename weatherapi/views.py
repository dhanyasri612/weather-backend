import requests
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class WeatherAPIView(APIView):
    def get(self, request):
        city = request.query_params.get('city', None)

        if not city:
            return Response({"error": "City parameter is required."}, status=400)
        
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geo_response = requests.get(geo_url)
        geo_data = geo_response.json()

        if 'results' not in geo_data or len(geo_data['results']) == 0:
            return Response({"error": "City not found."}, status=404)
        
        res = geo_data['results'][0]
        lat = res['latitude']
        lon = res['longitude']

        if not lat or not lon:
            return Response({"error": "Latitude and Longitude are required parameters."}, status=400)
        
        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}"
            "&daily=sunrise,sunset,daylight_duration,sunshine_duration,uv_index_max,"
            "uv_index_clear_sky_max,weathercode,temperature_2m_max,temperature_2m_min,"
            "apparent_temperature_max,apparent_temperature_min,wind_speed_10m_max,wind_gusts_10m_max"
            "&hourly=temperature_2m,wind_speed_10m,wind_speed_80m,wind_speed_120m,"
            "wind_speed_180m,wind_direction_10m,wind_direction_80m,temperature_180m,"
            "temperature_120m,temperature_80m,wind_gusts_10m,wind_direction_180m,"
            "wind_direction_120m,cloud_cover,cloud_cover_low,cloud_cover_mid,"
            "cloud_cover_high,rain,snowfall,showers,snow_depth,soil_temperature_0cm,"
            "soil_temperature_6cm,soil_temperature_18cm,soil_temperature_54cm,"
            "soil_moisture_0_to_1cm,soil_moisture_3_to_9cm,soil_moisture_9_to_27cm,"
            "soil_moisture_27_to_81cm,soil_moisture_1_to_3cm,weathercode"
            "&current=temperature_2m,wind_speed_10m,wind_direction_10m,rain,cloud_cover,weathercode"
            "&timezone=auto"
        )


        response = requests.get(url)

        if response.status_code != 200:
            return Response({"error": "Failed to fetch weather data."}, status=response.status_code)

        weather_data = response.json()

        print(weather_data.keys())
        print("\n")
        print(weather_data["current"].keys())
        print("\n")
        print(weather_data["hourly"].keys())

        print(weather_data)




        #print(weather_data)  # Debugging statement

        return Response(weather_data)
