#!/usr/bin/python3
"""
This module contains the function that displays
stats from the standard input.
"""
import re
from sys import stdin

def status_printer(total_size, status):
    """A method to print the status with the format given."""
    print('File size: {}'.format(total_size))
    for code, count in sorted(status.items()):
        if count > 0:
            print('{}: {}'.format(code, count))

def main():
    """Main method."""
    status_codes = {'200': 0, '301': 0, '400': 0,
                    '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    total = 0
    count = 0
    pattern = re.compile(r'\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)')
    
    try:
        for line in stdin:
            match = pattern.search(line)
            if match:
                code, file_size = match.groups()
                if code in status_codes:
                    status_codes[code] += 1
                    total += int(file_size)
                    count += 1
                
                if count % 10 == 0:
                    status_printer(total_size=total, status=status_codes)
                
    except KeyboardInterrupt:
        status_printer(total_size=total, status=status_codes)
        print("\nProgram interrupted by user.")

if __name__ == '__main__':
    main()
