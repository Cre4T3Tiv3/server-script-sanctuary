#!/usr/bin/env pwsh

# Task:
# Monitor the root directory's disk usage and send an alert if it exceeds 90%.

# Extensive Details:
# - The script is suitable for any OS with PowerShell Core, which includes Windows, Linux, and macOS.
# - We define a disk usage threshold (in this case, 90%) which you can adjust.
# - We use the `Get-PSDrive` cmdlet, which works across multiple OSes, to get details of the root filesystem.
# - We calculate the usage percentage by dividing the used space by the total space.
# - We compare the usage value against our defined threshold to decide whether to send an alert.
# - The `Start-Sleep -Seconds 10` command makes the script wait for 10 seconds before rechecking the disk usage.

$rootDrive = Get-PSDrive -Name "Root" -PSProvider FileSystem
$usedSpace = $rootDrive.Used
$totalSpace = $rootDrive.Size
$diskUsagePercent = ($usedSpace / $totalSpace) * 100

if ($diskUsagePercent -gt 90) {
    Write-Output "Disk usage alert! It's over 90%"
}
Start-Sleep -Seconds 10
<<<<<<< HEAD
=======
git commit -m 'update(details): revised the Extensive Details across all in-scope code.'
>>>>>>> a5cdbfc23a9abfbadd58a672ea6dadbbb2ccf5a7
