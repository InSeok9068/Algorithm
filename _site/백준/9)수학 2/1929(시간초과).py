# 소수 구하기
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 2 초	256 MB	43905	12424	8685	28.269%
# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000)

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

# 예제 입력 1 
# 3 16
# 예제 출력 1 
# 3
# 5
# 7
# 11
# 13

M,N = input().split()

M = int(M)
N = int(N)

for i in range(M,N+1):
    check = False
    for j in range(2,i):
        if i%j == 0:
            check = True

    if check == False:
        print(i)
