# 문제
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

# 입력
# 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

# 출력
# 직사각형의 네 번째 점의 좌표를 출력한다.

# 예제 입력 1 
# 30 20
# 10 10
# 10 20
# 예제 출력 1 
# 30 10

def makeRectangularShape(list):
    
    xList = []
    yList = []

    x = 0
    y = 0

    for i in range(len(list)):
        xList.append(list[i][0])
        yList.append(list[i][1])

    if xList[0] in xList[1:]:
        xList.remove(xList[0])
        x = xList[0]
    else:
        x = xList[0]


    if yList[0] in yList[1:]:
        yList.remove(yList[0])
        y = yList[0]
    else:
        y = yList[0]

    print(x,y)

def main():

    list = []

    for i in range(3) :
        list.append([int(x) for x in input().split()])

    makeRectangularShape(list)

if __name__ == "__main__":
    main()