# 회의실 준비 (Big)
#
# 엘리스씨는 보다 더 나은 서비스를 제공하기 위하여 정기적인 회의를 하는 것을 선호하는 편이다.
# 여기서 엘리스씨의 역할은 nn개의 회의가 언제 시작하는지, 그리고 언제 끝나는지를 모두 모으고,
# 그 이후 각 회의가 어느 장소에서 이루어져야 하는지를 정한다. 각 회의가 시작하는 시간, 그리고 끝나는 시간은 초단위로 주어진다고 하자.
# 예를 들어, 하나의 회의는 10초에 시작하여 99초에 끝날 수 있다.
#
# 당연하게도, 두 개의 회의가 시간이 겹칠 경우에는 같은 회의실을 사용할 수 없다. 또한, 만약 정확히 10초에 끝나는 회의가 있고,
# 또 다른 회의가 정확히 10초에 시작한다면, 이 두 회의는 같은 회의실을 사용할 수 있다.
#
# 회의실을 빌리는 데에는 돈이 들기 때문에, 엘리스씨는 가능한한 적은 수의 회의실을 준비하고자 한다. nn개의 회의에 대한 정보가 주어질 때,
# 모든 회의가 이루어지기 위하여 빌려야 하는 회의실의 최소 개수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 회의실의 개수 nn이 주어진다. (1 \leq n \leq 100,0001≤n≤100,000) 이후 각 회의에 대하여 회의가 시작하는 시간,
# 그리고 끝나는 시간이 주어진다. 이 시간은 정수로 주어진다.
#
# 출력
# 엘리스씨가 예약을 해야 하는 최소 회의실의 개수를 출력한다.
#
# 입력 예시 1
# 4
# 1 4
# 3 5
# 2 7
# 4 6
#
# 출력 예시 1
# 3

import sys


def reservation(meetingList):
    '''
    회의 일정이 list로 주어질 때, 엘리스씨가 준비해야 하는 회의실의 수의 최솟값을 반환하는 함수를 작성하세요.

    각 일정은 tuple로 주어진다. 예를 들어, 주어진 입력의 경우 다음과 같이 저장된다.

    meetingList[0] = (1, 4)
    meetingList[1] = (3, 5)
    meetingList[2] = (2, 7)
    meetingList[3] = (4, 6)
    '''

    return 0


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())
    meetingList = []

    for i in range(n):
        data = [int(x) for x in input().split()]
        meetingList.append((data[0], data[1]))

    print(reservation(meetingList))


if __name__ == "__main__":
    main()
