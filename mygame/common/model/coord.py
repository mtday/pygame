
from mygame.common.config.settings import BYTE_ORDER


class Coord:
    __directions = [(1, -1, 0), (1, 0, -1), (0, 1, -1), (-1, 1, 0), (-1, 0, 1), (0, -1, 1)]

    def __init__(self, x=0, y=0, z=0):
        if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
            self.x = x
            self.y = y
            self.z = z
        else:
            self.x = round(x)
            self.y = round(y)
            self.z = round(z)
            x_diff = abs(self.x - x)
            y_diff = abs(self.y - y)
            z_diff = abs(self.z - z)
            if x_diff > y_diff and x_diff > z_diff:
                self.x = -self.y - self.z
            elif y_diff > z_diff:
                self.y = -self.x - self.z
            else:
                self.z = -self.x - self.y

        if self.x + self.y + self.z != 0:
            raise Exception(f'Invalid coordinates: {self.x}, {self.y}, {self.z}')

    def distance_to(self, other):
        return max(abs(self.x - other.x),
                   abs(self.y - other.y),
                   abs(self.z - other.z))

    def add(self, x=0, y=0, z=0):
        if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
            new_x = self.x + x
            new_y = self.y + y
            new_z = self.z + z
        else:
            new_x = self.x + round(x)
            new_y = self.y + round(y)
            new_z = self.z + round(z)
            x_diff = abs(new_x - x)
            y_diff = abs(new_y - y)
            z_diff = abs(new_z - z)
            if x_diff > y_diff and x_diff > z_diff:
                new_x = -new_y - new_z
            elif y_diff > z_diff:
                new_y = -new_x - new_z
            else:
                new_z = -new_x - new_y
        return Coord(new_x, new_y, new_z)

    def add_coord(self, coord):
        return self.add(coord.x, coord.y, coord.z)

    def subtract(self, x=0, y=0, z=0):
        return self.add(-x, -y, -z)

    def subtract_coord(self, coord):
        return self.subtract(coord.x, coord.y, coord.z)

    def get_neighbor(self, i):
        (x, y, z) = Coord.__directions[i]
        return self.add(x, y, z)

    def get_neighbors(self):
        return [self.get_neighbor(i) for i in range(6)]

    def get_ring(self, distance):
        results = []
        direction = Coord.__directions[4]
        coord = self.add_coord(Coord(direction[0] * distance, direction[1] * distance, direction[2] * distance))
        for i in range(6):
            for j in range(distance):
                results.append(coord)
                coord = coord.get_neighbor(i)
        return results

    def write(self, iostream):
        iostream.write(int(self.x).to_bytes(4, byteorder=BYTE_ORDER, signed=True))
        iostream.write(int(self.z).to_bytes(4, byteorder=BYTE_ORDER, signed=True))

    @staticmethod
    def read(iostream):
        x = int.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=True)
        z = int.from_bytes(iostream.read(1), byteorder=BYTE_ORDER, signed=True)
        return Coord(x, -x - z, z)
