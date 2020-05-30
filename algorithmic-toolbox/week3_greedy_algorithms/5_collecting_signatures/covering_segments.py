# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    segments = sorted(segments, key=lambda s: s.end)
    points = []
    while segments:
        p = segments.pop(0).end
        while segments:
            if segments[0].start <= p:
                segments.pop(0)
            else:
                break
        points.append(p)
    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
