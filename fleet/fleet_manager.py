from database import get_connection

class FleetManager:
    def add_vehicle(self, vehicle):
        conn = get_connection()
        cursor = conn.cursor()
        if hasattr(vehicle, 'seats'):
            cursor.execute('''
                INSERT INTO vehicles (type, brand, model, year, seats)
                VALUES (?, ?, ?, ?, ?)
            ''', ('car', vehicle.brand, vehicle.model, vehicle.year, vehicle.seats))
        elif hasattr(vehicle, 'has_sidecar'):
            cursor.execute('''
                INSERT INTO vehicles (type, brand, model, year, has_sidecar)
                VALUES (?, ?, ?, ?, ?)
            ''', ('motorcycle', vehicle.brand, vehicle.model, vehicle.year, vehicle.has_sidecar))
        conn.commit()
        conn.close()

    def remove_vehicle(self, brand):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM vehicles WHERE brand = ?", (brand,))
        conn.commit()
        conn.close()

    def update_vehicle(self, brand, new_model):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE vehicles SET model = ? WHERE brand = ?", (new_model, brand))
        conn.commit()
        conn.close()

    def list_vehicles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM vehicles")
        for row in cursor.fetchall():
            print(row)
        conn.close()

    def find_vehicle(self, keyword):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM vehicles WHERE brand LIKE ? OR model LIKE ?", (f'%{keyword}%', f'%{keyword}%'))
        for row in cursor.fetchall():
            print(row)
        conn.close()

    def close(self):
        pass