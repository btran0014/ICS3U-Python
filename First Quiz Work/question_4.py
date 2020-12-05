first_word=input("Enter a word: ")
second_word=input("Enter another word: ")
if first_word>second_word:
  print(f"{second_word} appears first alphabetically\n{first_word} appears second alphabetically")
elif second_word>first_word:
  print(f"{first_word} appears first alphabetically\n{second_word} appears second alphabetically")
else:
  print("The words are alphabetically equal")