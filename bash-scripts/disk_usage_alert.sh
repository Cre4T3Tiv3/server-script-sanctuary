#!/bin/bash

# Task:
# Monitor disk usage and send an alert if the usage exceeds a specified threshold (e.g., 90%).

# If this script is sourced from another script, return without executing the rest of the script.
if [[ "$0" != "$BASH_SOURCE" ]]; then return; fi

# Define the disk usage threshold.
threshold=90

# Start an infinite loop to periodically check the disk usage.
while true; do
    # Extract the disk usage percentage for the root filesystem.
    usage=$(df / | tail -n 1 | awk '{print $5}' | tr -d '%')

    # Check if the usage exceeds the threshold.
    if (( usage > threshold )); then
        echo "Disk Usage is above 90%"
    fi

    # Wait for 10 seconds before rechecking.
    sleep 10
done