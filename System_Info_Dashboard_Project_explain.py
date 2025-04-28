#!/usr/bin/env python3
# This is called a "shebang" line. It tells Linux to run this script with Python 3 
# when executed directly (e.g., `./system_dashboard.py`).

import subprocess  # Allows running Linux commands from Python.
import re          # Provides regex support for parsing text.

def get_memory_info():
    # Function to fetch memory usage using `free -m`.
    result = subprocess.run(['free', '-m'], stdout=subprocess.PIPE)
    # ^ Runs the Linux command `free -m` (shows memory in MB).
    # `stdout=subprocess.PIPE` captures the command's output.

    lines = result.stdout.decode('utf-8').split('\n')
    # ^ Decodes the command output (bytes) to a string and splits it into lines.

    mem_line = lines[1].split()  
    # ^ Selects the 2nd line (index 1) from `free -m` output, which contains memory stats.
    # `split()` breaks the line into a list of words (e.g., ["Mem:", "1000", "500", ...]).

    total, used, free = mem_line[1:4]  
    # ^ Extracts the 2nd, 3rd, and 4th items from the list (total/used/free memory in MB).

    return f"Memory: {used}MB used / {total}MB total (Free: {free}MB)"
    # ^ Returns a formatted string with the memory stats.

def get_disk_info():
    # Function to fetch disk usage using `df -h /` (shows root partition).
    result = subprocess.run(['df', '-h', '/'], stdout=subprocess.PIPE)
    # ^ Runs `df -h /` (disk space on root partition in human-readable format).

    line = result.stdout.decode('utf-8').split('\n')[1]
    # ^ Gets the 2nd line (index 1) of `df` output, which contains the root partition stats.

    parts = re.split(r'\s+', line)  
    # ^ Splits the line by whitespace (regex `\s+`) into a list (e.g., ["/dev/sda1", "50G", ...]).

    return f"Disk: {parts[4]} used on {parts[0]}"  
    # ^ `parts[4]` is the usage % (e.g., "45%"), `parts[0]` is the disk name (e.g., "/dev/sda1").

def get_cpu_info():
    # Function to fetch CPU usage using `top -bn1` (batch mode, 1 iteration).
    result = subprocess.run(['top', '-bn1'], stdout=subprocess.PIPE)
    # ^ Runs `top -bn1` (non-interactive, single output).

    cpu_line = result.stdout.decode('utf-8').split('\n')[2]
    # ^ Gets the 3rd line (index 2) of `top` output, which contains CPU stats.

    return f"CPU: {cpu_line.split()[1]}% usage"  
    # ^ Splits the line and extracts the 2nd item (CPU usage %).

def main():
    # Main function to display all system info.
    print("==== System Info Dashboard ====")
    print(get_memory_info())  # Calls and prints memory stats.
    print(get_disk_info())    # Calls and prints disk stats.
    print(get_cpu_info())     # Calls and prints CPU stats.

if __name__ == "__main__":
    # This block runs only if the script is executed directly (not imported as a module).
    main()