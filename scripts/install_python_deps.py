#!/usr/bin/env python3
"""
Sanity checks the Python environment
"""
import sys
from subprocess import check_call, check_output

# Check Python version
if sys.version_info < (3,6):
    sys.exit("mitmproxy-node requires a Python version >= 3.6, but found {}.{}".format(sys.version_info[0], sys.version_info[1]))

# Install dependencies with pip3 first.
# If pip3 isn't found, use pip.
try:
    check_call(["pip3", "install", "-r", "requirements.txt"])
except FileNotFoundError:
    check_call(["pip", "install", "-r", "requirements.txt"])
