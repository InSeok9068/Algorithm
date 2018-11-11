# 곱셈
# 재귀 연습을 위하여 두 수의 곱을 구하는 함수를 재귀함수로 정의하여 문제를 풀어봅니다.
#
# 문제
# 두 수 n, m을 입력받아서 곱한값을 출력하는 프로그램을 작성해 봅니다.
#
# 입력
# 첫번째 줄에 두 수 n,m이 주어집니다. n과 m은 1보다 크거나 같고, 100보다 작거나 같은 값이 주어집니다.
#
# 출력
# 입력받은 n과 m의 곱한값을 출력합니다.
#
# 입력 예제
# 2 5
# 출력 예제
# 10

def multiplication(n, m) :

    return n * m

def main():

    data = input()

    n = int(data.split()[0])
    m = int(data.split()[1])

    print(multiplication(n, m))

if __name__ == "__main__":
    main()