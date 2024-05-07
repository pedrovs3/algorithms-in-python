def plusMinus(arr):
  arr_lenght = len(arr)
  positives = []
  negatives = []
  zeros = 0

  for number in arr:
    if number < 0:
      negatives.append(number)
    elif number > 0 :
      positives.append(number)
    else:
      zeros += 1

  return print(f'{format(len(positives) / arr_lenght, ".6f")}\n{format(len(negatives) / arr_lenght, ".6f")}\n{format(zeros / arr_lenght, ".6f")}') 

plusMinus([-4, 3, -9, 0, 4, 1])