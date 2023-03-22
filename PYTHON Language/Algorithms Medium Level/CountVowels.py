# Create a program that asks the user for a sentence and then counts the number of vowels
# in the sentence using a loop and displays the result on the screen.

sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
count = 0

for letter in sentence:
    if letter in vowels:
        count += 1

print("The sentence has", count, "vowels.")
