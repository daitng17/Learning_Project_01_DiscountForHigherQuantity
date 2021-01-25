# strings and bytes are not dierectly interchangable
# strings contain unicode, bytes are raw 8-bit values

def main():
    # define some starting values
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = "This is a string"
    print(s)

    s2 = b.decode("utf-8")
    print(s+s2)

    b2 = s.encode("utf-8")
    print(b+b2)

    b3 = s.encode("utf-32")
    print(b3)

if __name__ == "__main__":
    main()

## cannot combine strings and bytes directly

