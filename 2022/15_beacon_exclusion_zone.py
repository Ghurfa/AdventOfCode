import math as Math

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def manhattan(self, other):
        x_diff = self.x - other.x
        y_diff = self.y - other.y
        return abs(x_diff) + abs(y_diff)

def main():
    # target_line_num = 10
    dims = 4000000
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

    y = 0
    sensor_dists = [sensor.manhattan(beacons[s]) for s, sensor in enumerate(sensors)]
    while y <= dims:
        ranges = []
        for s, sensor in enumerate(sensors):
            dist = sensor_dists[s]
            width = (dist - abs(sensor.y - y)) * 2 + 1

            if width > 0:
                lower_x = int(sensor.x - (width - 1)/2)
                upper_x = int(sensor.x + (width - 1)/2)
                ranges.append((lower_x, upper_x))
            if sensor.x == y:
                ranges.append((sensor.x, sensor.x))
        for beacon in beacons:
            if beacon.x == y:
                ranges.append((beacon.x, beacon.x))
        ranges.sort(key=lambda x: x[0] * dims + x[1])
        right = -1

        ranges.insert(0, (-1, -1))

        min_overlap = dims
        for ran in ranges[1:]:
            if right < (ran[0] - 1):
                x = right + 1
                print(x * 4000000 + y)
                break
            overlap = right - ran[0] + 1
            min_overlap = min(min_overlap, overlap)
            right = max(right, ran[1])
        y += int(Math.floor(min_overlap/2)) + 1
    print('done')

if __name__ == "__main__":
    main()
