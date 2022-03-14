from operator import le


def isPalindrome1(input):
    
    reverseInput =""
    #create a new variable with the string reversed and compare
    
    ####print([input[x] for x in range(len(input))]) 

    # reversed iterates tje items in ragnge backwards
    # then store it
    for i in reversed(range(len(input))):
        reverseInput += input[i]

    return input== reverseInput

def isPalindrome2(input):
    leftIdx =0
    rightIdx = len(input) -1
    # Declare 2 indices at the begining and the end

    #iterate whilhe they don't meet or they are different
    while leftIdx < rightIdx:
        if input[leftIdx] != input[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -=1
    return True    

def main():
    #input = "anitalavalatina"
    input = "anna"
    print(isPalindrome1(input))
    print(isPalindrome2(input))

main()