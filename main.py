import pip._vendor.requests as requests
import json
import time
import paho.mqtt.publish as publish

 # Setările brokerului MQTT
 broker = "mqtt.beia-telemetrie.ro"
 port = 1883
 topic = "training/device/Ionescu-Stefania"
 topic_processed="training/device/Ionescu-Stefania/temperature"

 # Coordonatele geografice
 latitude = 44.1598
 longitude = 28.6348

 # Cheia API OpenWeatherMap
 api_key = "f80ba330cc9f0b9b8be76410d81ff742"

 # URL pentru obținerea datelor meteorologice
 weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"

 # URL pentru obținerea datelor de poluare a aerului
 pollution_url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={latitude}&lon={longitude}&appid={api_key}"

 # Funția pentru obținerea temperaturii curente din API
 def get_current_temperature():
 	response = requests.get(weather_url)
 	data = response.json()
 	temperature_kelvin = data["main"]["temp"]
 	temperature_celsius = temperature_kelvin - 273.15
 	return temperature_celsius

 # Funția pentru obținerea nivelului de poluare a aerului
 def get_air_pollution():
 	response = requests.get(pollution_url)
 	data = response.json()
 	air_pollution_index = data["list"][0]["main"]["aqi"]
 	return air_pollution_index

 # Publicarea datelor în mod continuu
 while True:
 	# Obținerea temperaturii curente
 	temperature = get_current_temperature()
 	print(f"Temperature: {temperature}°C")

 	# Obținerea nivelului de poluare a aerului
 	air_pollution = get_air_pollution()
 	print(f"Air Pollution Index: {air_pollution}")

 	payload_dict = {
     	"temperature": temperature,
     	"air_pollution": air_pollution
 	}

 	# Publicarea datelor în topic
 	publish.single(topic, hostname=broker, port=port, payload=json.dumps(payload_dict))

 	# Așteptare pentru o perioadă de timp
 	time.sleep(1)
