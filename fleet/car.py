from vehicles import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, year, seats):
        super().__init__(brand, model, year)
        self.seats = seats

    def get_info(self):
        return f"{self.full_name} - {self.seats} seats"