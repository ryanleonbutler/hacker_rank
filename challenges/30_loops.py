#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    for i in range(10):
        i += 1
        answer = n * i
        print("{} x {} = {}".format(n, i, answer))

