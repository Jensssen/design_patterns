# -*- coding: utf-8 -*-
"""

File:
    Random_Vehicle_Factory.py

Authors: Sören Erichsen
Date:
    05.08.21

Copyright:
    Sören Erichsen
"""

import random

from Car import Car
from Truck import Truck
from Vehicle import Vehicle
from Vehicle_Factory import VehicleFactory


# This is the so called CONCRETECREATOR
class RandomVehicleFactory(VehicleFactory):

    def create_vehicle(self) -> Vehicle:
        if random.uniform(0, 1) > 0.5:
            return Car("blue", 110)
        else:
            return Truck("green", 55)
