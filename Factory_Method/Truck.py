# -*- coding: utf-8 -*-
"""

File:
    Truck.py

Authors: Sören Erichsen
Date:
    05.08.21

Copyright:
    Sören Erichsen
"""

from Vehicle import Vehicle


# This is a so called CONCRETEPRODUCT
# A CONCRETEPRODUCT implements a Product (in this case Vehicle)
class Truck(Vehicle):
    def what_type_are_you(self):
        print("I am a Truck.")
        return "Truck"
