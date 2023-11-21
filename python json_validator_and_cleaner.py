import json

def validate_json(json_path):
    """
    Validates the JSON file format.
    """
    try:
        with open(json_path, 'r') as file:
            data = json.load(file)
        print("JSON file is valid.")
        return data
    except json.JSONDecodeError as e:
        print(f"Invalid JSON file: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def clean_json_data(data, fields_to_remove):
    """
    Cleans the JSON data by removing specified fields.
    """
    if not data:
        return None

    cleaned_data = []
    for record in data:
        cleaned_record = {k: v for k, v in record.items() if k not in fields_to_remove and v is not None}
        cleaned_data.append(cleaned_record)
    
    return cleaned_data

# User input for JSON file path
json_file_path = input("Enter the path of your JSON file: ")

# Validate JSON file
data = validate_json(json_file_path)

if data:
    # Specify fields to remove (can be modified)
    fields_to_remove = ['unwantedField1', 'unwantedField2']

    # Clean JSON data
    cleaned_data = clean_json_data(data, fields_to_remove)

    if cleaned_data:
        # Optional: Save the cleaned data back to a JSON file
        cleaned_json_path = json_file_path.replace('.json', '_cleaned.json')
        with open(cleaned_json_path, 'w') as file:
            json.dump(cleaned_data, file, indent=4)

        print(f"Cleaned JSON file saved to {cleaned_json_path}")
