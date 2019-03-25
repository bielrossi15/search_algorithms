def interpolation_search(l: list, value: int):
    begin = 0
    end = len(l) - 1
    while begin <= end and l[begin] <= value <= l[end]:
        i = int(begin + (((end - begin)/(l[end] - l[begin])) * (value - l[begin])))
        if l[i] == value:
            print("{} was found at {}".format(value, i))
            return True

        if value > l[i]:
            begin = i + 1

        else:
            end = i - 1

    print("{} wasnt found".format(value))
    return False
