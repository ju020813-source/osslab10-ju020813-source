# lab10.py
# LAB10: 정수의 약수 구하기

def divisors(n: int):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result


if __name__ == "__main__":
    n = int(input())        # 사용자로부터 정수 입력
    print(*divisors(n))     # 약수들을 공백으로 구분해 한 줄에 출력
