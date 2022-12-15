import math as Math

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def add(self, x, y):
        return Point(self.x + x, self.y + y)

    def euclid(self, other):
        x_diff = self.x - other.x
        y_diff = self.y - other.y
        return int(Math.sqrt(x_diff * x_diff + y_diff * y_diff))

    def manhattan(self, other):
        x_diff = self.x - other.x
        y_diff = self.y - other.y
        return abs(x_diff) + abs(y_diff)

def main():
    # target_line_num = 10
    dims = 4000000
    line_start = 0
    # target_line = dict()
    grid = [[] for x in range(0, dims)]
    sensors = []
    beacons = []
    with open("15input.txt", encoding='UTF-8') as file:
        for line in file:
            parts = line.strip().split(' ')
            sensor_x = int(parts[2].split('=')[1].split(',')[0])
            sensor_y = int(parts[3].split('=')[1].split(':')[0])
            beacon_x = int(parts[8].split('=')[1].split(',')[0])
            beacon_y = int(parts[9].split('=')[1].split(':')[0])

            sensor = Point(sensor_x, sensor_y)
            sensors.append(sensor)

            beacon = Point(beacon_x, beacon_y)
            beacons.append(beacon)

    for target_line_num in range(0, dims):
        ranges = []
        for s, sensor in enumerate(sensors):
            beacon = beacons[s]
            dist = sensor.manhattan(beacon)
            width = (dist - abs(sensor.y - target_line_num)) * 2 + 1
            if sensor.y == 0:
                pass

            if width > 0:
                lower_x = int(sensor.x - (width - 1)/2)
                upper_x = int(sensor.x + (width - 1)/2)
                ranges.append((max(lower_x, 0), min(upper_x, dims)))
            if sensor.x == target_line_num:
                ranges.append((sensor.x, sensor.x))
        for beacon in beacons:
            if beacon.x == target_line_num:
                ranges.append((beacon.x, beacon.x))
        key_func = lambda x: x[0] * dims + x[1]
        ranges.sort(key=key_func);
        right = ranges[0][1]
        for r, ran in enumerate(ranges[1:], 1):
            if right < ran[0] - 1:
                x = right + 1
                y = target_line_num
                print(x * 4000000 + y)
                break
            else:
                right = max(right, ran[1])
    raise Exception('asd')

if __name__ == "__main__":
    main()
