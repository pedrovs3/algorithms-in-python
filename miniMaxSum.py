import functools
arr = [1,2,3,4,5]

def minMaxSum(arr):
  arr.sort()
    
  mini = functools.reduce(lambda x, y: x + y, arr[:4]) # [:4] get the four initial values of array
  maxi = functools.reduce(lambda x, y: x + y, arr[-4:]) # -4: get the last four values of array
    
  print(mini, maxi)

minMaxSum(arr)