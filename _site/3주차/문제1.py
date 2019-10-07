# 숫자 찾기
# nn개의 숫자 중에서, 숫자 mm이 존재하면 “Yes”, 존재하지 않으면 "No"를 반환하는 프로그램을 작성하세요.
#
# 입력
# 첫째 줄에 nn개의 숫자가 주어진다. (1 \leq n \leq 100,0001≤n≤100,000) 둘째 줄에 숫자 mm이 주어진다.
#
# 출력
# nn개의 숫자 중에서 mm이 존재하면 “Yes”, 아니면 "No"를 반환한다.
#
# 입력 예시 1
# 1 4 6 7 10 14 16
# 7
#
# 출력 예시 1
# Yes
#
# 입력 예시 2
# 1 4 6 7 10 14 16
# 9
#
# 출력 예시 2
# No

import sys

def binarySearch(data, m) :
    '''
    n개의 숫자 중에서 m이 존재하면 "Yes", 존재하지 않으면 "No"를 반환하는 함수를 작성하세요.
    '''

    if len(data) == 0 :
        return "No"

    if data[0] == m :
        return "Yes"
    else :
        return binarySearch(data[1:],m)

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]
    m = int(input())

    print(binarySearch(data, m))

if __name__ == "__main__":
    main()
