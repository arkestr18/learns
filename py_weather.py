import pyowm
owm = pyowm.OWM('41b33e65cbf85aaa61dd7a5ee1e51dbd')
observation = owm.weather_at_place('Samara')
w = observation.get_weather()
print(w)