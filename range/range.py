def main():
    for i in range(10):
        print(i)


def test():
    for i in range(1000000000000000000000000000000000):
        print(i)
        if i > 10:
            break


if __name__ == '__main__':
    main()
