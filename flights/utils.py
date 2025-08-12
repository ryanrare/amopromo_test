from math import radians, sin, cos, sqrt, atan2
from datetime import datetime


def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


def calculate_meta(flight, origin_airport, destination_airport):
    range_km = haversine(origin_airport.latitude, origin_airport.longitude, destination_airport.latitude,
                         destination_airport.longitude)

    fmt = "%Y-%m-%dT%H:%M:%S"
    dep = datetime.strptime(flight["departure_time"], fmt)
    arr = datetime.strptime(flight["arrival_time"], fmt)
    duration_hours = (arr - dep).total_seconds() / 3600

    cruise_speed = range_km / duration_hours if duration_hours else 0
    cost_per_km = flight['price']['fare'] / range_km if range_km else 0

    return {
        "range": round(range_km),
        "cruise_speed_kmh": round(cruise_speed),
        "cost_per_km": round(cost_per_km, 2)
    }


def calculate_price(fare):
    fee = max(fare * 0.1, 40.0)
    total = fare + fee
    return {
        "fare": round(fare, 2),
        "fee": round(fee, 2),
        "total": round(total, 2)
    }
