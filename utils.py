import pandas as pd
import numpy as np

DEPOT_COORDINATES = "(0.0,0.0)"
DEPOT_ARRAY = np.array([float(i) for i in DEPOT_COORDINATES.strip().replace('(', '').replace(')', '').split(',')])

def read_file(file_path:str)->pd.DataFrame:
    """
    Reads input file path .txt and output DataFrame with coordinates as string.
    file_path: path to input file.

    Returns: pd.DataFrame with "pickup" and "dropoff" column names.
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()[1:]
    data = [{"pickup":DEPOT_COORDINATES, "dropoff":DEPOT_COORDINATES}]
    for line in lines:
        line = line.replace('\n', '')
        container = {'pickup': line.split(' ')[1], 'dropoff': line.split(' ')[2]}
        data.append(container)

    df = pd.DataFrame(data)
    return df

def format_input_file(df:pd.DataFrame)->pd.DataFrame:
   """
   String coordinates are transformed to Numpy array.
   df: DataFrame with "pickup" and "dropoff" column name.
   Returns: pd.DataFrame with "pickup" and "dropoff" coordinates as Numpy array.
   """
   df['pickup'] = df['pickup'].apply(lambda x: np.array([float(i) for i in x.strip().replace('(', '').replace(')', '').split(',')]))
   df['dropoff'] = df['dropoff'].apply(lambda x: np.array([float(i) for i in x.strip().replace('(', '').replace(')', '').split(',')]))
   
   return df

def euclidean_distance(p1:np.array, p2:np.array)->float:
    """
    p1: initial coordinate, np.array
    p2: final coordinate, np.array
    Returns: euclidean distance between two vectors
    """
    return np.linalg.norm(p1 - p2)

def build_distance_matrix(df:pd.DataFrame)->pd.DataFrame:
    """
    Calcuates distances between route A ---> route B, including returning distance to depot.

    total distance between two routes = distance(previous dropoff, route A pickup)
                                        + distance(route A pickup, route A dropoff) 
                                        + distance(route A dropoff, depot)
    df: DataFrame with "pickup" and "dropoff" coordinates
    Returns: pd.DataFrame distance matrix
    """
    
    total_routes = df.shape[0]
    distance_matrix = np.zeros((total_routes,total_routes))

    for i in range(total_routes):
        for j in range(total_routes):
            distance_between_two_routes = (
                euclidean_distance(df.loc[i,'dropoff'], df.loc[j,'pickup']) + 
                euclidean_distance(df.loc[j,'pickup'], df.loc[j,'dropoff']) +
                euclidean_distance(df.loc[j,'dropoff'], DEPOT_ARRAY)
            )
            distance_matrix[i,j] = distance_between_two_routes
    
    df_index  = [i for i in range(total_routes)]
    distance_df = pd.DataFrame(distance_matrix, index=df_index, columns=df_index)


    return distance_df




    