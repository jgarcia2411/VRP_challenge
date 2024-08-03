import pandas as pd
import numpy as np


def read_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()[1:]
    data = []
    for line in lines:
        line = line.replace('\n', '')
        container = {'pickup': line.split(' ')[1], 'dropoff': line.split(' ')[2]}
        data.append(container)

    df = pd.DataFrame(data)

    return df

def format_input_file(df:pd.DataFrame):
   df['pickup'] = df['pickup'].apply(lambda x: np.array([float(i) for i in x.strip().replace('(', '').replace(')', '').split(',')]))
   df['dropoff'] = df['dropoff'].apply(lambda x: np.array([float(i) for i in x.strip().replace('(', '').replace(')', '').split(',')]))
   
   return df

def euclidean_distance(p1:np.array, p2:np.array):
    return np.linalg.norm(p1 - p2)

def get_distances_input_file(df:pd.DataFrame):
    df['distance'] = df.apply(lambda x: euclidean_distance(x['pickup'], x['dropoff']), axis=1)
    return df

