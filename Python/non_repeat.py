def nonRep(s):
    n = len(s)
    for i in range(n):
        found = False
        for j in range(n):
            if i != j and s[i] == s[j]:
                found = True
                break
        if not found:
            return s[i]
    return '$'


inp = input("Enter a lower case string: ")
print(nonRep(inp))