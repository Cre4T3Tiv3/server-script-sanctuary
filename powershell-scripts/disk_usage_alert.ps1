#!/usr/bin/env pwsh

# Task:
# This script monitors the disk usage of the root directory and sends an alert if the usage exceeds a specified threshold (90% in this case).

# If the script is being run from another script, it will exit without executing the rest of the script.
# This is to prevent the script from running in a different context than intended.
if ($myInvocation.InvocationName -ne '') { return }

# The root drive details are retrieved using the 'Get-PSDrive' cmdlet.
# The '-Name' parameter specifies the name of the drive and the '-PSProvider' parameter specifies the provider of the drive.
$rootDrive = Get-PSDrive -Name "Root" -PSProvider FileSystem

# The used space and total space of the root drive are retrieved from the 'Used' and 'Size' properties of the drive object, respectively.
# The disk usage percentage is then calculated by dividing the used space by the total space and multiplying by 100.
$usedSpace = $rootDrive.Used
$totalSpace = $rootDrive.Size
$diskUsagePercent = ($usedSpace / $totalSpace) * 100

# If the disk usage percentage exceeds 90%, a warning message is outputted using the 'Write-Output' cmdlet.
if ($diskUsagePercent -gt 90) {
    Write-Output "Disk usage alert! It's over 90%"
}

# The script waits for 10 seconds before performing the next disk usage check.
# This is done using the 'Start-Sleep' cmdlet with the '-Seconds' parameter specifying the number of seconds to wait.
Start-Sleep -Seconds 10