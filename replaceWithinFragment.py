#Project: Given a string. Replace every occurrence of the letter h by the letter H, except for the first and the last ones.

#Suggested solution:
'''
s = input()
a = s[:s.find('h') + 1] 
b = s[s.find('h') + 1:s.rfind('h')]
c = s[s.rfind('h'):]
s = a + b.replace('h', 'H') + c
print(s)
'''

#my Code:
a = str(input())
b = a.count('h')
counter = 0
if b == 0:
    pass
elif b == 1:
    d = a.index('h')
else:
    d = a.index('h')
    c = str(a[::-1])
    e = len(c) + ((1 + c.index('h')) * -1)
l = a[d+1:e]
j = l.replace('h','H')

for i in j:
    if i != 'H':
        counter = counter + 1
if counter == 0:
    m = a.replace(a[d+1],'H')
    r = m[:(d+1)]
    s = r[:-1] + 'h'
    w = 'h' + m[(e+1):]
    n = s + j + w
    print(n)
else:
    k = a.replace(l, j)
    print(k)