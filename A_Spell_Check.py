from collections import Counter
correct_name = Counter("Timur")
for i in range(int(input())):
    leng = int(input())
    s = input()
    if leng>5:
        print("NO")
    else:
        found = False
        freq = Counter(s)
        for ch,fr in correct_name.items():
            if freq[ch]!=fr:
                found = True
                break
            
        print("YES" if not found else "NO")