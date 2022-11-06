# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:22 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""


def sum_in_array(lst: list, guess: int):
    seen = set()
    for i in lst:
        diff = guess - i
        if diff in seen:
            return [diff, i]
        seen.add(i)
    return [-1]


if __name__ == "__main__":
    print(sum_in_array([2, 7, 4, 5, 6, 10], 8))
