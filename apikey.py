import requests
import folium

def get_location(ip_address):
  
    api_key = ""
    api_url = f"http://api.ipstack.com/{ip_address}?access_key={api_key}"

    try:
        response = requests.get(api_url)
        data = response.json()
        print(data)

        # Extract latitude and longitude
        latitude = data["latitude"]
        longitude = data["longitude"]
        print(latitude)
        print(longitude)

        return latitude, longitude
    except Exception as e:
        print(f"Error fetching location: {e}")
        return None

def display_on_map(latitude, longitude):
    
    user_map = folium.Map(location=[latitude, longitude], zoom_start=10)

    # Add a marker for the user's location
    folium.Marker(location=[latitude, longitude], popup="User Location").add_to(user_map)

    
    user_map.save("user_location_map.html")
    print("Map saved as user_location_map.html. Opening in the default web browser.")

if __name__ == "__main__":
    
    target_ip = input("Enter the target IP address (press Enter for your own IP): ") or requests.get("https://api64.ipify.org?format=json").json()["ip"]

    location = get_location(target_ip)

    if location:
        print(f"Location for IP {target_ip}: {location}")
        display_on_map(*location)
    else:
        print("Failed to fetch location.")
