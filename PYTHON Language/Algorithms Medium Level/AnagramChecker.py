# Create a program that asks the user for two strings and checks if they are anagrams
# (have the same letters in a different order) using a function and displays the result on the screen.

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    for char in s1:
        if s1.count(char) != s2.count(char):
            return False
    return True

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if is_anagram(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
