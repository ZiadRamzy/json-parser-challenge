# JSON Parser Coding Challenge

## Overview

This project implements a custom JSON parser as part of a coding challenge series. The parser is built to progressively handle various JSON structures, ensuring validity and providing meaningful error messages for invalid JSON files. The challenge was designed to strengthen understanding of parsing techniques and JSON standards.

## Features

The parser is implemented in Python and supports the following functionalities:

1. **Basic JSON Validation:**

   - Parses simple JSON objects, such as `{}`.
   - Identifies empty or invalid JSON files.

2. **String Key-Value Pairs:**

   - Parses JSON objects with string keys and string values, e.g., `{"key": "value"}`.

3. **Mixed Data Types:**

   - Parses JSON objects containing values of the following types:
     - Strings
     - Numbers (integers and floats)
     - Booleans (`true`, `false`)
     - Null (`null`)

4. **Nested Objects and Arrays:**

   - Handles JSON objects containing nested objects and arrays, e.g.,
     ```json
     {
       "key1": {},
       "key2": []
     }
     ```

5. **Custom Test Cases:**
   - Extensive testing of edge cases, including:
     - Valid JSON structures like deeply nested objects and mixed data types.
     - Invalid JSON structures with errors like trailing commas or non-string keys.

## Project Structure

```
json-parser/
├── parser.py           # Main script for JSON parsing
├── tests/
│   ├── step1/          # Test files for Step 1
│   ├── step2/          # Test files for Step 2
│   ├── step3/          # Test files for Step 3
│   ├── step4/          # Test files for Step 4
│   └── step5/          # Custom test cases for Step 5
├── run_tests.sh        # Bash script for automating tests
└── README.md           # Project documentation
```

## How to Use

### Prerequisites

- Python 3.9 or later

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/json-parser-challenge.git
   cd json-parser-challenge
   ```
2. Make the test script executable:
   ```bash
   chmod +x run_tests.sh
   ```

### Running the Parser

To validate a JSON file, run the following command:

```bash
python parser.py <path-to-json-file>
```

- Example:
  ```bash
  python parser.py tests/step1/valid.json
  ```

### Running Tests

To execute all test cases, run the test script:

```bash
./run_tests.sh
```

This will validate all JSON files in the `tests/` directory and display the results along with exit codes.

## Test Cases

### Valid JSON Examples

1. `{}` (Empty JSON object)
2. ```json
   {
     "key": "value",
     "key-n": 123,
     "key-b": true,
     "key-null": null,
     "key-o": { "subkey": "subvalue" },
     "key-a": [1, 2, 3]
   }
   ```

### Invalid JSON Examples

1. Trailing commas:
   ```json
   { "key": "value" }
   ```
2. Non-string keys:
   ```json
   { "123": "value" }
   ```

## Coding Challenge Citation

This project is based on the JSON parser coding challenge from [Coding Challenges](https://codingchallenges.fyi/challenges/challenge-json-parser).

## License

This project is open-source and available under the MIT License.
