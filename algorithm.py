import pandas as pd

def get_routes(df:pd.DataFrame):
    """
    - Greedy search based algorithm.
    
    - Adaptation of original problem to the Salesman Problem. 
    - Each load is considered a node.
    - Distance between nodes = distance(previous dropoff, next node pickup) +
                            distance(next node pickup, next node dropoff) +
                            distance(next node dropoff, depot)
    
    - Next node is choosen by the min distance from initial node.
    - If this distance can be covered with remaining truck distance capacity, the driver
    is assigned the route. 
    - Truck distance capacity is 720, and is provided in problem definition

    df: DataFrame distance matrix of load route.
    Returns: List[dict] with planning route and remaining truck capacity

    """
    remaining_routes = [i for i in range(1,df.shape[0])]
    routes = []
    depot_index = 0
    while len(remaining_routes)!=0:
        # Initialize route for each truck. Trucks always start from depot and return to depot.
        truck_time_capacity_remaining = 12*60
        truck_log = {'route':[], 'usage':truck_time_capacity_remaining}
        current_route = depot_index

        while truck_time_capacity_remaining >= 0 and len(remaining_routes)!=0:
            next_route = min(remaining_routes, key=lambda x: df.loc[current_route, x])
            next_route_distance = df.loc[current_route,next_route]
            truck_time_capacity_remaining -= next_route_distance
            if truck_time_capacity_remaining >= 0:
                truck_log['route'].append(next_route)
                truck_log['usage'] = truck_time_capacity_remaining
                remaining_routes.remove(next_route)
                current_route = next_route
            else:
                # Start a new truck route.
                continue
        routes.append(truck_log)
    
    return routes
