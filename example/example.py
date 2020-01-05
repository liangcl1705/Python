#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
    description: This is an example for printing the current second.
    author: LiangCL
    since: 2020/1/5
"""

from datetime import datetime
import time

odds = [
    1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21,
    23, 25, 27, 29, 31, 33, 35, 37, 39, 41,
    43, 45, 47, 49, 51, 53, 55, 57, 59
]

if __name__ == '__main__':
    for i in range(5):
        current_second = datetime.today().second
        print(f'The current second is: {current_second}')

        if current_second in odds:
            print('This second is an odd.')
        else:
            print('This second is an even.')

        time.sleep(1)
