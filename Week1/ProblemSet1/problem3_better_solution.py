# https://codereview.stackexchange.com/questions/188033/longest-substring-in-alphabetical-order

#s = input("Enter your string s: ")

s = 'cabzaabbcczab'

previous = ''
current = ''
longest= ''

for c in s:
    if c >= previous:
        current += c
        
        if len(longest) < len(current):
            longest = current
    else:
        current = c

    previous = c        
    
print(longest)