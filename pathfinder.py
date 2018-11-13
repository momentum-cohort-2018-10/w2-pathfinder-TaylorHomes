# Made significant progress. Still no map. Will attempt another approach in the morning.
import random
import csv
from PIL import Image

# with open("elevation_small.txt") as elevation_file:
#     for line in elevation_file:
#         stripped_data = []
#         stripped_data.append([int(num) for num in line.strip().split()])

with open('elevation_small.txt', 'r') as file:
    stripped_data = [line.strip() for line in file.readlines()]
    cleaned_data = [line.split(' ') for line in stripped_data]
    ready_for_pixels = [[int(x) for x in line] for line in cleaned_data]

    # print(ready_for_pixels)


def find_max_elevations(data):
    max_elevation = max([max(row) for row in data])
    return max_elevation


max_elevation = find_max_elevations(ready_for_pixels)
print(max_elevation)


def find_min_elevations(data):
    min_elevation = min([min(row) for row in data])
    return min_elevation


min_elevation = find_min_elevations(ready_for_pixels)
print(max_elevation)


gradient_list = [abs[int((num - min_elevation)/(max_elevation - min_elevation) * 255)]


def draw_map(list):
    list = gradient_list
    image = Image.new("RGB", (600, 600))
    for y, row in enumerate(gradient_list):
        for x, value in enumerate(row):
            image.putpixel((x, y), (value, value, value))
    image.save('map_image.png')
    image.show('map_image.png')
