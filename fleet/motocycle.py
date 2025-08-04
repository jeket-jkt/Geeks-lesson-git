from vehicles import Vehicle

class Motocycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def get_info(self):
        return f"{self.full_name} - Sidecar: {self.has_sidecar}"