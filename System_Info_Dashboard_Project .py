#!/usr/bin/env python3
import subprocess
import re

def get_memory_info():
    # Run 'free -m' command and parse output
    result = subprocess.run(['free', '-m'], stdout=subprocess.PIPE)
    lines = result.stdout.decode('utf-8').split('\n')
    mem_line = lines[1].split()
    total, used, free = mem_line[1:4]
    return f"Memory: {used}MB used / {total}MB total (Free: {free}MB)"

def get_disk_info():
    # Run 'df -h' and parse root partition usage
    result = subprocess.run(['df', '-h', '/'], stdout=subprocess.PIPE)
    line = result.stdout.decode('utf-8').split('\n')[1]
    parts = re.split(r'\s+', line)
    return f"Disk: {parts[4]} used on {parts[0]}"

def get_cpu_info():
    # Run 'top' to get CPU usage (simplified)
    result = subprocess.run(['top', '-bn1'], stdout=subprocess.PIPE)
    cpu_line = result.stdout.decode('utf-8').split('\n')[2]
    return f"CPU: {cpu_line.split()[1]}% usage"

def main():
    print("==== System Info Dashboard ====")
    print(get_memory_info())
    print(get_disk_info())
    print(get_cpu_info())

if __name__ == "__main__":
    main()