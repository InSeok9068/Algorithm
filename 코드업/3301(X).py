# 문제 설명    
# 어떤 가게의 욕심쟁이 점원은 거스름돈을 나눠줄때 거스름돈의 개수를 적게해서 주고자 한다.

# 거스름돈을 입력 받아 점원이 줄 수 있는 최소 거스름돈의 개수를 출력하시오.

# 예를 들어 54520원인 경우,

# 거스름돈으로 50000원권 1장, 1000원권 4장, 500원 1개, 10원 2개 해서 총 8개이다.

# (※ 현재 우리나라가 사용하고 있는 화폐를 사용한다. 10원 50원 100원 500원 1,000원 5,000원 10,000원 50,000원)

# 입력
# 거스름돈 n이 입력된다. ( n은10이상의  int 범위 )

# 출력
# 최소 거스름돈의 개수를 출력한다.

# 입력 예시   
# 54520

# 출력 예시
# 8

# 도움말

import sys

def calculationOfChange(money,moneylist):

    if money == 0:
        return 0
    
    if money >= moneylist[0] :
        money = money - moneylist[0]
        
        return 1+ calculationOfChange(money,moneylist[0:])
    else :
        return calculationOfChange(money,moneylist[1:])

def main():

    money = int(input())

    moneylist = [50000,10000,5000,1000,500,100,50,10]

    print(calculationOfChange(money,moneylist))

if __name__ == "__main__":
    main()
