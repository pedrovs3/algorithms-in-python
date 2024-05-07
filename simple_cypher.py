import re

NON_ALPHANUMERIC_PATTERN = re.compile('[^0-9a-zA-Z]+')
LOWER_ALPHABET = list(map(chr, range(97, 123)))
UPPER_ALPHABET = list(map(chr, range(65, 91)))

def generate_caesar_cipher_map(shift): 
  cipher_map = {}

  for char in LOWER_ALPHABET:
    cipher_map[char] = LOWER_ALPHABET[(LOWER_ALPHABET.index(char) + shift) % 26]
  for char in UPPER_ALPHABET:
    cipher_map[char] = UPPER_ALPHABET[(UPPER_ALPHABET.index(char) + shift) % 26]
  return cipher_map

def caesar_cipher(text, k):
  cipher_map = generate_caesar_cipher_map(k)
  encrypted = ""

  for letter in text:
   if not NON_ALPHANUMERIC_PATTERN.search(letter):
     encrypted += cipher_map.get(letter, letter)
   else:
     encrypted += letter
  return encrypted

cleartext = "1X7T4VrCs23k4vv08D6yQ3S19G4rVP188M9ahuxB6j1tMGZs1m10ey7eUj62WV2exLT4C83zl7Q80M"
k = 27

print(caesar_cipher(cleartext, k))


# Expected Output:
# 1Y7U4WsDt23l4ww08E6zR3T19H4sWQ188N9bivyC6k1uNHAt1n10fz7fVk62XW2fyMU4D83am7R80N