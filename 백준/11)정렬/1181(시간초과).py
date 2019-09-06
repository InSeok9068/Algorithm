# 문제
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 입력
# 첫째 줄에 단어의 개수 N이 주어진다. (1≤N≤20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

# 출력
# 조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.

# 예제 입력 1 
# 13
# but
# i
# wont
# hesitate
# no
# more
# no
# more
# it
# cannot
# wait
# im
# yours
# 예제 출력 1 
# i
# im
# it
# no
# but
# more
# wait
# wont
# yours
# cannot
# hesitate

# n = int(input())

# wordList = []

# for i in range(n):
#     wordList.append(input())

# wordList = list(set(wordList))

# for i in range(len(wordList)-1):
#     for j in range(len(wordList)-(1+i)):
#         if len(wordList[j]) == len(wordList[j+1]):
#             if wordList[j] > wordList[j+1]:
#                 word = wordList[j]
#                 wordList[j] = wordList[j+1]
#                 wordList[j+1] = word
#         elif len(wordList[j]) > len(wordList[j+1]):
#             word = wordList[j]
#             wordList[j] = wordList[j+1]
#             wordList[j+1] = word

# for word in wordList:
#     print(word)

voca_list = []
for i in range(int(input())):               # 테스트케이스 수 입력
    voca_list.append(input())               # 입력하는 단어를 리스트로 저장
 
set_voca_list = list(set(voca_list))        # 리스트의 중복 제거
 
sort_voca_list = []
 
for j in set_voca_list:
    sort_voca_list.append((len(j), j))      # 단어의 길이와 단어를 같이 리스트화 시켜 저장
 
sort_voca_list.sort()                       # sort()는 len(j), j 에서 앞을 먼저 정렬후에 앞의 조건이 일치하면 뒤를 정렬한다.
 
for len_voca, voca in sort_voca_list:       # 리스트를 순환시켜 순서대로 출력
    print(voca)


