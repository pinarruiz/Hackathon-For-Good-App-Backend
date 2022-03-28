import csv
from geopy import distance

from .query_models import Coordinates

def get_distance(origin: Coordinates, target: Coordinates):
    return distance.distance(origin.to_list(), target.to_list()).meters

def read_csv(file_name: str = "dataset_contendores.csv"):
    print(f"INFO:     Reading Locations...")
    container_type_locations = {}
    with open(file_name, 'r')as file:
        filecontent = csv.reader(file)
        for i, data in enumerate(filecontent):
            if i != 0:
                if not int(data[1]) in container_type_locations:
                    container_type_locations[int(data[1])] = []
                container_type_locations[int(data[1])].append(Coordinates(latitude = float(data[11]), longitude = float(data[10])))
    print(f"INFO:     Locations readed")
    return container_type_locations