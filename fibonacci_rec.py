import time

def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return fib(n-1) + fib(n-2)


def main():
    n = int(input())
    start_time = time.time()
    print(fib(n))
    print("%s seconds elapsed" % (time.time() - start_time))


if __name__ == "__main__":
    main()
