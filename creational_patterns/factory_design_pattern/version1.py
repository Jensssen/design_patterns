class Car:
    def get_max_speed_in_kmh(self) -> int:
        return 220

    def get_max_delivery_weight_in_kg(self) -> int:
        return 100

    def prepare_vehicle(self) -> None:
        print("Prepare Car.")


def create_vehicle() -> Car:
    """Returns a new Vehicle."""
    return Car()


def main(vehicle: Car) -> None:
    vehicle.prepare_vehicle()
    print(f"Vehicles max speed: {vehicle.get_max_speed_in_kmh()}")
    print(f"Vehicles max weight it can carry: {vehicle.get_max_delivery_weight_in_kg()}")


if __name__ == '__main__':
    main(create_vehicle())
