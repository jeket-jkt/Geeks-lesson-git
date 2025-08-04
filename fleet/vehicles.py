from abc import ABC, abstractmethod

class Vehicle(ABC):
    _vehicle_count = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        Vehicle._vehicle_count += 1

    @property
    def full_name(self):
        return f"{self.brand} {self.model} ({self.year})"

    @classmethod
    def total_vehicles(cls):
        return cls._vehicle_count

    @abstractmethod
    def get_info(self):
        pass