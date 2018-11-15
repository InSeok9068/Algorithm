# Inversion counting
# nn개의 숫자의 리스트 A가 주어질 때, inversion은 다음과 같이 정의된다.
#
# 만약 i < j 이고, A[i] > A[j]라면 A[i]와 A[j]는 inversion 관계이다.
#
# 예를 들어, A = [1, 4, 3, 2] 일 경우, 총 3개의 inversion이 존재하는데, 이는 그 값들을 나열해보면 (4, 3), (4, 2), (3, 2) 이다.
#
# nn개의 숫자가 주어질 때, inversion 관계인 숫자 쌍의 개수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 nn개의 숫자가 주어진다. (1 \leq n \leq 100,0001≤n≤100,000)
#
# 출력
# Inversion의 개수를 출력한다.
#
# 입력 예시
# 1 4 3 2
#
# 출력 예시
# 3

import sys

def inversionCount(data) :
    '''
    n개의 숫자가 list로 주어질 때, inversion 관계에 있는 숫자 쌍의 개수를 반환하는 함수를 작성하세요.
    '''

    return 0

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(inversionCount(data))

if __name__ == "__main__":
    main()
