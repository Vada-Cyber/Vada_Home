word = input(">>> ")

for c in word:
    print(c)

# vowels = "aeiouAEIOU"
vowels = word

for vowel in vowels:
    vowel_count = word.count(vowel)
    print(f"{vowel}: {vowel_count}")


print(word[::-1])

