def main():
    ctemps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]

    print(list(map(lambda t: (t-32) * 5/9, ftemps)))
    print(list(map(lambda t: (t*9/5) + 32, ctemps)))

if __name__ == "__main__":
    main()