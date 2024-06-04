#!/usr/bin/python3
"""
Log parsing script to read from stdin and compute metrics
"""
import sys


def print_stats(total_size, status_codes):
    """
    Print the accumulated statistics
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    """
    Main function to parse logs and print statistics
    """
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 7:
                continue

            try:
                file_size = int(parts[-1])
                status_code = int(parts[-2])
                total_size += file_size

                if status_code in status_codes:
                    status_codes[status_code] += 1

            except (ValueError, IndexError):
                continue

            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()
