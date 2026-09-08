#!/bin/bash

# Ensure build fails on any command error
set -e

echo "=== Installing Dependencies ==="
python3 -m pip install -r requirements.txt

echo "=== Collecting Static Files ==="
python3 manage.py collectstatic --noinput --clear

echo "=== Build Complete ==="