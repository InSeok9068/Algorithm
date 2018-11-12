# 문제
# # N개의 풍선이 있다. 각 풍선 안에는 -N부터 N까지의 수가 적혀있는 종이가 들어 있다. 이 풍선들을 다음과 같은 규칙으로 터뜨린다.
# #
# # 우선, 제일 처음에는 1번 풍선을 터뜨린다. 다음에는 풍선 안에 있는 종이를 꺼내어 그 종이에 적혀있는 값만큼 이동하여 다음 풍선을 터뜨린다. 양수가 적혀 있을 경우에는 오른쪽으로,
# # 음수가 적혀 있을 때는 왼쪽으로 이동한다. 풍선은 원형으로 놓여 있다고 생각한다. 즉, 1번 풍선의 왼쪽에 N번 풍선이 있고, N번 풍선의 오른쪽에 1번 풍선이 있는 것이다. 이동할 때에는 이미 터진 풍선은 빼고 생각한다.
# #
# # 예를 들어 다섯 개의 풍선 안에 차례로 3, 2, 1, -3, -1이 적혀 있었다고 하자. 이 경우 3이 적혀 있는 1번 풍선, -3이 적혀 있는 4번 풍선, -1이 적혀 있는 5번 풍선, 1이 적혀 있는 3번 풍선,
# # 2가 적혀 있는 2번 풍선의 순서대로 터지게 된다.
# #
# # 입력
# # 첫째 줄에 자연수 N(1≤N≤1,000)이 주어진다. 다음 줄에는 차례로 각 풍선 안의 종이에 적혀 있는 수가 주어진다. 편의상 0은 적혀있지 않다고 가정하자.
# #
# # 출력
# # 첫째 줄에 터진 풍선의 번호를 차례로 나열한다.
# #
# # 예제 입력 1
# # 5
# # 3 2 1 -3 -1
# #
# # 예제 출력 1
# # 1 4 5 3 2

def ispos(string) :
    if string == '' :
        retrun False
    eliff

def bang(n, myInput):
    '''
    모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수를 리턴하는 함수를 구현하세요.
    '''

    myInputLen = len(myInput)
    input = myInput

    result = []     # 리턴 리스트
    abangVal = 0    # 터진 값
    bangVal = 0     # 터진 값
    val = 0         # 터진 위치

    for i in range(myInputLen - 1):
        if i == 0 :
            bangVal = myInput[i]                    # 터진 값을 저장
            result.append(input.index(bangVal)+1)     # 터진 위치값 저장
            val = myInput.index(bangVal)            # 터진 위치
        else :
            abangVal = myInput[val+bangVal]
            result.append(input.index(abangVal) + 1)
            myInput.remove(bangVal)
            bangVal = abangVal
            val = myInput.index(abangVal)

    return result


def main():
    '''
    수정하시면 안됩니다.
    '''
    n = int(input())
    # myInput = []
    # for _ in range(n):
    #     myInput.append(int(input()))

    myInput = [int(x) for x in input().split()]

    print(bang(n, myInput))


if __name__ == "__main__":
    main()