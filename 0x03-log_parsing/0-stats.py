#!/usr/bin/python3

"""
Log Parsing
"""

import sys


def print_stats(status_code_counts, total_size):
    """Prints information"""
    print("File size: {:d}".format(total_size))
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] != 0:
            print("{}: {:d}".format(code, status_code_counts[code]))


status_code_counts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                      "404": 0, "405": 0, "500": 0}

count = 0
total_size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            print_stats(status_code_counts, total_size)

        line_list = line.split()
        count += 1

        try:
            total_size += int(line_list[-1])
        except ValueError:
            pass

        try:
            if line_list[-2] in status_code_counts:
                status_code_counts[line_list[-2]] += 1
        except IndexError:
            pass

    print_stats(status_code_counts, total_size)

except KeyboardInterrupt:
    print_stats(status_code_counts, total_size)
    raise
