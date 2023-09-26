def split_and_join(line):
    new_string = line.split(" ")
    new_string = "-".join(new_string)
    return new_string

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)