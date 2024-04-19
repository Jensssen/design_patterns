class Car:
    """Regular Car Vehicle."""

    def get_max_speed_in_kmh(self) -> int:
        return 220

    def get_max_delivery_weight_in_kg(self) -> int:
        return 100

    def prepare_vehicle(self) -> None:
        print("Prepare Car.")


class Truck:
    """Regular Truck Vehicle."""

    def get_max_speed_in_kmh(self) -> int:
        return 120

    def get_max_delivery_weight_in_kg(self) -> int:
        return 1000

    def prepare_vehicle(self) -> None:
        print("Prepare Truck.")


def create_vehicle(vehicle_speed: str) -> Car | Truck:
    """Returns a new Vehicle depending on user selection."""
    if vehicle_speed == "fast":
        return Car()
    if vehicle_speed == "slow":
        return Truck()


def main(vehicle: Car | Truck) -> None:
    vehicle.prepare_vehicle()
    print(f"Vehicles max speed: {vehicle.get_max_speed_in_kmh()}")
    print(f"Vehicles max weight it can carry: {vehicle.get_max_delivery_weight_in_kg()}")


if __name__ == '__main__':
    main(create_vehicle("slow"))
