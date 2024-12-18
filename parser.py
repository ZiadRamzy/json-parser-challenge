import json
import sys
from typing import Any, NoReturn


def validate_json(file_path: str) -> NoReturn:
    """
    Validates a JSON file containing a JSON object with various value types,
    including nested objects and arrays.

    Args:
        - file_path (str): Path to the JSON file to validate.
    
    Output:
        - Prints "Valid JSON object with string keys and values" and exits with code 0 if the JSON is valid.
        - Prints "Invalid JSON: <error_message>" and exits with code 1 if invalid.
    """

    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
            if not content:
                raise ValueError("Empty JSON file")

            data = json.loads(content)

            if isinstance(data, dict):
                if all(validate_value(value) for value in data.values()):
                    print("Valid JSON object with nested objects and arrays")
                    sys.exit(0)
                else:
                    raise ValueError("Invalid value types found in JSON object")
            else:
                raise ValueError("Not a JSON object")
            
    except (json.JSONDecodeError, ValueError) as error:
        print("Invalid JSON", str(error))
        sys.exit(1)

def validate_value(value: Any) -> bool:
    """
    Recursively validates that a value is one of the allowed JSON types:
    - String
    - Number (int or float)
    - Boolean
    - Null (None)
    - Object (dict)
    - Array (list)

    Args:
        value (Any): The value to validate.
    
    Returns:
        bool: True if the value is valid, False otherwise.
    """

    valid_primitive_types = (str, int, float, bool, type(None))

    if isinstance(value, valid_primitive_types):
        return True
    elif isinstance(value, dict):
        # Recursively validate each value in the nested object
        return all(validate_value(v) for v in value.values())
    elif isinstance(value, list):
        # Recursively validate each item in the list
        return all(validate_value(item) for item in value)
    else:
        # Invalid types found
        return False


if __name__ == '__main__':
    import argparse

    # setting up argument parsing for the file input
    parser = argparse.ArgumentParser(description="JSON Parser for nested objects and arrays")
    parser.add_argument("file", type=str, help="Path to the JSON file to validate")
    args = parser.parse_args()

    # validate the provided JSON file 
    validate_json(args.file)
