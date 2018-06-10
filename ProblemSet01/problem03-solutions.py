# https://codereview.stackexchange.com/questions/188033/longest-substring-in-alphabetical-order

s = input("Enter your string s: ")

prev_char = ""
current_string = ""
longest_string = ""

for char in s:
    if prev_char <= char:
        current_string += char
        if len(current_string) > len(longest_string):
            longest_string = current_string
    else:
        current_string = char
    prev_char = char
print('Longest substring in alphabetical order is: ' + longest_string )
