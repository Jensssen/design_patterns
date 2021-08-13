from random import randrange
from typing import List

from Observer import Observer
from Observable import Observable


class WeatherStation(Observable):
    """
    The WeatherStation owns some important state such as temperature and notifies observers when the state
    changes.
    """

    temperature: int = None

    # _observers holds a List of all Observers to this Weather station
    # This list of subscribers could also be stored more comprehensively eg by event, type, etc...
    _observers: List[Observer] = []

    def addObserver(self, observer: Observer) -> None:
        print(f"WeatherStation: Attached an observer with name {type(observer).__name__}.")
        self._observers.append(observer)

    def removeObserver(self, observer: Observer) -> None:
        print(f"WeatherStation: Removed an observer with name {type(observer).__name__}.")
        self._observers.remove(observer)

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("WeatherStation: Notifying observers...")
        for observer in self._observers:
            observer.update()

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        self.temperature = randrange(0, 30)
        print(f"WeatherStation: Temperature has just changed to: {self.temperature}")
        self.notify()

    def get_temperature(self) -> int:
        return self.temperature
