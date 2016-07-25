import time


def fib(n):
    arr = [0, 1]
    for i in range(2, n + 1):
        arr.append(arr[i - 1] + arr[i - 2])
    return arr[len(arr) - 1]


def main():
    n = int(input())
    start_time = time.time()
    print(fib(n))
    print("%s seconds elapsed" % (time.time() - start_time))


if __name__ == "__main__":
    main()