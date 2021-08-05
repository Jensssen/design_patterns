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

from Car import Car
from Truck import Truck
from Vehicle import Vehicle
from Vehicle_Factory import VehicleFactory


# This is the so called CONCRETECREATOR
class ImplicitVehicleFactory(VehicleFactory):

    def __init__(self, type:str):
        self.type = type

    def create_vehicle(self) -> Vehicle:
        if self.type == "car":
            return Car("blue", 110)
        if self.type == "truck":
            return Truck("green", 55)
