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


class Airplane(Vehicle):

    def get_max_speed_in_kmh(self) -> int:
        return 800

    def get_max_delivery_weight_in_kg(self) -> int:
        return 5000

    def prepare_vehicle(self) -> None:
        print("Prepare Airplane.")


class Helicopter(Vehicle):

    def get_max_speed_in_kmh(self) -> int:
        return 400

    def get_max_delivery_weight_in_kg(self) -> int:
        return 500

    def prepare_vehicle(self) -> None:
        print("Prepare Helicopter.")


class VehicleFactory:

    def create_and_prepare_vehicle(self, vehicle_speed: str, vehicle_type: str) -> Vehicle:
        try:
            vehicle = self.create_vehicle(vehicle_speed, vehicle_type)
            vehicle.prepare_vehicle()
            return vehicle
        except AttributeError:
            raise AttributeError(f"Vehicle Type {vehicle_speed} not supported.")

    def create_vehicle(self, vehicle_speed: str, vehicle_type: str) -> Vehicle | None:
        if vehicle_type == "ground":
            if vehicle_speed == "fast":
                return Car()
            if vehicle_speed == "slow":
                return Truck()
        if vehicle_type == "air":
            if vehicle_speed == "fast":
                return Airplane()
            if vehicle_speed == "slow":
                return Helicopter()
        return None


def vehicle_factory() -> VehicleFactory:
    """Construct a vehicle object that allows to create a vehicle, based on the user's speed preference."""
    return VehicleFactory()


def main(factory: VehicleFactory) -> None:
    vehicle = factory.create_and_prepare_vehicle("slow", "ground")
    print(f"Vehicles max speed: {vehicle.get_max_speed_in_kmh()}")
    print(f"Vehicles max weight it can carry: {vehicle.get_max_delivery_weight_in_kg()}")


if __name__ == '__main__':
    main(vehicle_factory())
