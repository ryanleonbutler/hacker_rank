def create_hash(arr):
    hash(arr)
    return arr

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    list(integer_list)
    print(create_hash(integer_list))