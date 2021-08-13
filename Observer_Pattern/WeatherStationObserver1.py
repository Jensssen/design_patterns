from Observer import Observer
from Observable import Observable


class WeatherStationObserver1(Observer):
    def update(self, subject: Observable) -> None:
        if subject.temperature < 12:
            print("WeatherStationObserver1: Reacted to the event")
