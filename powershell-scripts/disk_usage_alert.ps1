#!/usr/bin/env pwsh


# Task:
# Monitor the root directory's disk usage and send an alert if it exceeds 90%.

# Check if the script is being run from another script, if so, exit without executing the rest of the script.
if ($myInvocation.InvocationName -ne '') { return }

# Get the root drive details
$rootDrive = Get-PSDrive -Name "Root" -PSProvider FileSystem

# Calculate the used space, total space, and disk usage percentage.
$usedSpace = $rootDrive.Used
$totalSpace = $rootDrive.Size
$diskUsagePercent = ($usedSpace / $totalSpace) * 100

# Check if the disk usage exceeds 90%, if so, output a warning message.
if ($diskUsagePercent -gt 90) {
    Write-Output "Disk usage alert! It's over 90%"
}

# Wait for 10 seconds before the next check.
Start-Sleep -Seconds 10