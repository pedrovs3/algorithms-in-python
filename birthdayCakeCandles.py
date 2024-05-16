import functools

candles = [3,2,1,3]

def birthdayCakeCandles(candles):
  higherCandles = 0
  maximumVal = functools.reduce(lambda x,y: x if x>y else y, candles)

  for candle in candles:
    if candle == maximumVal:
      higherCandles += 1
  return higherCandles


print(birthdayCakeCandles(candles))
