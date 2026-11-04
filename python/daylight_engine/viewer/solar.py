"""Solar paths at the same standard-time hourly midpoints as the EPW/WEA sky."""
from functools import lru_cache


@lru_cache(maxsize=8)
def solar_diagram(latitude: float, longitude: float, time_zone: float, north: float = 0.0) -> dict:
    """Sun positions for all 8,760 hours at a location, for drawing the sun path."""
    from ladybug.sunpath import Sunpath
    from ladybug.dt import DateTime

    path = Sunpath(latitude, longitude, time_zone, north_angle=north)
    hourly = []
    for index in range(8760):
        sun = path.calculate_sun_from_hoy(index + 0.5)
        vector = sun.sun_vector_reversed
        hourly.append([round(vector.x, 6), round(vector.y, 6), round(vector.z, 6), round(sun.altitude, 3), round(sun.azimuth, 3)])
    month_days = [int(DateTime(month, 21).hoy // 24) for month in range(1, 13)]
    monthly_paths = [[hourly[day * 24 + hour][:3] for hour in range(24) if hourly[day * 24 + hour][2] > 0] for day in month_days]
    analemmas = [[hourly[day * 24 + hour][:3] for day in range(365) if hourly[day * 24 + hour][2] > 0] for hour in [8, 10, 12, 14, 16]]
    return {"hourly": hourly, "monthly_paths": monthly_paths, "analemmas": analemmas,
            "month_timesteps": [day * 24 + 12 for day in month_days],
            "time_zone": time_zone, "latitude": latitude, "longitude": longitude,
            "time_convention": "EPW standard time, hourly midpoint"}
