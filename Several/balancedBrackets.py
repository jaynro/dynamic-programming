def balancedBrackets(input):
    #declare
    openingBrackets = "([{"
    closingBrackets = ")]}"
    matchingBrackets ={")":"(", "]":"[",  "}":"{" }

    stack = []

    #iterate input
    for char in input:
        #if we have an "openning bracket", lets ADD it to  the stack
        if char in openingBrackets:
            stack.append(char)
        #if is in "closingBrackets" not, we might have certains validations    
        elif char in closingBrackets:
            # If stack is empty is imbalanced
            if len(stack) == 0:
                return False
            #if last element of the stach is a matching bracker POP it    
            if stack[-1] == matchingBrackets[char]:
                stack.pop()
            else:
                return False            
    return len(stack) == 0


def main():
    print(balancedBrackets("[{(a+b)(a)[({})]}]"))

main()    