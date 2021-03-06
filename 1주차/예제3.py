# 올바른 괄호인지 판단하기
#
# 본 문제에서는 입력으로 주어지는 괄호가 올바른 괄호인지를 판단하는 프로그램을 작성합니다.
#
# 예를 들어, ‘(())’ 은 올바른 괄호이지만, ‘(()))’, 혹은 ‘(()()(’ 는 올바른 괄호가 아닙니다.
#
# 입력
# 괄호 pp가 주어집니다.
#
# 출력
# pp가 올바른 괄호이면 YES, 그렇지 않으면 NO를 출력합니다.
#
# 입력 예시 1
# (())()
# 출력 예시 1
# YES
# 입력 예시 2
# (((())())(()())((())()))
# 출력 예시 2
# YES
# 입력 예시 3
# (())())()
# 출력 예시 3
# NO
# 입력 예시 4
# ((()())(()())))(())
# 출력 예시 4
# NO

def checkParen(p):
    '''
    괄호 문자열 p의 쌍이 맞으면 "YES", 아니면  "NO"를 반환
    '''

    if len(p) <= 1:
        if len(p) == 0:
            return "YES"
        else:
            return "NO"
    elif p == "()":
        return "YES"

    for i in range(len(p) - 1):
        if p[i] == '(' and p[i + 1] == ')':
            q = p[:i] + p[i + 2:]

            return checkParen(q)

    return "NO"


def main():
    '''
    Do not change this code
    '''

    x = input()
    print(checkParen(x))


if __name__ == "__main__":
    main()


