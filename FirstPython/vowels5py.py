vowels = ['a', 'e', 'i', 'o','u']
word = input("Please inpu: ")

found = {}

for letter in word:
    found.setdefault(letter, 0)
    found[letter] += 1

for k, v in sorted(found.items()):
    print( k, 'was found',v , 'item(s).')
