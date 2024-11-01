import json
import sys
from typing import NoReturn


def validate_json(file_path: str) -> NoReturn:
    """
    Validate a JSON file containing a simple JSON object with string keys and values.

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
                if all(isinstance(key, str) and isinstance(value, str) for key, value in data.items()):
                    print("Valid JSON object with string keys and values")
                    sys.exit(0)
                else:
                    raise ValueError("Non-string keys or values present")
            else:
                raise ValueError("Not a JSON object")
    except (json.JSONDecodeError, ValueError) as error:
        print("Invalid JSON", str(error))
        sys.exit(1)


if __name__ == '__main__':
    import argparse

    # setting up argument parsing for the file input
    parser = argparse.ArgumentParser(description="JSON Parser for string key-value pairs")
    parser.add_argument("file", type=str, help="Path to the JSON file to validate")
    args = parser.parse_args()

    # validate the provided JSON file 
    validate_json(args.file)
