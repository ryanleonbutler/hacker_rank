if __name__ == '__main__':
    n = int(input())
    newList = []
    txt = ""

    for i in range(n):
        newList.append(i+1)

    for item in newList:
        txt += str(item)

    print(txt)