letters = ['a', 'b', 'c', 'd', 'e']


# for character in letters:
#   print(type(character))


for character in enumerate(letters):
    print(f"Index = {character[0]}, value = {character[1]}")


for index, char in enumerate(letters):
    print(f"Index = {index}, value = {char}")


item = ('0','a')
item[0]
item[1]

index, char = (0, 'a')