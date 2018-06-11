occurs = 'bob'
num = 0

for x in range(len(s)):
    if s[x:x+len(occurs)] == occurs:
        num += 1
        
print("Number of times bob occurs is: ", num)
