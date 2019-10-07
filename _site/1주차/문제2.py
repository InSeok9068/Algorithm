# 문자열 포함 관계 조사
# 두 문자열 A, B가 주어질 때, A의 모든 알파벳이 문자열 B에 존재하는지 판별하는 프로그램을 작성하세요. 예를 들어, A = “mef” 이고,
# B = “myself” 라면 A의 모든 알파벳이 B에 존재합니다. 하지만 A = “abca”, B = “acf” 일 경우에는 A의 모든 알파벳이 B에 존재하지 않습니다.
# 재귀호출을 이용하여 작성하도록 합니다.
#
# 입력
# 첫째 줄에는 문자열 A가 주어집니다. 두 번째 줄에는 문자열 B가 주어집니다. 문자열의 길이는 100을 넘지 않습니다.
#
# 출력
# 문자열 A의 모든 알파벳이 문자열 B에 존재한다면 Yes, 아니면 No를 출력하는 프로그램을 작성하세요.
#
# 입력 예시 1
# mef
# myself
# 출력 예시 1
# Yes
# 입력 예시 2
# abca
# acf
# 출력 예시 2
# No

import sys

sys.setrecursionlimit(100000)

def strContain(A, B):
    '''
    문자열 A의 알파벳이 문자열 B에 모두 포함되어 있으면 "Yes", 아니면 "No"를 반환합니다.
    '''

    # 강사 코딩
    # if len(A) <= 0 :
    #     return "Yes"
    # if A[0] in B :
    #     return strContain(A[1:],B)
    # else :
    #     return "No"

    aList = list(A)
    aListLen = len(aList)
    bList = list(B)
    isTrue = False

    if A == "" :
        return "Yes"

    for i in range(aListLen) :
        if aList[0] in bList :
            isTrue = True
            del aList[0]
            A = "".join(aList)

            return strContain(A, B)

    if bool(isTrue) == False :
        return "No"

def main():
    '''
    Do not change this code
    '''

    A = input()
    B = input()

    print(strContain(A, B))


if __name__ == "__main__":
    main()
