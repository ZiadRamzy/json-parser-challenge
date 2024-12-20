#!/bin/bash

# step 1 tests
echo "Testing step 1 JSON files:"
python parser.py tests/step1/valid.json
echo "Exit code: $?"

python parser.py tests/step1/invalid.json
echo "Exit code: $?"


# step 2 tests
echo "Testing step 2 JSON files:"
python parser.py tests/step2/valid.json
echo "Exit code: $?"

python parser.py tests/step2/valid2.json
echo "Exit code: $?"

python parser.py tests/step2/invalid.json
echo "Exit code: $?"

python parser.py tests/step2/invalid2.json
echo "Exit code: $?"

# Run tests for Step 3
echo "Testing Step 3 JSON files:"
python parser.py tests/step3/valid.json 
echo "Exit code: $?"

python parser.py tests/step3/invalid.json
echo "Exit code: $?"

# Run tests for Step 4
echo "Testing Step 4 JSON files:"
for file in tests/step4/*.json; do
    echo "Testing $file"
    python parser.py "$file"
    echo "Exit code: $?"
    echo "------------------------"
done

# Run tests for Step 5
echo "Running custom tests for Step 5:"
# Loop through all valid and invalid files
for file in tests/step5/*.json; do
    echo "Testing $file"
    python parser.py "$file"
    echo "Exit code: $?"
    echo "------------------------"
done