def linear_search(l: list, value: int):
    for i in l:
        if value == l[i]:
            print('{} was found at {}'.format(value, i))
            return True
    print("{} wasnt found".format(value))
    return False
