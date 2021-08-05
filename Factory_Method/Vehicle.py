# -*- coding: utf-8 -*-
"""

File:
    Vehicle.py

Authors: Sören Erichsen
Date:
    05.08.21

Copyright:
    Sören Erichsen
"""
from abc import ABC, abstractmethod


# This is the so called PRODUCT
class Vehicle(ABC):

    def __init__(self, color: str, top_speed: int):
        self.color = color
        self.top_speed = top_speed

    def print_top_speed(self):
        print(f"My top speed is {self.top_speed}.")

    @abstractmethod
    def what_type_are_you(self):
        pass