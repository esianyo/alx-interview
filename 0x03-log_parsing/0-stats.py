#!/usr/bin/env python3
import sys
from collections import defaultdict


def is_valid_line(line):
    """
    Checks if the line follows the expected format.
    """
    try:
        # Split based on spaces, ensuring there are at least 7 parts
        parts = line.split()
        if len(parts) < 7:
            return False

        # Check IP address format (basic validation)
        if not all(0 <= int(part) <= 255 for part in parts[:4]):
            return False

        # Check status code is an integer
        int(parts[5])
        int(parts[6])
        return True
    except ValueError:
        return False


def parse_line(line):
    """
    Extracts relevant information from a valid line.
    """
    return int(line.split()[-1])


def print_stats(total_size, status_counts):
    """
    Prints the total file size and status code counts.
    """
    print(f"Total file size: {total_size}")

    for code, count in sorted(status_counts.items()):
        print(f"{code}: {count}")


total_size = 0
status_counts = defaultdict(int)
line_count = 0

for line in sys.stdin:
    line_count += 1

    if not is_valid_line(line):
        continue

    file_size = parse_line(line)
    total_size += file_size
    status_counts[int(line.split()[5])] += 1

    # Print statistics every 10 lines or on keyboard interrupt
    if line_count % 10 == 0 or line_count == 1:
        print_stats(total_size, status_counts)
        status_counts.clear()  # Reset counts for the next batch


# Print final statistics after processing all lines
if line_count > 0:
    print_stats(total_size, status_counts)
