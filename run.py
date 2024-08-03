import argparse


from utils import read_file

def main(file_path):
    try:
        input_file = read_file(file_path=file_path)
        print(input_file.head())
    except Exception as e:
        print(f"Error ocurred while reading file: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=str, help="Path to text file.")
    args = parser.parse_args()
    
    main(args.file_path)
