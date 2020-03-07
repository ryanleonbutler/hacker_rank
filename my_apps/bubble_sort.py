# my own version of bubble sort

from datetime import datetime

MY_LIST = [212, 543, 65, 4, 3, 56, 765]

start_time = datetime.now()

def my_bubble_sort_v1(l):
    n = 0
    while True:
        for i in range(0, len(l)):
            try:
                if l[0 + n] <= l[1 + n]:
                    n += 1
                    if n == len(l):
                        break
                else:
                    temp = l[0 + n]
                    l[0 + n] = l[1 + n]
                    l[1 + n] = temp
                    n = 0
            except IndexError as e:
                pass
    return l


def my_bubble_sort_v2(l):
    n = len(l)
    for i in range(n):
        #print(f"i = {i}")
        for j in range(0, n - i - 1):
            #print(f"j = {j}")
            #print(f"n - i - 1 = {n - i - 1}")
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]


if __name__ == "__main__":

    # My Sort
    # my_bubble_sort_v1(MY_LIST)
    #my_bubble_sort_v2(MY_LIST)
    #print(MY_LIST)

    #Built in Sort:
    print(sorted(MY_LIST))

    end_time = datetime.now()
    print(f"Duration: {format(end_time - start_time)}")
