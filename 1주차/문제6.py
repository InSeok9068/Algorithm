# 가로수
# 직선으로 되어있는 도로의 한 편에 가로수가 임의의 간격으로 심어져있습니다.
# KOI 시에서는 가로수들이 모두 같은 간격이 되도록 가로수를 추가로 심는 사업을 추진하고 있습니다.
# KOI 시에서는 예산문제로 가능한 한 가장 적은 수의 나무를 심고 싶습니다.
#
# 편의상 가로수의 위치는 기준점으로 부터 떨어져 있는 거리로 표현되며, 가로수의 위치는 모두 양의 정수입니다.
#
# 예를 들어, 가로수가 (1, 3, 7, 13)의 위치에 있다면 (5, 9, 11)의 위치에 가로수를 더 심으면 모든 가로수들의 간격이 같게 됩니다.
# 또한, 가로수가 (2, 6, 12, 18)에 있다면 (4, 8, 10, 14, 16)에 가로수를 더 심어야 합니다.
#
# 심어져 있는 가로수의 위치가 주어질 때, 모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수를 구하는 프로그램을 작성하세요.
# 단, 추가되는 나무는 기존의 나무들 사이에만 심을 수 있습니다.
#
# 입력
# 첫째 줄에는 이미 심어져 있는 가로수의 수를 나타내는 하나의 정수 NN이 주어진다(3≤NN≤100,000).
# 둘째 줄부터 NN개의 줄에는 각 줄마다 심어져 있는 가로수의 위치가 양의 정수로 주어지며,
# 가로수의 위치를 나타내는 정수는 100,000,000 이하이다. 가로수의 위치를 나타내는 정수는 모두 다르다.
#
# 출력
# 모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수를 첫 번째 줄에 출력합니다.
#
# 입력 예시
# 4
# 1
# 3
# 7
# 13
# 출력 예시
# 3

def howManyTree(n, myInput):
    '''
    모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수를 리턴하는 함수를 구현하세요.
    '''

    myInput.sort()
    sortListLen = len(myInput)

    smallValue = 0

    for i in range(sortListLen-1) :
        if i == 0 :
            smallValue = myInput[i + 1] - myInput[i]
        else :
            if smallValue > myInput[i + 1] - myInput[i] :
                smallValue = myInput[i + 1] - myInput[i]

    for i in range(sortListLen-1) :
        if smallValue != myInput[i + 1] - myInput[i] :
            myInput.insert(i+1, myInput[i]+smallValue)
            return 1 + howManyTree(n,myInput)

    return 0

def main():
    '''
    수정하시면 안됩니다.
    '''
    n = int(input())
    myInput = []
    for _ in range(n):
        myInput.append(int(input()))

    print(howManyTree(n, myInput))


if __name__ == "__main__":
    main()
