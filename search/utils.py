import math

EARTH_RADIUS = 6371000.0
MIN_LNG = - math.pi
MAX_LNG = math.pi
MIN_LAT = - math.pi / 2
MAX_LAT = math.pi / 2

""" Geospatial functions. We could use simple models
    for calculation when distance is small. Those functions are however tested
    in javascript.
    Write unittest before touching them!

"""
def to_rad(dec_degrees):
    return dec_degrees * math.pi / 180.0


def to_decgrees(radians):
    return (180.0 * radians) / math.pi


def get_bbox(lng, lat, radius):
    rad_dist = radius / EARTH_RADIUS

    rad_lat = to_rad(lat)
    rad_lng = to_rad(lng)

    min_lat = rad_lat - rad_dist
    max_lat = rad_lat + rad_dist

    if min_lat > MIN_LAT and max_lat < MAX_LAT:
        delta_lng = math.asin(math.sin(rad_dist) / math.cos(rad_lat))
        min_lng = rad_lng - delta_lng
        if min_lng < MIN_LNG:
            min_lng += 2 * math.pi

        max_lng = rad_lng + delta_lng
        if max_lng > MAX_LNG:
            max_lng -= 2 * math.pi
    else:
        min_lat = max(min_lat, MIN_LAT)
        max_lat = min(max_lat, MAX_LAT)
        min_lng = MIN_LNG
        max_lng = MAX_LNG

    return to_decgrees(min_lat), to_decgrees(min_lng), to_decgrees(max_lat), to_decgrees(max_lng)


def get_distance(lng1, lat1, lng2, lat2):
    delta_lat = to_rad(lat2 - lat1)
    delta_lng = to_rad(lng2 - lng1)
    a = math.sin(delta_lat / 2) * math.sin(delta_lat / 2) + math.sin(delta_lng / 2) * \
        math.sin(delta_lng / 2) * math.cos(to_rad(lat1)) * math.cos(to_rad(lat2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return c * EARTH_RADIUS
