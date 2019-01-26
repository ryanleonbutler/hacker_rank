# Student Marks - Nested List
# Author: Ryan
print("---STUDENT MARK PROGRAM---")
print("")

print("Welcome, how many students and their marks do you wish to enter?")
n = int(input())

markSheet = []

for i in range(n):
    print("Please enter student name:")
    name = input()
    print("Please enter mark:")
    mark = float(input())
    markSheet.append([name, mark])

markSheet = sorted.markSheet

