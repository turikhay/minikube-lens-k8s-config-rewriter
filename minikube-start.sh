#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"

minikube start

(cd "$SCRIPT_DIR" && source venv/bin/activate && python main.py)
