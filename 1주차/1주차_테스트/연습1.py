# 덧셈
# 재귀 연습을 위하여 덧셈을 하는 재귀 함수를 백지에서 작성해봅니다.
#
# 문제
# 입력 n이 주어졌을 때, 1부터 n까지의 총합을 구하는 프로그램을 재귀로 작성해봅니다.
#
# 입력
# 첫번째 줄에 입력 n이 주어집니다. n은 1보다 크거나 같고, 100보다 작거나 같은 값이 주어집니다.
#
# 출력
# 1부터 n까지의 총합을 출력합니다.
#
# 입력 예제
# 10
# 출력 예제
# 55

def sum(n) :

    if n == 0 :
        return 0
    else :
        return n + sum(n-1)

def main():

    n = int(input())

    print(sum(n))

if __name__ == "__main__":
    main()