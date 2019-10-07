# 러시아 농부의 곱셈
# 러시아 농부 혹은 고대 이집트 계산법으로 알려진 문제로 주어진 두 수의 곱을 구하는 재귀함수를 작성해 봅니다.
#
# 문제
# 두 수 n,m이 주어집니다.
#
# n은 두배를 하고, m은 2로 나눠줍니다
#
# m이 1이 되면 종료한다.
#
# 이때, m이 홀수인 경우의 n의 총합을 구한다.
#
# 입력
# 첫번째 줄에 n과 m이 주어집니다. n과 m은 1보다 크거나 같고 1000보다 작거나 같은 값이 주어진다.
#
# 출력
# 입력된 n과 m의 곱한값을 출력한다.
#
# 입력 예제
# 123 12
# 출력 예제
# 1476

def farmerMultiplication(n, m) :

    nVal = n * 2
    mVal = m // 2
    xVal = mVal % 2

    if mVal == 1 :
        return nVal

    if xVal == 0 :
        return farmerMultiplication(nVal, mVal)
    else :
        return nVal + farmerMultiplication(nVal, mVal)

def main():

    data = input()

    n = int(data.split()[0])
    m = int(data.split()[1])

    print(farmerMultiplication(n, m))

if __name__ == "__main__":
    main()