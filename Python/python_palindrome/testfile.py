# Refer to README.md for the problem instructions


def palindrome(number):
    num = str(number)

    l = 0
    r = len(num) - 1
    while (num[l] == num[r]):
        if (l == r):
            return 'palindrome'
        else:
            l += 1
            r -= 1

    return 'NOT a palindrome'
