"""
INPUT:
rank    age     height
5       3
10      2       5
7       1       0
9       9       9
1       23      12
6       5       9

k = 1

RESULT:
rank    age     height
7       1       0
10      2       5
6       5       9
9       9       9
1       23      12
"""
from typing import List


def athlete_sort(athletes: List[List[int]], sort_column: int) -> List[List[int]]:
    for athlete in athletes:
        if len(athlete) < 3:
            athletes.remove(athlete)

    athletes.sort(key=lambda x: x[sort_column])
    return athletes
