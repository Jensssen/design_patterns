from abc import ABC, abstractmethod


class GroundVehicle(ABC):

    @abstractmethod
    def get_max_speed_in_kmh(self) -> int:
        """Get maximum speed of vehicle in km/h."""

    @abstractmethod
    def get_max_delivery_weight_in_kg(self) -> int:
        """Get max weight, the vehicle can carry."""

    @abstractmethod
    def prepare_vehicle(self) -> None:
        """Prepare vehicle"""


class Car(GroundVehicle):
    """Regular Car Vehicle."""

    def get_max_speed_in_kmh(self) -> int:
        return 220

    def get_max_delivery_weight_in_kg(self) -> int:
        return 100

    def prepare_vehicle(self) -> None:
        print("Prepare Car.")


class Truck(GroundVehicle):
    """Regular Truck Vehicle."""

    def get_max_speed_in_kmh(self) -> int:
        return 120

    def get_max_delivery_weight_in_kg(self) -> int:
        return 1000

    def prepare_vehicle(self) -> None:
        print("Prepare Truck.")


class AirVehicle(ABC):

    @abstractmethod
    def get_max_speed_in_kmh(self) -> int:
        """Get maximum speed of vehicle in km/h."""

    @abstractmethod
    def get_max_delivery_weight_in_kg(self) -> int:
        """Get max weight, the vehicle can carry."""

    @abstractmethod
    def prepare_vehicle(self) -> None:
        """Prepare vehicle"""


class Airplane(AirVehicle):
    """Regular Airplane Vehicle."""

    def get_max_speed_in_kmh(self) -> int:
        return 800

    def get_max_delivery_weight_in_kg(self) -> int:
        return 5000

    def prepare_vehicle(self) -> None:
        print("Prepare Airplane.")


class Helicopter(AirVehicle):
    """Regular Helicopter Vehicle."""

    def get_max_speed_in_kmh(self) -> int:
        return 400

    def get_max_delivery_weight_in_kg(self) -> int:
        return 500

    def prepare_vehicle(self) -> None:
        print("Prepare Helicopter.")


class VehicleFactory(ABC):

    @abstractmethod
    def create_fast_vehicle(self) -> GroundVehicle:
        """Get ground vehicle for use."""

    @abstractmethod
    def create_slow_vehicle(self) -> AirVehicle:
        """Get air vehicle for use."""


class GroundVehicleFactory(VehicleFactory):
    def create_fast_vehicle(self) -> GroundVehicle:
        return Car()

    def create_slow_vehicle(self) -> GroundVehicle:
        return Truck()


class AirVehicleFactory(VehicleFactory):
    def create_fast_vehicle(self) -> AirVehicle:
        return Airplane()

    def create_slow_vehicle(self) -> AirVehicle:
        return Helicopter()


def create_factory() -> VehicleFactory:
    factories = {
        "ground": GroundVehicleFactory(),
        "air": AirVehicleFactory()
    }
    while True:
        transport_mode = input("Enter desired mode of transport (ground or air): ")
        if transport_mode in factories:
            return factories[transport_mode]
        print(f"Unknown type of transport option: {transport_mode}.")


def main(vehicle_factory: VehicleFactory) -> None:
    fast_vehicle = vehicle_factory.create_fast_vehicle()
    slow_vehicle = vehicle_factory.create_slow_vehicle()

    fast_vehicle.prepare_vehicle()

    print(f"Fast vehicles max speed: {fast_vehicle.get_max_speed_in_kmh()}")
    print(f"Fast Vehicles max weight it can carry: {fast_vehicle.get_max_delivery_weight_in_kg()}")

    slow_vehicle.prepare_vehicle()
    print(f"Slow vehicles max speed: {slow_vehicle.get_max_speed_in_kmh()}")
    print(f"Slow Vehicles max weight it can carry: {slow_vehicle.get_max_delivery_weight_in_kg()}")


if __name__ == '__main__':
    factory = create_factory()
    main(factory)
