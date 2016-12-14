#Problem 1 - hello_name
def hello_name(name):
  """
  Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
  """
  return "Hello " + name + "!"

#Problem 2 - make_abba
def make_abba(a, b):
  """
  Given two strings, a and b, return the result of putting them together in 
  the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
  """
  return a + b + b + a

#Problem 3 - make_tags
def make_tags(tag, word):
  """
  The web is built with HTML strings like "<i>Yay</i>" which draws 
  Yay as italic text. In this example, the "i" tag makes <i> and </i> 
  which surround the word "Yay". Given tag and word strings, create the 
  HTML string with tags around the word, e.g. "<i>Yay</i>".
  """
  return "<" + tag + ">" + word + "</" + tag + ">"

#Problem 4 - make_out_word
def make_out_word(out, word):
  """
  Given an "out" string length 4, such as "<<>>", and a word, 
  return a new string where the word is in the middle of the 
  out string, e.g. "<<word>>".
  """
  return out[:2] + word + out[2:]

#Problem 5 - extra_end
def extra_end(str):
  """
  Given a string, return a new string made of 3 copies of the last 2 
  chars of the original string. The string length will be at least 2.
  """
  return str[-2:]*3

#Problem 6 - first_two
def first_two(str):
  """
  Given a string, return the string made of its first two chars, 
  so the String "Hello" yields "He". If the string is shorter than 
  length 2, return whatever there is, so "X" yields "X", and the 
  empty string "" yields the empty string "".
  """
  if len(str) > 2:
    return str[:2]
  return str

#Problem 7 - first_half
def first_half(str):
  """
  Given a string of even length, return the first half. 
  So the string "WooHoo" yields "Woo".
  """
  return str[:len(str)//2]

#Problem 8 - without_end
def without_end(str):
  """
  Given a string, return a version without the first and last char, 
  so "Hello" yields "ell". The string length will be at least 2.
  """
  return str[1:-1]

#Problem 9 - 