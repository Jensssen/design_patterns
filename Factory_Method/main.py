# -*- coding: utf-8 -*-
"""

File:
    main.py

Authors: Sören Erichsen
Date:
    05.08.21

Copyright:
    Sören Erichsen
"""

from Implicit_Vehicle_Factory import ImplicitVehicleFactory
from Random_Vehicle_Factory import RandomVehicleFactory
from Vehicle_Factory import VehicleFactory


def client_code(vehicle_factory: VehicleFactory) -> None:
    vehicle = vehicle_factory.create_vehicle()
    vehicle.what_type_are_you()
    vehicle.print_top_speed()


if __name__ == "__main__":
    client_code(RandomVehicleFactory())
    print("\n")
    client_code(ImplicitVehicleFactory("car"))
