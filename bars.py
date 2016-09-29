import json
import os.path
import argparse
import sys
from math import pi, sqrt, sin, cos, atan2


CONVERT_TO_KM = 6367
STRAIGHT_ANGLE = 180


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    else:
        return None


def get_biggest_bar(data):
    SeatsCount_max = sorted(data, key=lambda d: d['Cells']['SeatsCount'],
                            reverse=True)[0]['Cells']['SeatsCount']
    biggest_bar = [bar['Cells']['Name'] for bar in data
                   if bar['Cells']['SeatsCount'] == SeatsCount_max]
    return biggest_bar


def get_smallest_bar(data):
    SeatsCount_min = sorted(data, key=lambda d:
                            d['Cells']['SeatsCount'])[0]['Cells']['SeatsCount']
    smallest_bar = [bar['Cells']['Name'] for bar in data
                    if bar['Cells']['SeatsCount'] == SeatsCount_min]
    return smallest_bar


def get_distance(pos1, pos2):
    lat1 = float(pos1['lat'])
    long1 = float(pos1['long'])
    lat2 = float(pos2['lat'])
    long2 = float(pos2['long'])
    degree_to_rad = float(pi / STRAIGHT_ANGLE)
    d_lat = (lat2 - lat1) * degree_to_rad
    d_long = (long2 - long1) * degree_to_rad
    dist = pow(sin(d_lat / 2), 2) + cos(lat1 * degree_to_rad) * \
        cos(lat2 * degree_to_rad) * pow(sin(d_long / 2), 2)
    lin_dist = 2 * atan2(sqrt(dist), sqrt(1 - dist))
    km = CONVERT_TO_KM * lin_dist
    return km


def get_closest_bar(data, longitude, latitude):
    distance = [{'name': bar['Cells']['Name'], 'distance':get_distance(
            {'long': longitude, 'lat': latitude},
            {'long': bar['Cells']['geoData']['coordinates'][0],
                'lat': bar['Cells']['geoData']['coordinates'][1]})}
            for bar in data]
    return sorted(distance, key=lambda d: d['distance'])[0]['name']


def createParser():
    parser = argparse.ArgumentParser(description='Программа для поиска самого \
                                     большого, самого маленького и \
                                     самого близкого бара Москвы.')
    parser.add_argument('-f', '--file', required=True, metavar='ФАЙЛ',
                        help='Путь до файла в формате json.')
    parser.add_argument('-c', '--coordinates', nargs=2, type=float,
                        metavar='КООРДИНАТЫ',
                        help='Координаты: долгота и широта (через пробел).')
    parser.add_argument('-s', '--smallest', action='store_true',
                        default=False, help='Вывести самый маленький бар.')
    parser.add_argument('-b', '--biggest', action='store_true',
                        default=False, help='Вывести самый большой бар.')
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
    data = load_data(namespace.file)
    if not data:
        print('Путь до файла указан неверно!')
        sys.exit()
    if namespace.biggest:
        print('Самый большой бар: %s' % get_biggest_bar(data))
    if namespace.smallest:
        print('Самцй маленький бар: %s' % get_smallest_bar(data))
    if namespace.coordinates:
        print('Ближайший бар: %s' % get_closest_bar(data,
              namespace.coordinates[0], namespace.coordinates[1]))
