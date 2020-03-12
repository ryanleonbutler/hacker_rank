if __name__ == '__main__':
    N = int(input())
    my_list = []
    for i in range(N):
        string = input().split()
        cmd = string[0]
        args = string[1:]
        if cmd != "print":
            cmd += "(" + ",".join(args) + ")"
            eval("my_list." + cmd)
        else:
            print(my_list)
