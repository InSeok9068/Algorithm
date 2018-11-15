# 거듭제곱 구하기
#
# 본 연습문제에서는 m^n을 구하는 프로그램을 작성합니다.
#
# 만약 getPower 함수의 반환 값이 1,000,000,007 보다 클 경우, 반환 값을 1,000,000,007로 나눈 나머지 값을 반환하세요.
#
# 입력
# 첫 번째 줄에 mm과 nn이 주어집니다. (1 \leq n \leq 1,000,000,000,0001≤n≤1,000,000,000,000)
#
# 출력
# m^n을 1,000,000,007으로 나눈 나머지를 출력합니다.
#
# 입력 예시
# 3 4
#
# 출력 예시
# 81

LIMIT_NUMBER = 1000000007

def getPower(m, n):
    '''
    m^n 을 LIMIT_NUMBER로 나눈 나머지를 반환하는 함수를 작성하세요.
    '''

    return 1

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    myList = [int(v) for v in input().split()]

    print(getPower(myList[0], myList[1]))

if __name__ == "__main__":
    main()
