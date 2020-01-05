#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
    description: The counter class.
    author: LiangCL
    since: 2020/1/4
"""


class Counter:

    def __init__(self, value: int = 0, increments: int = 1):
        self.value = value
        self.increments = increments

    def incr(self) -> None:
        self.value += self.increments

    def __repr__(self) -> str:
        return f'Counter[ value = {self.value}, increments = {self.increments}].'


if __name__ == '__main__':
    counter = Counter()
    counter.incr()
    print(counter.value)
