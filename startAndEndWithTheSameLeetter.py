from collections import Counter
s = "abcdeabde"
x = Counter(s)
out = 0
for i in x.values():
    out+=(i*(i+1))//2
print(out)