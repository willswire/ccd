#!/usr/bin/env python

# Refer to README.md for the problem instructions

import os

def dir_reader(dir_path):
    result = {}

    dirs = os.listdir(dir_path)

    for d in dirs:
        if (d.__contains__(".txt")):
            key = dir_path + '/' + d
            value = ''
            with open(key) as f:
                value = f.read()
            result[key] = value

    return result
