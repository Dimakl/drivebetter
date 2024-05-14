# FILE_PATH = str(pathlib.Path().parent.resolve())
import pyrosm
import geopandas as gpd

# Function to calculate distance between a point and a line
def point_to_line_dist(point, line):
    try:
        return point.distance(line)
    except Exception as e:
        print(f"Error calculating distance: {e}")
        return float('inf')

def get_clean_nodes_edges(path):
    osm = pyrosm.OSM(path)
    nodes, edges = osm.get_network(nodes=True, network_type="driving")
    edges = edges[['maxspeed', 'id', 'geometry', 'u', 'v', 'length', 'oneway']] #maybe surface and smoothness would be added
    nodes = nodes[['lat', 'lon', 'id', 'geometry']]
    return nodes, edges

# 'C:/Users/Xiaomi/Downloads/respublika-krym.geojson'
def get_accidents(path):
    accidents = gpd.read_file(path)
    return accidents


def to_graph(nodes, edges):
    G = osm.to_graph(nodes, edges)
    return G