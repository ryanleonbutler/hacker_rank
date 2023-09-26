# Enter your code here. Read input from STDIN. Print output to STDOUT
numbers = []

N = int(input())
for _ in range(N):
    numbers.append(input().split())

for num in numbers:
    try:
        a = int(num[0])
        b = int(num[1])
        print(int(a / b))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)
