# Source of technique concept: https://www.geeksforgeeks.org/window-sliding-technique/

def length_of_longest_substring(s):
  max_length = 0
  char_indices_map = {}
  window_beginning = 0

  for curr_index, val in enumerate(s):
    if s[curr_index] in char_indices_map:
      window_beginning = max(char_indices_map[s[curr_index]] + 1, window_beginning)
    else:
      char_indices_map[s[curr_index]] = curr_index
      max_length = max(max_length, curr_index - window_beginning + 1)

  return max_length

print(length_of_longest_substring("abcabcbb"))