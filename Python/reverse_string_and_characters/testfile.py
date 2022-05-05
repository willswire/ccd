#!/usr/bin/env python

# Refer to README.md for the problem instructions


def reverse_strings(string_list):
    res = list()
    for string in string_list:
        res.append(string[::-1])
    return " ".join(res)
