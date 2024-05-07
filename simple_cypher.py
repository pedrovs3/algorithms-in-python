import re
regex_test = re.compile('[^0-9a-zA-Z]+')
lower_alphabet = list(map(chr, range(97, 123)))
upper_alphabet = list(map(chr, range(65, 91)))

def circular_array(arr, index): 
  return arr[index % len(arr)]

def caesar_cipher(text, k):
  encrypted = ""

  for letter in text:
    if not regex_test.search(letter) and not letter.isdigit():
      if letter.isupper():
        encrypted += circular_array(upper_alphabet, upper_alphabet.index(letter) + k)
      else:
        encrypted += circular_array(lower_alphabet, lower_alphabet.index(letter) + k)
    else: 
      encrypted += letter
  return encrypted

cleartext = "1X7T4VrCs23k4vv08D6yQ3S19G4rVP188M9ahuxB6j1tMGZs1m10ey7eUj62WV2exLT4C83zl7Q80M"
k = 27

print(caesar_cipher(cleartext, k))


# Expected Output:
# 1Y7U4WsDt23l4ww08E6zR3T19H4sWQ188N9bivyC6k1uNHAt1n10fz7fVk62XW2fyMU4D83am7R80N