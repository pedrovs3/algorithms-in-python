def getRatio(num, arr_len):
  return format(num / arr_len, ".6f")

def plusMinus(arr):
  arr_lenght = len(arr)
  positives = negatives = zeros = 0

  for number in arr:
    if number < 0:
      negatives += 1
    elif number > 0 :
      positives += 1
    else:
      zeros += 1

  positive_ratio = getRatio(positives, arr_lenght)
  negative_ratio = getRatio(negatives, arr_lenght)
  zeros_ratio = getRatio(zeros, arr_lenght)

  return f"{positive_ratio}\n{negative_ratio}\n{zeros_ratio}"

print(plusMinus([-4, 3, -9, 0, 4, 1]))