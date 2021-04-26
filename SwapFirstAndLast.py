def SwapFirstAndLast() :
    # Swap function
    def swapList(newList):
        newList[0], newList[-1] = newList[-1], newList[0]

        return newList

    # Driver code
    newList = [12, 35, 9, 56, 24]
    print(swapList(newList))

if __name__ == '__main__':
    SwapFirstAndLast()
