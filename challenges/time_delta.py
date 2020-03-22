#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):
    date_fmt = "%a %d %b %Y %H:%M:%S %z"
    a = datetime.strptime(t1, date_fmt)
    b = datetime.strptime(t2, date_fmt)

    difference = int(abs((a - b).total_seconds()))

    return str(difference)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        print(delta)
