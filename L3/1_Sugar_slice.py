

def s0():
    # list (aka array)
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(list(a))

    # start, stop increment
    print(list(a[1:4]))
    print(list(a[1:8:2]))


def s1():
    # fill in data
    a = range(10)
    print(list(a))

    # start, stop increment
    print(list(a[1:4]))
    print(list(a[1:8:2]))


def s2():
    # reverse works too
    print("Slicing is easy...")
    print("Slicing is easy..."[::-1])


def s3():
    #tuple
    t = (1, 2, "Three", "Four", 5, 6)
    # start, stop increment
    print(list(t[1:3]))

if __name__ == "__main__":
    s3()