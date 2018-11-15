# 가장 가까운 값 찾기
#
# 오름차순으로 정렬된 nn개의 숫자가 주어지고, 정수 mm이 주어질 때, nn개의 숫자 중에서 mm과 가장 가까운 숫자를 출력하는 프로그램을 작성하시오.
# 만약 가장 가까운 숫자가 2개 이상이라면, 그 중 가장 작은 숫자를 출력한다.
#
# 입력
# 첫째 줄에 nn개의 숫자가 주어진다. (1 \leq n \leq 100,0001≤n≤100,000) 둘째 줄에 숫자 mm이 주어진다.
#
# 출력
# nn개의 숫자 중에서 mm과 가장 가까운 숫자를 출력한다. 만약 가장 가까운 숫자가 2개 이상일 경우, 그 중 가장 작은 값을 출력한다.
#
# 입력 예시 1
# 1 4 6 7 10 14 16
# 8
#
# 출력 예시 1
# 7
#
# 입력 예시 2
# 1 4 6 7 10 14 16
# 12
#
# 출력 예시 2
# 10

import sys

def getNearest(data, m) :
    '''
    n개의 숫자가 list로 주어지고, 숫자 m이 주어질 때, n개의 숫자 중에서 m과 가장 가까운 숫자를 반환하는 함수를 작성하세요.
    '''

    return 0

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]
    m = int(input())

    print(getNearest(data, m))

if __name__ == "__main__":
    main()
