#!/bin/bash

# Task:
# Monitor disk usage and send an alert if the usage exceeds a specified threshold (e.g., 90%).

# Extensive Comments:
# - The #!/bin/bash at the beginning of the script specifies the interpreter for executing the script.
# - We define a disk usage threshold (in this case, 90%) which you can adjust.
# - An infinite while loop is used to periodically check the disk usage.
# - Inside the loop, we use the df command, which reports the amount of disk space used by file systems. We then extract the usage percentage for the root filesystem.
# - The tail -1 command ensures we only get the last line of the df output, which contains the relevant usage information.
# - The awk '{print $5}' command extracts the fifth field (i.e., the usage percentage) from the output.
# - The sed 's/%//g' command is used to strip the '%' character from the output.
# - We then compare the extracted usage value against our defined threshold to decide whether to send an alert.
# - The sleep 10 command makes the script wait for 10 seconds before rechecking the disk usage.

while true; do
    # Extract the disk usage percentage for the root filesystem.
    usage=$(df / | tail -1 | awk '{print $5}' | sed 's/%//g')
    # Check if the usage exceeds the threshold.
    if [ $usage -gt 90 ]; then
        echo "Disk Usage is above 90%"
    fi
    # Wait for 10 seconds before rechecking.
    sleep 10
done
