import math
from functools import reduce
import re

# Problem 1: GCD of multiple numbers
def problem_1_gcd_multiple_numbers():
    nums = list(map(int, input("Enter numbers separated by spaces to find the GCD: ").split()))
    return reduce(math.gcd, nums)

# Problem 2: Count vowels in a string
def problem_2_count_vowels():
    string = input("Enter a string to count vowels: ")
    vowels = "aeiouAEIOU"
    return sum(1 for char in string if char in vowels)

# Problem 3: Count occurrences of a substring
def problem_3_count_occurrences():
    substring = input("Enter the substring to search for: ")
    string = input("Enter the main string: ")
    return string.count(substring)

# Problem 4: Convert UpperCamelCase to lowercase_with_underscores
def problem_4_convert_case():
    s = input("Enter a string in UpperCamelCase to convert: ")
    return ''.join(['_' + i.lower() if i.isupper() else i for i in s]).lstrip('_')

# Problem 5: Validate if a number is a palindrome
def problem_5_is_palindrome():
    n = int(input("Enter a number to check if it is a palindrome: "))
    return str(n) == str(n)[::-1]

# Problem 6: Extract the first number from text
def problem_6_extract_number():
    text = input("Enter a text to extract the first number: ")
    match = re.search(r'\d+', text)
    return int(match.group()) if match else None

# Problem 7: Count bits with value 1 in a number
def problem_7_count_bits():
    n = int(input("Enter a number to count its '1' bits: "))
    return bin(n).count('1')

# Problem 8: Count how many words exist in a text
def problem_8_count_words():
    text = input("Enter a text to count words: ")
    return len(text.split())

############################
if __name__ == "__main__":
    
    print(problem_1_gcd_multiple_numbers()) 
    
    print(problem_2_count_vowels()) 
    
    print(problem_3_count_occurrences()) 
    
    print(problem_4_convert_case())  
    
    print(problem_5_is_palindrome()) 
    
    print(problem_6_extract_number()) 
    
    print(problem_7_count_bits())  
    
    print(problem_8_count_words())  
