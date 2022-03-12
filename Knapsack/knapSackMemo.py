import numpy as np

def solve_knapsack(profits, weights, capacity):
  # create a two dimensional array for Memoization, each element is initialized to '-1'
  # Capacity Index matrix

  m=[[1,2,3],[4,5,6],[7,8,9]]
  print (m)

  oneTo9 = [x for x in range(1,10)]
  n=[oneTo9 for y in range(3)]
  print (n)





  print("profits: ", profits)
  print("weights: ", weights)
  print("Capacity: ", capacity)
  print("len(profits): " ,len(profits))
  a1 =  ["-1" for x in range(capacity+1)]
  print("a1: ")
  print(a1)
  dp = [
      a1
      #[-1 for x in range(capacity+1)] 
      for y in range(len(weights))
      ]

  print ("dp: ")
  print (dp)
  dp2 = np.array(dp)
  print (dp2)
  return knapsack_recursive(dp, profits, weights, capacity, 0)


def knapsack_recursive(dp, profits, weights, capacity, currentIndex):
    return
def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))

main()