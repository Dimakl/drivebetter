import math

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points on the Earth specified in decimal degrees.
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371  # Radius of Earth in kilometers
    return c * r

def find_nearest_node(graph, lat, lon):
    """
    Find the nearest node in the graph to the given latitude and longitude.
    """
    min_distance = float('inf')
    nearest_node = None

    for vertex in graph.vs:
        node_lat = vertex['lat']
        node_lon = vertex['lon']
        distance = haversine_distance(lat, lon, node_lat, node_lon)
        if distance < min_distance:
            min_distance = distance
            nearest_node = vertex.index

    return nearest_node
