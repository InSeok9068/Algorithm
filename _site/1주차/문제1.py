# 이진수 변환
# 10진수를 2진수로 변환하여 출력하는 프로그램을 작성하세요. 단, 재귀호출을 이용하여 작성합니다.
#
# 입력
# 첫째 줄에 10진수 nn이 주어집니다. (1 \leq n \leq 1,000,0001≤n≤1,000,000)
#
# 출력
# nn을 2진수로 변환한 결과를 출력합니다.
#
# 입력 예시
# 19
# 출력 예시
# 10011

import sys
sys.setrecursionlimit(100000)

def convertBinary(n) :
    '''
    10진수 n을 2진수로 변환하여 반환합니다.

    *주의* : 변환된 2진수는 문자열이어야 합니다.

    예를 들어, 19가 입력될 경우 문자열 "10011"이 반환되어야 합니다.
    '''

    mox = 0

    if n == 1 :
        return n
    else :
        mox = n%2

    return str(convertBinary(n//2)) + str(mox)

def main():
    '''
    이 부분은 수정하지 마세요.
    '''


    n = int(input())

    print(convertBinary(n))

if __name__ == "__main__":
    main()
