import requests

api_key = '5880yHdcbe5sXVvSG4Mm3B7V4ZyX4Tp9kJlRu7B2'
start_date = '2024-09-01'
end_date = '2024-09-07'


url = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}'

response = requests.get(url)

asteroid_list = []



if response.status_code == 200:
    data  = response.json()

    asteroids = data['near_earth_objects']



    for date in asteroids :
        print(f"Asteroids approaching on {date}")
        for asteroid in asteroids[date][:3]:
                print(f"Name : {asteroid['name']}")
                print(f"Estimated Diameter (km): {asteroid['estimated_diameter']['kilometers']}")
                print(f"Close Approach Date : {asteroid['close_approach_data'][0]['close_approach_date']}")
                print(f"Relative Velocity (km/h):{asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']}")
                print(f"Miss Distance (km): {asteroid['close_approach_data'][0]['miss_distance']['kilometers']}")
                print("-"*30)








    print("Data retrived successfully!")
else :
    print(f"Failed to retrieve data : {response.status_code}")
