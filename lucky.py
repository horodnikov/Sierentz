# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:51 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""
import re


def lucky_series(input_string: str):
    guess = re.findall(r'[5-6]+', input_string)
    if guess:
        sequence = [x for x in guess if len(set(x)) > 1]
        if len(sequence) > 0:
            return sorted(sequence, key=lambda x: len(x), reverse=True)[0]
    return 'Zero'


if __name__ == "__main__":
    seria = input('Please input numbers seria ')
    print(lucky_series(seria))
