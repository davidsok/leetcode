def palindrome(str: str) -> bool:
    return str == str[::-1]

print(palindrome('racecar'))