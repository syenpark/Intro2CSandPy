s = input('Enter your string s: ')

last = 0
pre = 0
subs = []
max = ''

for i in range(len(s)-1):
    if s[i] > s[i+1]:
        last = i+1
        subs.append(s[pre:last])
        pre = i+1
        
subs.append(s[last:])

for sub in subs:
    if len(sub) > len(max):
        max = sub

print('Longest substring in alphabetical order is: ', max)
