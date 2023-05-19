#!/usr/bin/python3
""" Module for log parsing interview question
"""

import sys

status_codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0}

total_file_size = 0
count = 0

try:
    for line in sys.stdin:
        log_line = line.split(" ")

        if len(log_line) > 4:
            status_code = log_line[-2]
            file_size = int(log_line[-1])

            # Update values in dict for status codes
            if status_code in status_codes_dict.keys():
                status_codes_dict[status_code] += 1

            # Increment total file size
            total_file_size += file_size

            # Count the lines
            count += 1

        # Print the stats
        if (count % 10 == 0):
            print("File size: {}".format(total_file_size))
            for key, value in sorted(status_codes_dict.items()):
                if value != 0:
                    print("{}: {}".format(key, value))
        # print(log_line)

except Exception as e:
    pass

finally:
    # Print stats if keyboard interrupt or end of file
    print("File size: {}".format(total_file_size))
    for key, value in sorted(status_codes_dict.items()):
        if value != 0:
            print("{}: {}".format(key, value))
