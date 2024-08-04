import argparse
from utils import read_file, format_input_file, build_distance_matrix 
from algorithm import get_routes

def main(file_path):
    try:
        input_file = read_file(file_path=file_path)
        cleaned_file = format_input_file(input_file)
        distance_matrix_df = build_distance_matrix(cleaned_file)

        routing_plan = get_routes(distance_matrix_df)
        for i in routing_plan:
            print(i['route'])

    except Exception as e:
        print(f"Error ocurred while processing file {file_path}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=str, help="Path to text file.")
    args = parser.parse_args()
    
    main(args.file_path)
