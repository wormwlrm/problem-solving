import sys
import math

input = sys.stdin.readline

T = int(input())


def get_distance(point1, point2):
    return math.sqrt((point2[1] - point1[1]) ** 2 + (point2[0] - point1[0]) ** 2)


for _ in range(T):
    start_x, start_y, end_x, end_y = map(int, input().split())

    start = (start_x, start_y)
    end = (end_x, end_y)

    planet_count = int(input())

    planets = []

    count = 0

    for _ in range(planet_count):
        planet_x, planet_y, planet_r = map(int, input().split())
        planet_center = (planet_x, planet_y)

        distance_from_start = get_distance(planet_center, start)
        distance_from_end = get_distance(planet_center, end)

        if (distance_from_start < planet_r and distance_from_end > planet_r) or (
            distance_from_start > planet_r and distance_from_end < planet_r
        ):
            count += 1

    print(count)
