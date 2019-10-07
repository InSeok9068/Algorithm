
def minSort(myMap):

    minVal1 = 99999;
    minVal2 = 99999;

    newList = []

    for i in range(len(myMap)):
        for j in range(len(myMap[i])-1):
            minVal1 = myMap[i][j] - myMap[i][j+1]  

            if 
        

def main():
    n = int(input());

    myMap = []
    for i in range(n) :
        myMap.append([int(x) for x in input().split()])

    minSort(myMap)

    

if __name__ == "__main__":
    main()
