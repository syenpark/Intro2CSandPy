# https://codereview.stackexchange.com/questions/188033/longest-substring-in-alphabetical-order

s = input("Enter your string s: ")

prevChar = ""
currentString = ""
longestString = ""

for char in s:
    if prevChar <= char:
        currentString += char
        if len(currentString) > len(longestString):
            longestString = currentString
    else:
        currentString = char
    prevChar = char
print('Longest substring in alphabetical order is: ' + longestString )
