def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]
     
    i = iter(days)
    #  print(next(i))
    #  print(next(i))
    #  print(next(i))

    #  with open("testfile.txt", "r") as fp:
    #      for line in iter(fp.readline, ""):
    #          print(line)

    # for m in range(len(days)):
    #     print(m+1, days[m])

    # for i,m in enumerate(days, start=1):
    #     print(i,m)

    # use zip to combine sequences
    for i, m in enumerate(zip(days, daysFr), start=1):
        print(i, m[0], "=", m[1], "in French")

if __name__ == "__main__":
    main()