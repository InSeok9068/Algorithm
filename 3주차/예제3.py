# 합병정렬 구현
# nn개의 숫자를 합병정렬을 이용하여 정렬하는 프로그램을 작성하세요.
#
# 입력
# 첫째 줄에 nn개의 숫자가 주어진다. (1 \leq n \leq 1000001≤n≤100000)
#
# 출력
# nn개의 숫자를 오름차순으로 정렬한 결과를 출력한다.
#
# 입력 예시
# 1 5 6 2 3 8 4 9 7 10
#
# 출력 예시
# 1 2 3 4 5 6 7 8 9 10

import sys

def mergeSort(data) :
    '''
    n개의 숫자를 합병정렬을 이용하여 정렬한 결과를 list로 반환하는 함수를 작성하세요.
    '''

    result = []

    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(*mergeSort(data))

if __name__ == "__main__":
    main()
