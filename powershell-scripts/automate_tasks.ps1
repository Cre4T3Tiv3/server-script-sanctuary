#!/usr/bin/env pwsh

# Task:
# Monitor the root directory's disk usage and send an alert if it exceeds 90%.

# Extensive Comments:
# - The `#!/usr/bin/env pwsh` at the beginning of the script specifies the interpreter for executing the script.
# - We define a disk usage threshold (in this case, 90%) which you can adjust.
# - The `df /` command reports the amount of disk space used by file systems.
# - `tail -1` ensures we only get the last line of the df output, which contains the relevant usage information.
# - `awk '{print $5}'` extracts the fifth field (i.e., the usage percentage) from the output.
# - `sed 's/%//g'` is used to strip the '%' character from the output.
# - We then compare the extracted usage value against our defined threshold to decide whether to send an alert.
# - The `Start-Sleep -s 10` command makes the script wait for 10 seconds before rechecking the disk usage.

$diskUsage = df / | tail -1 | awk '{print $5}' | sed 's/%//g'
if ($diskUsage -gt 90) {
    Write-Output "Disk usage alert! It's over 90%"
}
Start-Sleep -s 10
