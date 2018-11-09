# 각 자릿수의 차이
# # 두 자연수가 주어질 때, 각 자릿수의 숫자를 비교하여 다른 개수를 세는 프로그램을 작성하시오.
# #
# # 예를 들어, 두 자연수가 각각 212, 233 이라면 10의 자리와 1의 자리가 다르므로, 총 2개의 자리가 다르다.
# #
# # 입력
# # 첫 번째 줄과 두 번째 줄에 각각 자연수가 주어진다.
# #
# # 출력
# # 각 자릿수의 숫자를 비교하여, 다른 자리수의 개수를 출력한다.
# #
# # 입력 예시 1
# # 212
# # 233
# #
# # 출력 예시 1
# # 2
# #
# # 입력 예시 2
# # 123
# # 123456
# #
# # 출력 예시 2
# # 6

def diffDigit(a, b) :
    '''
    a, b의 서로 다른 자리수의 개수를 반환한다
    '''

    '''
    1. 둘의 길이의 차이를 구하고
    2. 차이수 만큼 자릿수에 ""로 채워줌
    3. 큰 길이를 구해 for문으로 자릿수 하나씩 비교하여 
    4. result에 쌓아줌
    '''
    # aList = list(str(a))
    # bList = list(str(b))
    # aListLen = len(aList)
    # bListLen = len(bList)
    # minLen = min(aListLen, bListLen)
    # result = 0
    #
    # for i in range(minLen-1) :
    #     if aList[(minLen-1)-i] != bList[(minLen-1)-i] :
    #         result += 1
    #
    # return result;

def main():
    '''
    Do not change this code
    '''

    a = int(input())
    b = int(input())

    print(diffDigit(a, b))


if __name__ == "__main__":
    main()
