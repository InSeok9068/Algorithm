# 균형 맞추기
#
# nn개의 숫자가 주어진다. 이제 이 숫자를 두 개의 그룹으로 나눌 것이다. 예를 들어 5개의 숫자 [1, -3, 4, 5, -2] 가 주어진다면,
# 이를 두 개의 그룹으로 나누는 경우는 여러가지가 있을 수 있다. 가능한 경우로써 [1, -3], [4, 5, -2] 가 있을 수 있고,
# 또 다른 경우로는 [1, 4, -2], [-3, 5] 가 있을 수 있다.
#
# 나눈 두 그룹을 A, B라고 할 때, (A의 원소의 합) - (B의 원소의 합) 의 절댓값을 최소화 하는 프로그램을 작성하시오.
# 위의 예제에서는 A = [1, 4, -2], B = [-3, 5] 라고 하였을 때 (A의 원소의 합) - (B의 원소의 합) 의 절댓값 = |3 - 2| = 1 이며,
# 이보다 더 작은 값을 만드는 A, B는 존재하지 않는다.
#
# 입력
# 첫째 줄에 nn개의 숫자가 주어진다. (1 \leq n \leq 201≤n≤20)
#
# 출력
# (A의 원소의 합) - (B의 원소의 합) 의 절댓값의 최솟값을 출력한다.
#
# 입력 예시
# 1 -3 4 5 -2
#
# Copy
# 출력 예시
# 1

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

def makeEqual(data) :
    '''
    n개의 숫자를 두 그룹 A, B로 나눈다고 할 때,

    | (A의 원소의 합) - (B의 원소의 합) | 의 최솟값을 반환하는 함수를 작성하시오.
    '''

    combinations = powerSet(len(data))
    totalSum = sum(data)

    result = 9887698978767

    for p in combinations :
        '''
        예를 들어 원소가 5개면
        p = [1, 3]
        '''

        mySumA = 0

        for i in p :
            mySumA += data[i-1]

        mySumB = totalSum - mySumA

        result = min( result, abs(mySumA - mySumB))

    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(makeEqual(data))

if __name__ == "__main__":
    main()
