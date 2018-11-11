# 제곱
# 재귀 연습을 위하여 2^3과 같은 형태의 지수형태의 값을 처리하는 함수를 정의하여 문제를 풀어봅니다.
#
# 문제
# 두 수 n,m을 입력받아 n ^ M 의 값을 출력하는 프로그램을 작성해봅니다.
#
# 입력
# 첫번째 줄에 두 수 n,m이 주어집니다. n과 m은 1보다 크거나 같고, 10보다 작거나 같은 값이 주어집니다.
#
# 출력
# 입력받은 두 수 n과 m의 제곱값을 출력합니다.
#
# 입력 예제
# 2 3
# 출력 예제
# 8

def pow(n, m) :

    if m == 0 :
        return 1
    else :
        return n * pow(n,m-1)

def main():

    data = input()

    n = int(data.split()[0])
    m = int(data.split()[1])

    print(pow(n, m))

if __name__ == "__main__":
    main()