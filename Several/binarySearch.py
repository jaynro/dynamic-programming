
def binarySearch(listOfNumbers, target):
    # create a helper funtion to initialize left and right pointers
    return binarySearchHelper(listOfNumbers, target,0, len(listOfNumbers) -1)

def binarySearchHelper(listOfNumbers, target, left, right):

    # Base case:While left is minor or equal to right pointer

    while left <= right:
        #calculate middle index and assign potential Match
        middleIndex = (left+right) //2
        potentialMatch = listOfNumbers[middleIndex]

        # target =2
        # left =0; right =6
        # middle =3
        # [0]--[2]--[3]----[6]
        # left =0; right =2
        # 
        # If target...
            # matchs  potentialMatch        --> return true
            # Is minor than potentialMatch  --> right = middle - 1 (move to the left)
            # Is major than potentialMatch  --> left  = middle + 1 (move to the right)

        if target == potentialMatch:
            return middleIndex
        elif target < potentialMatch:
            right= middleIndex -1
        else:
            left= middleIndex +1

    return -1

def main():
    #input = "anitalavalatina"
    target = 33
    listOfNumbers = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]

    print(binarySearch(listOfNumbers, target))

main()