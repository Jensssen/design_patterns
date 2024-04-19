from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def get_max_speed_in_kmh(self) -> int:
        """Get maximum speed of vehicle in km/h."""

    @abstractmethod
    def get_max_delivery_weight_in_kg(self) -> int:
        """Get max weight, the vehicle can carry."""

    @abstractmethod
    def prepare_vehicle(self) -> None:
        """Prepare vehicle"""


class Car(Vehicle):
    """Regular Car Vehicle."""

    def get_max_speed_in_kmh(self) -> int:
        return 220

    def get_max_delivery_weight_in_kg(self) -> int:
        return 100

    def prepare_vehicle(self) -> None:
        print("Prepare Car.")


class Truck(Vehicle):
    """Regular Truck Vehicle."""

    def get_max_speed_in_kmh(self) -> int:
        return 120

    def get_max_delivery_weight_in_kg(self) -> int:
        return 1000

    def prepare_vehicle(self) -> None:
        print("Prepare Truck.")


class VehicleFactory(ABC):

    def create_and_prepare_vehicle(self) -> Vehicle:
        """Create and prepare a new Vehicle that belongs to this Factory."""
        vehicle = self.create_vehicle()
        vehicle.prepare_vehicle()
        return vehicle

    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        """Get vehicle for use."""


class FastGroundVehicleFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Car()


class SlowGroundVehicleFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Truck()


def create_factory() -> VehicleFactory:
    factories = {
        "slow": SlowGroundVehicleFactory(),
        "fast": FastGroundVehicleFactory()
    }
    while True:
        delivery_speed = input("Enter desired delivery speed (fast, slow): ")
        if delivery_speed in factories:
            return factories[delivery_speed]
        print(f"Unknown delivery speed option: {delivery_speed}.")


def main(vehicle_factory: VehicleFactory) -> None:
    vehicle = vehicle_factory.create_and_prepare_vehicle()
    print(f"Vehicles max speed: {vehicle.get_max_speed_in_kmh()}")
    print(f"Vehicles max weight it can carry: {vehicle.get_max_delivery_weight_in_kg()}")


if __name__ == '__main__':
    factory = create_factory()
    main(factory)
