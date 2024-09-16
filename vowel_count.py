s = "hello"
vowels = "aeiou"
count = sum(1 for char in s if char in vowels)
print("Vowels:", count)
