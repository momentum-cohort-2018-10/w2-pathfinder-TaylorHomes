# I've written perhaps a hundred other lines of non-sensical code. But this is currently all I have that works. Will continue and make another commit this afternoon.


import random
import csv
from PIL import Image


with open("elevation_small.txt") as elevation_file:
    for line in elevation_file:
        stripped_data = []
        stripped_data.append([int(num) for num in line.strip().split()])


def find_max_elevation(data):
    max_elevation = max([max(row) for row in data])
    return max_elevation


def find_min_elevation(data):
    min_elevation = min([min(row) for row in data])
    return min_elevation
