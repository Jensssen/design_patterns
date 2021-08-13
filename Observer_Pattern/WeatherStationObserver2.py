from Observer import Observer
from Observable import Observable


class WeatherStationObserver2(Observer):
    def update(self, subject: Observable) -> None:
        if subject.temperature == 0 or subject.temperature >= 12:
            print("WeatherStationObserver2: Reacted to the event")
