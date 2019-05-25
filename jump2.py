import sys

counter = 0
costs = [0,1,4,6,2,5,3,9,6,2,2,3,5,4,6,5,4,9]
cost = 0
mincost = 999999
minpaths = 0


def printStairPathsUtil(ansList, i, n):
    global counter
    global costs
    global cost
    global mincost
    global minpaths

    if n < 0:
        return

    if n == 0:
        ansList[i] = ""
        index = 0
        for i in ansList:

            if i != "":
                index = index + i
                sys.stdout.write(str(i) + " ")
                cost = cost + costs[index]
        print("cost is :" + str(cost))
        if cost < mincost:
            mincost = cost
            minpaths = 0
        if cost == mincost:
            minpaths = minpaths + 1
        cost = 0
        sys.stdout.write('\n')
        sys.stdout.flush()
        counter = counter + 1
        return

    ansList[i] = 1
    printStairPathsUtil(ansList, i + 1, n - 1)

    ansList[i] = 2
    printStairPathsUtil(ansList, i + 1, n - 2)

    # ansList[i] = 3
    # printStairPathsUtil(ansList, i + 1, n - 3)


def printStairPaths(n):
    ansList = [None] * (n + 1)
    printStairPathsUtil(ansList, 0, n)


n = len(costs)

printStairPaths(n - 1)
print("Number of paths is : " + str(counter))
print("Min Cost is :" + str(mincost))
print("Amount of minimum paths :" + str(minpaths))
