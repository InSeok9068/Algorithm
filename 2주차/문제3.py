# 부분 문자열 개수 세기
# 두 문자열 A, B가 주어질 때 B가 A에 포함되어 있는 횟수를 출력하는 프로그램을 작성하시오. 예를 들어,
# A = “abcab” 이고 B = “ab” 이면, B는 A에 2번 포함되어 있다.
#
# 입력
# 첫째 줄이 문자열 A가 주어지고, 둘째 줄에 문자열 B가 주어진다. 각 문자열의 길이는 1000을 넘지 않는다.
#
# 출력
# B가 A에 포함되어 있는 횟수를 출력한다.
#
# 입력 예시 1
# abcab
# ab
#
# 출력 예시 1
# 2
#
# 입력 예시 2
# aaaaa
# aa
#
# 출력 예시 2
# 4

import sys

def numSubstr(A, B) :
    '''
    B가 A에 포함되어 있는 횟수를 반환하는 함수를 작성하세요.
    '''

    if A == '' :
        return 0

    if B in A[0:len(B)] :
        return 1 + numSubstr(A[1:], B)
    else :
        return numSubstr(A[1:], B)

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    A = input()
    B = input()

    print(numSubstr(A, B))

if __name__ == "__main__":
    main()
