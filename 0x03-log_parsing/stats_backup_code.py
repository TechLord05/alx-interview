#!/usr/bin/python3

"""Write a script that reads stdin line by line and compute metrics"""

import re


def print_stats(status_counts: int, file_size: int):
    """function to print out the stats"""
    print("File size: {}".format(file_size))
    for status in sorted(status_counts):
        if status_counts[status] > 0:
            print("{}: {}".format(status, status_counts[status]))


def print_logs():
    """
    Reads logs from standard input and generates reports
    Reports:
        * Prints log size after reading every 10 lines & at KeyboardInterrupt
    Raises:
        KeyboardInterrupt (Exception): handles this exception and raises it
    """

    input_format = re.compile(
        r'^(?P<ip>\S+) - \[(?P<date>.+)\] "GET /projects/260 HTTP/1.1" (?P<status>\d{3}) (?P<size>\d+)$'
    )

    stdin = __import__('sys').stdin
    line_read = 0
    total_size = 0
    status_counts = {}
    valid_status_codes = {200, 301, 400, 401, 403, 404, 405, 500}

    try:
        for line in stdin:
            line_read += 1

            # Match the line against the regex pattern
            match = input_format.match(line.strip())
            if not match:
                continue
            # Extract File size and status code
            size = int(match.group('size'))
            status = int(match.group('status'))

            total_size += size
            if status in valid_status_codes:
                if status in status_counts:
                    status_counts[status] += 1
                else:
                    status_counts[status] = 1

            if line_read % 10 == 0:
                print_stats(status_counts, total_size)
                line_read = 0
        print_stats(status_counts, total_size)

    except KeyboardInterrupt:
        print_stats(status_counts, total_size)
        raise


if __name__ == "__main__":
    print_logs()
