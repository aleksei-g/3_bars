import json
from math import pi, sqrt, sin, cos, atan2


def load_data(filepath):
    with open(filepath, 'r') as f:
        data = json.loads(f.read())
    return data


def get_biggest_bar(data):
    SeatsCount_max = sorted(data, key=lambda d: d['Cells']['SeatsCount'],
                            reverse=True)[0]['Cells']['SeatsCount']
    bars_with_SeatsCount_max = [bar['Cells']['Name'] for bar in data
                                if bar['Cells']['SeatsCount'] ==
                                SeatsCount_max]
    return bars_with_SeatsCount_max


def get_smallest_bar(data):
    SeatsCount_min = sorted(data, key=lambda d:
                            d['Cells']['SeatsCount'])[0]['Cells']['SeatsCount']
    bars_with_SeatsCount_min = [bar['Cells']['Name'] for bar in data
                                if bar['Cells']['SeatsCount'] ==
                                SeatsCount_min]
    return bars_with_SeatsCount_min


def get_distance(pos1, pos2):
    lat1 = float(pos1['lat'])
    long1 = float(pos1['long'])
    lat2 = float(pos2['lat'])
    long2 = float(pos2['long'])
    degree_to_rad = float(pi / 180.0)
    d_lat = (lat2 - lat1) * degree_to_rad
    d_long = (long2 - long1) * degree_to_rad
    a = pow(sin(d_lat / 2), 2) + cos(lat1 * degree_to_rad) * \
        cos(lat2 * degree_to_rad) * pow(sin(d_long / 2), 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    km = 6367 * c
    return km


def get_closest_bar(data, longitude, latitude):
    distance = [{'name': bar['Cells']['Name'], 'distance':get_distance(
            {'long': longitude, 'lat': latitude},
            {'long': bar['Cells']['geoData']['coordinates'][0],
                'lat': bar['Cells']['geoData']['coordinates'][1]})}
            for bar in data]
    return sorted(distance, key=lambda d: d['distance'])[0]['name']


if __name__ == '__main__':
    while True:
        try:
            longitude = float(input(
                'Enter longitude (default: 37.621099): ') or '37.621099')
            break
        except:
            print('Incorrect value!')
    while True:
        try:
            latitude = float(input(
                'Enter latitude (default: 55.753525): ') or '55.753525')
            break
        except:
            print('Incorrect value!')
    data = load_data('bar.json')
    biggest_bar = get_biggest_bar(data)
    smallest_bar = get_smallest_bar(data)
    closest_bar = get_closest_bar(data, longitude, latitude)
    print('Biggest bars: %s' % biggest_bar)
    print('Smallest_bars: %s' % smallest_bar)
    print('Closest_bar: %s' % closest_bar)
