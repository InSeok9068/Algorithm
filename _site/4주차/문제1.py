# Fractional knapsack
#
# nn개의 물건이 있고, 각 물건은 무게 w_i 와 가치 c_i를 갖는다.
# 이제 이 물건들을 배낭에 넣으려 한다. 이 배낭은 무게 mm까지를 버틸 수 있다.
#
# 한 가지 재미있는 사실은, 물건을 쪼갤 수 있다는 것이다. 물론, 물건을 쪼개게 되면 무게가 줄지만, 가치도 줄게 된다.
# 예를 들어, 무게를 절반으로 줄이면 가치 역시도 절반으로 줄어들게 된다.
#
# 배낭이 버틸 수 있는 무게 mm과 nn개의 물건의 정보가 주어질 때, 배낭이 담을 수 있는 가치의 최댓값을 소숫점 넷째자리에서 반올림하여 출력하는 프로그램을 작성하세요.
#
# 입력
# 첫째 줄에 물건의 개수 nn, 그리고 배낭이 버틸 수 있는 무게 mm이 주어진다. (1 \leq n \leq 100,0001≤n≤100,000) 이후 nn개의 줄에 대하여
# 각 물건의 무게 w_i, 그리고 가치 c_i가 주어진다.
#
# 출력
# 배낭이 담을 수 있는 가치의 최댓값을 소숫점 넷째자리에서 반올림하여 출력한다.
#
# 입력 예시 1
# 4 10
# 3 10
# 2 7
# 4 9
# 5 13
#
# 출력 예시 1
# 30.000
#
# 입력 예시 2
# 4 11
# 3 10
# 2 7
# 4 9
# 5 13
#
# 출력 예시 2
# 32.250

import sys

def fKnapsack(materials, m) :
    '''
    크기 m까지 버틸 수 있는 베낭이 담을 수 있는 최대 가치를 반환하는 함수를 작성하세요.

    주의 : 셋째 자리에서 반올림하는 것을 고려하지 않고 작성하셔도 됩니다.
    '''

    return 0

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    line = [int(x) for x in input().split()]

    n = line[0]
    m = line[1]

    materials = []

    for i in range(n) :
        data = [int(x) for x in input().split()]
        materials.append( (data[0], data[1]) )

    print("%.3lf" % fKnapsack(materials, m))

if __name__ == "__main__":
    main()
