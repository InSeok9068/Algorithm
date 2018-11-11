# 순열 구하기
# 순열이란, nn개의 원소 중에서 rr개를 나열하는 것을 의미합니다. 예를 들어, 4개의 원소 중에서
# 2개를 나열한다고 하고, 우리가 갖고있는 원소가
# ‘a’, ‘b’, ‘c’, ‘d’라면, 그 순열은
# ‘ab’, ‘ac’, ‘ad’, ‘ba’, ‘bc’, ‘bd’, ‘ca’, ‘cb’, ‘cd’, ‘da’, ‘db’, dc’
# 로써 총 12개의 서로 다른 경우가 존재합니다.
#
# nn과 rr이 주어질 때, nn개의 원소 중에서 rr개를 나열한 결과를 출력하는 프로그램을 작성하세요.
# 단, 원소는 항상 'a’부터 시작하여 nn개의 알파벳이라고 가정합니다.
#
# 입력
# 첫 번째 줄에 nn과 rr이 주어집니다. (1 \leq r \leq n \leq 101≤r≤n≤10)
#
# 출력
# nn개의 원소 중에서 rr개를 나열한 결과를 출력합니다.
#
# 입력 예시
# 4 2
# 출력 예시
# ab
# ac
# ad
# ba
# bc
# bd
# ca
# cb
# cd
# da
# db
# dc

def getPermutation(n, r):
    '''
    n개의 알파벳 중에서 r개를 뽑아 나열한 결과를 리스트로 반환합니다.

    예를 들어, n = 4, r = 2 일 경우에는

    ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", dc"] 를 반환합니다.
    '''

    #힌트 2주차 예제2번을 참고

    result = []

    return result


def main():
    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''

    firstLine = [int(x) for x in input().split()]

    print('\n'.join(getPermutation(firstLine[0], firstLine[1])))


if __name__ == "__main__":
    main()
