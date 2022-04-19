import re

# Refer to README.md for the problem instructions


def count_pieces(testString):
    digits = sum(c.isdigit() for c in testString)
    whitespaces  = sum(c.isspace() for c in testString)
    nondigits = sum((c != None) for c in testString) - digits - whitespaces
    words = len(re.findall(r'\w+', testString))
    return [digits, nondigits, whitespaces, words]
