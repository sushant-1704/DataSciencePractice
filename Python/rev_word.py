def reverseWords(s):
    words = [word for word in s.split('.') if word]
    
    words.reverse()
    return '.'.join(words)

inp = input("enter a sentence: ")
print(reverseWords(inp))