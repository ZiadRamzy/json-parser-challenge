import json
import sys
from typing import NoReturn


def validate_json(file_path: str) -> NoReturn:
    """
    Validate a JSON file.

    Args:
        - file_path (str): Path to the JSON file to validate.
    
    Output:
        - Prints "Valid JSON object" and exits with code 0 if the JSON is valid.
        - Prints "Invalid JSON: <error_message>" and exits with code 1 if invalid.
    """

    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
            if not content:
                raise ValueError("Empty JSON file")

            data = json.loads(content)

            if isinstance(data, dict):
                print("Valid JSON object")
                sys.exit(0)
            else:
                raise ValueError("Not a JSON object")
    except (json.JSONDecodeError, ValueError) as error:
        print("Invalid JSON", str(error))
        sys.exit(1)


if __name__ == '__main__':
    import argparse

    # setting up argument parsing for the file input
    parser = argparse.ArgumentParser(description="Simple JSON Parser")
    parser.add_argument("file", type=str, help="Path to the JSON file to validate")
    args = parser.parse_args()

    # validate the provided JSON file 
    validate_json(args.file)
