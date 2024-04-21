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

    def get_max_speed_in_kmh(self) -> int:
        return 220

    def get_max_delivery_weight_in_kg(self) -> int:
        return 100

    def prepare_vehicle(self) -> None:
        print("Prepare Car.")


class Truck(Vehicle):

    def get_max_speed_in_kmh(self) -> int:
        return 120

    def get_max_delivery_weight_in_kg(self) -> int:
        return 1000

    def prepare_vehicle(self) -> None:
        print("Prepare Truck.")


class VehicleFactory:

    def create_and_prepare_vehicle(self, vehicle_speed: str) -> Vehicle:
        try:
            vehicle = self.create_vehicle(vehicle_speed)
            vehicle.prepare_vehicle()
            return vehicle
        except AttributeError:
            raise AttributeError(f"Vehicle Type {vehicle_speed} not supported.")

    def create_vehicle(self, vehicle_speed: str) -> Vehicle | None:
        if vehicle_speed == "fast":
            return Car()
        if vehicle_speed == "slow":
            return Truck()
        else:
            return None


def vehicle_factory() -> VehicleFactory:
    """Construct a vehicle object that allows to create a vehicle, based on the user's speed preference."""
    return VehicleFactory()


def main(factory: VehicleFactory) -> None:
    vehicle = factory.create_and_prepare_vehicle("slow")
    print(f"Vehicles max speed: {vehicle.get_max_speed_in_kmh()}")
    print(f"Vehicles max weight it can carry: {vehicle.get_max_delivery_weight_in_kg()}")


if __name__ == '__main__':
    main(vehicle_factory())
