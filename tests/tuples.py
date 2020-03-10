from challenges import tuples

arr = (1, 2)

def test_hash():
    answer = 3713081631934410656
    print(tuples.create_hash(arr))
    assert tuples.create_hash(arr) == answer

if __name__ == "__main__":
    test_hash()
    print("Tests Passed")