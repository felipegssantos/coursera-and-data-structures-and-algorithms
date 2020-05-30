# python3
import sys


def compute_min_refills(distance, tank, stops):
    refills = 0
    position = 0
    while distance - position > tank:
        if position + tank >= distance:
            break
        try:
            next_stop = max(stop for stop in stops if position + tank >= stop)
        except ValueError:
            refills = -1
            break
        else:
            refills += 1
            position, *stops = stops[stops.index(next_stop):]
    return refills


def stress_test():
    def compute_min_refills_alt(distance, tank, stops):
        refills = 0
        current_refill = 0
        x = [0] + stops + [distance]
        n = len(stops)
        while current_refill <= n:
            last_refill = current_refill
            while (current_refill <= n) and (x[current_refill+1] - x[last_refill] <= tank):
                current_refill = current_refill + 1
            if current_refill == last_refill:
                return -1
            if current_refill <= n:
                refills = refills + 1
        return refills

    import random
    while True:
        distance = random.random()
        tank = random.random()
        n = random.randint(0, 20)
        stops = sorted(random.random() for _ in range(n))
        y = compute_min_refills(distance, tank, stops)
        y_alt = compute_min_refills_alt(distance, tank, stops)
        if y == y_alt:
            print('OK!', y)
        else:
            print('Error!')
            print(distance, tank, stops, y, y_alt)
            break


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
