import json
import pandas as pd

def json_to_csv(json_path, csv_path):
    try:
        with open(json_path, 'r') as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("JSON data is not a list of records")

        df = pd.DataFrame(data)
        df.to_csv(csv_path, index=False)
        print(f"CSV file created successfully at {csv_path}")
    except FileNotFoundError:
        print(f"Error: The file {json_path} was not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Interactive user input for file paths
json_file_path = input("Enter the path of your JSON file: ")
csv_file_path = input("Enter the desired path for your CSV file: ")

# Convert JSON to CSV
json_to_csv(json_file_path, csv_file_path)
