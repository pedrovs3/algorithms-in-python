# s is time in 12h format
import datetime

def timeConversion(s):
  formatIdentifier = s[-2:]
  hours = s[:len(s) - 2]

  hour, minute, second = hours.split(":")
  
  if formatIdentifier == "PM":
    hour = str(int(hour) + 12) if hour != "12" else "12"
    
  else:
    hour = str(int(hour) - 12) if hour != "12" else "00"

  converted_time = f"{hour}:{minute}:{second}"
  return converted_time


print(timeConversion("07:05:45PM"))
