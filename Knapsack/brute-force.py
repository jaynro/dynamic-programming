
def solve_knapsack_recursive(profits, weights, capacity, index):
  # base check

  if capacity <= 0 | index >=  len(profits):
    return 0

  # initialize p1
  p1=0

  # Calculate P1 if needed: 
  # If the weight of the element at current index exceeds, capacity then don;t process

  currentWeight=weights[index]
  newIndex = index +1
  if currentWeight <= capacity:
    currentProfit=profits[index]
    newCapacity =capacity - currentWeight
    p1=currentWeight +  solve_knapsack_recursive(profits,weights, newCapacity, newIndex )

  # Calculate  p2
  p2 =solve_knapsack_recursive(profits,weights, capacity, newIndex )

  #return Max
  return max (p1,p2)

def solve_knapsack(profits, weights, capacity):
  # Delegate it; first iteraction

  solve_knapsack(profits, weights, capacity, o)


  return -1

def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
