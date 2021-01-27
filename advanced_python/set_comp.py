import random

def main():
    ctemps = random.sample(range(0,31), 15)
    ftemps1 = [(t*9/5)+32 for t in ctemps]
    ftemps2 = {(t*9/5)+32 for t in ctemps}
    print(ftemps1)
    print(ftemps2)

    sTemp = 'The quick brown fox jumped over the lazy dog'
    chars = {c.upper() for c in sTemp if not c.isspace()}
    print(chars)



if __name__ == '__main__':
    main()

