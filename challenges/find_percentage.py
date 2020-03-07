def student_avg(student_marks, name):
    total = 0
    marks = student_marks[name]
    for i in marks:
        total += i
    total = (total / len(marks))
    return total

    
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print("%.2f" % student_avg(student_marks, query_name))