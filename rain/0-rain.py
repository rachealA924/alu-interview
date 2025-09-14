#!/usr/bin/python3
"""calculate how many square units of water will be retained after it rains"""


def rain(walls):
    """Rain"""
    if not walls:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = walls[0]
    i = 1
    while i < n:
        if left_max[i - 1] > walls[i]:
            left_max[i] = left_max[i - 1]
        else:
            left_max[i] = walls[i]
        i += 1

    # Fill right_max with while loop
    right_max[n - 1] = walls[n - 1]
    i = n - 2
    while i >= 0:
        if right_max[i + 1] > walls[i]:
            right_max[i] = right_max[i + 1]
        else:
            right_max[i] = walls[i]
        i -= 1

    # Calculate trapped water
    total_water = 0
    i = 0
    while i < n:
        if left_max[i] < right_max[i]:
            water_level = left_max[i]
        else:
            water_level = right_max[i]

        total_water += water_level - walls[i]
        i += 1

    return total_water
