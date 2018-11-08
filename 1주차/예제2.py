# quick sort
#
# quick sort를 구현하는 프로그램을 작성하세요.
#
# 입력
# 첫 번째 줄에 nn개의 숫자가 주어집니다.
#
# 출력
# 오름차순으로 정렬된 결과를 출력합니다.
#
# 입력 예시
# 10 2 3 4 5 6 9 7 8 1
# 출력 예시
# 1 2 3 4 5 6 7 8 9 10

def getSmallElements(array, pivot):

    result = []

    for x in array :
        if pivot >= x :
            result.append(x)

    return result

def getLargeElements(array, pivot):

    result = []

    for x in array :
        if pivot < x :
            result.append(x)

    return result

    return array
def quickSort(array):

    if len(array) <= 1 :
        return array

    pivot = array[0]

    left = getSmallElements(array[1:],pivot)
    right = getLargeElements(array[1:],pivot)

    left = quickSort(left)  #작거나 같은 원수들
    right = quickSort(right)  #큰 원수들

    return left + [pivot] + right

def main():
    line = [int(x) for x in input().split()]

    print(*quickSort(line))

if __name__ == "__main__":
    main()
