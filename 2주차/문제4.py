import sys

def sqrt(A,B) :
    return pow((A[0] - B[0]),2) + pow((A[1] - B[1]),2)

def getDist(points) :
    '''
    n개의 점이 주어질 때, 가장 가까운 두 점 사이의 거리의 제곱을 반환하는 함수를 작성하세요.

    예를 들어, 점이 4개가 있고, 각각의 좌표가 (0, 3), (1, 1), (2, 2), (7, 1) 이라면 points에는 다음과 같이 그 정보가 저장됩니다.

    points = [ (0, 3), (1, 1), (2, 2), (7, 1) ]

    이 때, 가장 가까운 두 점 사이의 거리의 제곱은 2입니다.
    '''

    points1 = []
    result = 999999999999999999999

    for i in range(len(points)-1) :
        points1 = points[i+1:]
        for j in range(len(points1)) :
            result = min(result, sqrt(points[i], points1[j]))

    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())
    points = []

    for i in range(n) :
        line = [int(x) for x in input().split()]
        points.append( (line[0], line[1]) )

    print(getDist(points))

if __name__ == "__main__":
    main()
