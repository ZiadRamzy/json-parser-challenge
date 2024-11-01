#!/bin/bash

python parser.py tests/step1/valid.json
echo "Exit code: $?"

python parser.py tests/step1/invalid.json
echo "Exit code: $?"