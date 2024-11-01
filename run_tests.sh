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
