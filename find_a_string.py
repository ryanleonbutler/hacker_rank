def count_substring(string, sub_string):
    count = 0
    new_string = ''
    try:
        for i in range(0, len(string)):
            new_string += string[i]
            if new_string == sub_string:
                count += 1
    except IndexError as e:
        pass
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)