import random


def checkIsSafe(chessboard, i, j):
    for row in range(len(chessboard)):
        for ele in range(len(chessboard[row])):
            if chessboard[row][ele] == "Q":
                jDist = abs(j - ele)
                iDist = abs(i - row)
                if i == row or j == ele or jDist == iDist:
                    return False

    return True


def heuristicFunc(chessboard, goal, i, j):
    count = 0
    for row in chessboard:
        for pos in row:
            if pos == "Q":
                count += 1
    
    return (goal - count)



if __name__ == "__main__":
    N = int(input("Enter the number of Queens: "))

    chessboard = [["-"]*N for i in range(N)] # creates a a matrix of size n*n using list of list

    while heuristicFunc(chessboard, N, -1, -1) != 0:
        chessboard = [["-"]*N for i in range(N)]

        for row in range(len(chessboard)):
            dist = -1
            i = -1
            j = -1
            resultList = []
            for element in range(len(chessboard[row])):
                if checkIsSafe(chessboard, row, element):
                    hDist = heuristicFunc(chessboard, N, row, element)
                    if dist <= hDist:
                        dist = hDist
                        i = row 
                        j = element
                        resultList.append([row, element])
            if len(resultList) > 0:
                iIdx, jIdx = resultList[random.randint(0, len(resultList)-1)]
                print("\n i index=", iIdx, "\n j index=", jIdx)
                chessboard[row][element] = "Q"
    
            for row1 in chessboard:
                print("\t", row1)
            print("Heuristic value is: ", heuristicFunc(chessboard, N, -1, -1))

    print("Heuristic value = ", heuristicFunc(chessboard, N, -1, -1))
    print()

    print("\nFollowing is the Global maxima solution for", N, "Queen Problem with heuristic distance from goal state =", heuristicFunc(chessboard, N, -1, -1), "\n\n")

    for row1 in chessboard:
        print("\t", row1)

    print("\n")

