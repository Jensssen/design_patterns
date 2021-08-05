# -*- coding: utf-8 -*-
"""

File:
    Vehicle_Factory.py

Authors: Sören Erichsen
Date:
    05.08.21

Copyright:
    Sören Erichsen
"""
import random
from abc import ABC, abstractmethod

from Car import Car
from Truck import Truck
from Vehicle import Vehicle


# This is the so called CREATOR
class VehicleFactory(ABC):

    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass


