import itertools

def testFunction(x):
    return x < 40

def main():
    # cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    # print(next(cycle1))
    # print(next(cycle1))
    # print(next(cycle1))
    # print(next(cycle1))
    # print(next(cycle1))

    # create a simple counter
    count1 = itertools.count(100, 10)
    # print(next(count1))
    # print(next(count1))
    # print(next(count1))
    # print(next(count1))

    # accumulate values
    vals = [10,20,30,40,50,40,30]
    # acc = itertools.accumulate(vals, max)
    # print(list(acc))

    # connect sequences 
    # x = itertools.chain("AFFG", "1243")
    # print(list(x))

    # takewhile and dropwhile until it reaches a trigger point
    print(list(itertools.dropwhile(testFunction, vals)))
    print(list(itertools.takewhile(testFunction, vals)))


if __name__ == "__main__":
    main()