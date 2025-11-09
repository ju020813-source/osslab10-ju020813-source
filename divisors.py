import sys

def divisors(n: int):
    return [i for i in range(1, n + 1) if n % i == 0]

if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) >= 2 else sys.stdin.read().strip()
    n = int(arg)
    print(" ".join(str(x) for x in divisors(n)))
