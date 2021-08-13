from WeatherStationObservable import WeatherStation
from WeatherStationObserver1 import WeatherStationObserver1
from WeatherStationObserver2 import WeatherStationObserver2

if __name__ == "__main__":

    # Create a new Weather Station
    weatherStation = WeatherStation()

    # Create one Observer that observes the Weather Station
    weatherStationObserver1 = WeatherStationObserver1()
    weatherStation.addObserver(weatherStationObserver1)

    # Create a second Observer that also observes the Weather Station
    weatherStationObserver2 = WeatherStationObserver2()
    weatherStation.addObserver(weatherStationObserver2)

    # The Weather station performs some business logic (eg. measure the current temperature)
    weatherStation.some_business_logic()
    weatherStation.some_business_logic()

    # Remove one of the observers
    weatherStation.removeObserver(weatherStationObserver1)

    # The Weather station performs some business logic (eg. measure the current temperature)
    weatherStation.some_business_logic()
