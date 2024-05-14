sentence = input("Enter a sentence: ")
characters = [char.lower() for char in sentence]
characters.sort()
print("Sorted:", "".join(characters))