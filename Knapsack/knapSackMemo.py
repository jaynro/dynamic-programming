import numpy as np

def solve_knapsack(profits, weights, capacity):
  # create a two dimensional array for Memoization, each element is initialized to '-1'
  # Capacity Index matrix
  dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]

  return knapsack_recursive(dp, profits, weights, capacity, 0,"Init")


def knapsack_recursive(dp, profits, weights, capacity, currentIndex,trace):
    print(" trace: ", trace, "****** ENTER ******** knapsack_recursive  currentIndex= ",currentIndex, ",  capacity= ",capacity )

    # base checks
    if capacity <= 0 or currentIndex >= len(profits):
        print(" trace: ", trace,"                         --BASE CASE No more capacity!!! ")
        return 0
    # if we have already solved a similar problem, return the result from memory
    if dp[currentIndex][capacity] != -1:
        print(" trace: ", trace,"                         -----I have it!! ")
        return dp[currentIndex][capacity]

  # recursive call after choosing the element at the currentIndex
  # if the weight of the element at currentIndex exceeds the capacity, we
  # shouldn't process this
    profit1 = 0
    if weights[currentIndex] <= capacity:
        print(" trace: ", trace,"                         new recursive call LEG 1 ************** ----------- New profit " ,profits[currentIndex] ,"There is Capacity  [index: ",currentIndex+1, " , NEW capacity: ", capacity - weights[currentIndex], " ] : " ,dp[currentIndex][capacity]," ")
        profit1 = profits[currentIndex] + knapsack_recursive(
        dp, profits, weights, capacity - weights[currentIndex], currentIndex + 1,trace+"-A")
    else:
        print(" trace: ", trace,"                         new recursive call LEG 1 ************** -----------NO MORE Capacity  [index: ",currentIndex+1, " , NEW capacity: ", capacity - weights[currentIndex], " ] : " ,dp[currentIndex][capacity]," ")

    # recursive call after excluding the element at the currentIndex
    print(" trace: ", trace,"                         new recursive call LEG 2 ************** -----------There is Capacity  [index: ",currentIndex+1, " , capacity: ", capacity, " ] : " ,dp[currentIndex][capacity]," ", " trace: ", trace)
    profit2 = knapsack_recursive(
        dp, profits, weights, capacity, currentIndex + 1,trace+"-B")
  
    dp[currentIndex][capacity] = max(profit1, profit2)

    print(" trace: ", trace,"****** EXIT ********","  profit at  [",currentIndex, " , ", capacity, " ] : " ,dp[currentIndex][capacity])
    print(" trace: ", trace,"****** EXIT ********","  Max  (profit1= ",profit1, " profit2= ",profit2, ") = ", dp[currentIndex][capacity] )
    #dp2= np.asarray(dp)
    #print(dp2)
    return dp[currentIndex][capacity]
  

def main():
    #print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    #print(solve_knapsack([5, 4, 3 ], [1, 2, 3 ], 4))
    print(solve_knapsack([ 4, 3 ], [ 2, 3 ], 5))

main()
