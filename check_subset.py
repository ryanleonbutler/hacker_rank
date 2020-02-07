N = int(input())
for i in range(0, N):
    len_a = int(input())
    a = input()
    len_b = int(input())
    b = input()
    list_a = a.split()
    list_b = b.split()
    count = 0
    for i in list_a:
        for n in list_b:
            if i == n:
                count += 1
    if count == len_a:
        print("True")
    else:
        print("False")