vowels = set('aeiou')
word = input("Please input : ")
found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)
