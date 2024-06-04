#!/usr/bin/python3
"""
Log parsing script that reads log entries from standard input (stdin),
parses them, and computes metrics. It prints the total file size and a
breakdown of the number of occurrences for each status code (200, 301,
400, 401, 403, 404, 405, 500) every 10 lines or upon keyboard interruption
(CTRL+C).
"""

import sys
import re


def is_valid_log_entry(line):
  """
  Checks if a line matches the expected log entry format using a regular expression.

  Args:
      line (str): The line to be validated.

  Returns:
      bool: True if the line matches the format, False otherwise.
  """
  log_pattern = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] \"GET /projects/260 HTTP/1.1\" (\d+) (\d+)"
  return bool(re.match(log_pattern, line.strip()))


def parse_log_entry(line):
  """
  Parses a valid log entry line and extracts relevant information.

  Args:
      line (str): The valid log entry line.

  Returns:
      tuple: A tuple containing (IP address, date, status code, file size).
  """
  log_pattern = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] \"GET /projects/260 HTTP/1.1\" (\d+) (\d+)"
  match = re.match(log_pattern, line.strip())
  return match.groups()


def main():
  """
  The main function that reads log entries, parses them, and prints statistics.
  """
  total_size = 0
  status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
  line_count = 0

  try:
    for line in sys.stdin:
      line_count += 1

      if not is_valid_log_entry(line):
        continue

      ip, date, status_code, file_size = parse_log_entry(line)

      file_size = int(file_size)

      total_size += file_size
      status_codes[int(status_code)] += 1

      if line_count % 10 == 0 or line_count == 1:
        print(f"File size: {total_size}")
        for code, count in sorted(status_codes.items()):
          if count > 0:
            print(f"{code}: {count}")

  except KeyboardInterrupt:
    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
      if count > 0:
        print(f"{code}: {count}")


if __name__ == "__main__":
  main()
