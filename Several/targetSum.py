
def targetSum1(nums, target):
    print("targetSum (Square solutions): nums:", nums," target:", target)

 #   for i in range(len(nums) - 1):
 #       print("nums[",i,"]=",nums[i])

    for num in nums:
        print("num: ",num)
        #for j in nums:
        for numS in range(num +1, len(nums)):
            num2 =nums[numS]
            print("num2: ",num2)
            if num + num2 == target:
                print("There is a match :" ,num," , ",num2)
                return [num,num2]
        

    return

def targetSum2(nums, target):
    print("targetSum (n solution): nums:", nums," target:", target)
    numsMap ={}

    for num in nums:
        potentialMatch = target - num
        if potentialMatch in numsMap:
            return [potentialMatch, num]
        else:
            numsMap[num] = True    

    return []

def main():
    nums=[3,5,-4,8,11,1,-1,6]
    print(targetSum1( nums,10))
    #print(targetSum2( nums,10))
    

main()