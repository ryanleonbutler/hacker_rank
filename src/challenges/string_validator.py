def validate(string):
    for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
        print(any(method(c) for c in string))


if __name__ == '__main__':
    s = input()
    validate(s)

#qA2