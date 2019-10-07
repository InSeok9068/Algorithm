# 문자열 뒤집기
# 문자열이 주어질 때, 이 문자열을 뒤집어서 출력하는 프로그램을 작성하시오. 단, 재귀호출을 이용하여 구현한다.
#
# 입력
# 첫 번째 줄에 문자열이 주어진다. 문자열의 길이는 100을 넘지 않는다.
#
# 출력
# 주어진 문자열을 뒤집어서 출력한다.
#
# 입력 예시
# Elice is so coooool
# 출력 예시
# loooooc os si ecilE

def stringReverse(myString,list1) :
    '''
    문자열 myString을 뒤집어서 반환하는 함수를 작성하세요.
    '''

    #강사코딩
    # if len(myString) <= 1 :
    #    return myString
    # else :
    #    return myString[-1] + \
    #           stringReverse(myString[1:-1]) + \
    #           myString[0]

    if myString == "" :
        myString = "".join(list1)
        return myString

    strList = list(myString)
    strListLen = len(strList)

    for i in range(strListLen) :
        if i == strListLen-1 :
            list1.append(strList[strListLen-1])

    return stringReverse(myString[:len(myString)-1],list1)

def main():
    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''

    myString = input()

    list1 = []

    print(stringReverse(myString,list1))
    # print(stringReverse(myString))
if __name__ == "__main__":
    main()