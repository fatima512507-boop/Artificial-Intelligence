def luhn_check(card_number):
    card_number = str(card_number)
    total = 0
    reverse_digits = card_number[::-1]

    for i in range(len(reverse_digits)):
        digit = int(reverse_digits[i])

        if i % 2 == 1: 
            digit *= 2
            if digit > 9:
                digit -= 9

        total += digit

    if total % 10 == 0:
        return "Valid Card Number"
    else:
        return "Invalid Card Number"


# Test
number = input("Enter card number: ")
print(luhn_check(number))


# Remove Punctuations from a String

import string

text = input("Enter a sentence: ")

no_punct = ""
for char in text:
    if char not in string.punctuation:
        no_punct += char

print("Without Punctuation:", no_punct)


# Sort Sentence in Alphabetical Order

sentence = input("Enter a sentence: ")

words = sentence.split()
words.sort()

print("Sorted sentence:")
for word in words:
    print(word, end=" ")