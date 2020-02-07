# my own version of bubble sort

from datetime import datetime

MY_LIST = [160, 190, 60, 20, 30, 140, 180, 50, 100, 10, 90, 80, 40, 190, 70, 110, 130, 200, 120, 170, 150]

start_time = datetime.now()

def my_bubble_sort(my_list):
    n = 0
    while True:
        try:
            for i in range(0, len(my_list)):
                if my_list[0+n] <= my_list[1+n]:
                    n += 1
                    if n == len(my_list):
                        return(my_list)
            else:
                temp = my_list[0+n]
                my_list[0+n] = my_list[1+n]
                my_list[1+n] = temp
                n = 0
        except IndexError:
            return(my_list)
        
print(my_bubble_sort(MY_LIST))

end_time = datetime.now()
print(f'Duration: {format(end_time - start_time)}')