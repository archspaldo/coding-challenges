def palindrome(text : str) :
    if len(text) < 2 : return True
    if text[0] != text[-1] : return False
    return palindrome(text[1:-1])

print(palindrome("redder"), palindrome("tenet"), palindrome("python"))