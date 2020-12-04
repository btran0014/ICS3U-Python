word1=input("Enter a word: ")
word2=input("Enter another word: ")
if word1>word2:
  print (f"{word2} appears first alphabetically")
  print (f"{word1} appears after ")
elif word2>word1:
  print(f"{word1} appears first alphabetically")
  print(f"{word2} appears after alphabetically")
else:
  print(f" The words are alphabetically equal")