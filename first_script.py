#!/usr/bin/env python3

import psutil
import time

while True:
    # CPU Usage
    cpu_percent = psutil.cpu_percent(interval=1)

    # Disk Usage
    disk_usage = psutil.disk_usage('/')  # '/' is the root partition
    total = disk_usage.total / (1024 ** 3)  # Convert bytes to GB
    used = disk_usage.used / (1024 ** 3)
    free = disk_usage.free / (1024 ** 3)
    percent = disk_usage.percent

    # Print results
    print(f"CPU Usage: {cpu_percent}%")
    print(f"Disk Usage: {percent}%")
    print(f" - Total: {total:.2f} GB")
    print(f" - Used:  {used:.2f} GB")
    print(f" - Free:  {free:.2f} GB")
    print('-' * 40)

