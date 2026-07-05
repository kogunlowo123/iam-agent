#!/bin/bash
set -euo pipefail
echo "Setting up IAM Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
