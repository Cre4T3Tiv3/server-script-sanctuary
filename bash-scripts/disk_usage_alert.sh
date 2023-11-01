#!/bin/bash


# Task:
# This script monitors the disk usage and sends an alert if the usage exceeds a specified threshold (90% in this case).

# If this script is sourced from another script, it will return without executing the rest of the script.
# This is to prevent the script from running in a different context than intended.
if [[ "$0" != "$BASH_SOURCE" ]]; then return; fi

# The disk usage threshold is defined here. If the disk usage exceeds this value, an alert will be printed.
threshold=90

# An infinite loop is started to periodically check the disk usage.
while true; do
    # The disk usage percentage for the root filesystem is extracted using the 'df' command.
    # The 'awk' command is used to select the fifth field (which contains the disk usage percentage) from the output of 'df'.
    # The 'tr' command is used to remove the '%' character from the output.
    usage=$(df / | tail -n 1 | awk '{print $5}' | tr -d '%')

    # If the disk usage exceeds the threshold, an alert is printed to the console.
    if ((usage > threshold)); then
        echo "Disk Usage is above 90%"
    fi

    # The script waits for 10 seconds before checking the disk usage again.
    sleep 10
done
