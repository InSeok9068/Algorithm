# 멱집합 구하기
#
# 집합 A에 다하여, A의 모든 부분집합을 원소로 가지는 집합을 A의 멱집합이라고 한다.
# 예를 들어, 집합 A의 원소가 {1, 2, 3} 일 경우, A의 멱집합은 다음과 같이 8개의 원소를 갖는 집합이다.
#
# {}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}
#
# 집합 A의 원소는 1부터 nn까지의 자연수로 구성된다. nn이 주어질 때, A의 멱집합의 원소를 사전 순서대로 모두 출력하는 프로그램을 작성하시오.
# 단, 공집합은 제외하고 출력한다.
#
# 입력
# 첫째 줄에 원소의 개수 nn이 주어진다. (1 \leq n \leq 101≤n≤10)
#
# 출력
# A의 멱집합의 원소를 사전 순서대로 모두 출력한다. 단, 공집합은 제외하고 출력한다.
#
# 입력 예시
# 3
#
# Copy
# 출력 예시
# 1
# 1 2
# 1 2 3
# 1 3
# 2
# 2 3
# 3

import sys

def getPowerSet(n,k):
    '''
    n개의 원소가 있고, k를 가장 처음으로
    선택하는 경우의 멱집합 반환

    getPowerSet(3,2) = [ [2], [2, 3] ]
    '''

    if n == k :
        return [ [n] ]
    else :
        '''
        result = [ [1] ]
        temp = [ [2], [2,3], [3] ]
        '''
        result = [ [k] ]
        temp = []

        for i in range(k+1, n+1) :
            temp = temp + getPowerSet(n, i)

        for i in range(len(temp)) :
            temp[i] = [k] + temp[i]

        return result + temp

def powerSet(n):
    '''
    n개의 원소를 가지는 집합 A의 멱집합의 원소를 사전 순서대로 list로 반환하는 함수를 작성하시오.

    예를 들어, n = 3 일 경우 다음의 list를 반환한다.

    [ [1], [1, 2], [1, 3], [1, 2, 3], [2], [2, 3], [3] ]
    '''

    result = []

    for i in range(1, n+1) :
        result = result + getPowerSet(n, i)

    return result

    return []


def main():
    '''
    이 부분은 수정하지 마세요.
    재귀가 필요함!!
    '''

    n = int(input())

    result = powerSet(n)

    for line in result:
        print(*line)


if __name__ == "__main__":
    main()
