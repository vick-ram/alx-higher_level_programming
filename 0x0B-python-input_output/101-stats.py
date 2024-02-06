#!/usr/bin/python3
"""101-stats module"""
import sys


def print_stats(total_size, status_codes):
    """
    Print statistics for total file size and number
    of lines by status code.
    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing
        counts for each status code.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


def main():
    total_size = 0
    status_codes = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }
    try:
        for i, line in enumerate(sys.stdin, 1):
            try:
                spltLne = line.split()
                ip, status_code, size = spltLne[0], spltLne[8], spltLne[10]
                total_size += int(size)
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except (IndexError, ValueError):
                continue
            if i % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
