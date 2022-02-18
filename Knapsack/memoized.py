
def solve_knapsack_memo(dp,profits, weights, capacity, index):
  # base check

  if capacity <= 0 or index >=  len(profits):
    return 0

  #If we have it, return it
  if dp[capacity, index] != -1:
    return dp[capacity, index]   

  # initialize p1
  p1=0

  # Calculate P1 if needed: 
  # If the weight of the element at current index exceeds, 
  # capacity then don't process

  currentWeight=weights[index]
  newIndex = index +1
  
  if currentWeight <= capacity:
    currentProfit=profits[index]
    newCapacity =capacity - currentWeight
    p1=currentProfit +  solve_knapsack_recursive(profits,weights, newCapacity, newIndex )

  # Calculate  p2
  p2 =solve_knapsack_recursive(profits,weights, capacity, newIndex )

  #store it
  result = max (p1,p2)
  dp[capacity, index] = result
  #return Max
 
  return result

def solve_knapsack(profits, weights, capacity):

  #initialize array
  dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
  # Delegate it; first iteraction

  return solve_knapsack_memo(dpprofits, weights, capacity, 0)


def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
