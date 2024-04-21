from Observer import Observer
from Observable import Observable

from WeatherStationObservable import WeatherStation


class WeatherStationObserver2(Observer):

    def __init__(self, weatherstation: WeatherStation):
        self.weatherstation = weatherstation

    def update(self) -> None:
        if self.weatherstation.get_temperature() == 0 or self.weatherstation.get_temperature() >= 12:
            print("WeatherStationObserver2: Reacted to the event")
