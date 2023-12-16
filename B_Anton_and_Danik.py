leng = int(input())
x = input()
print("Anton" if x.count("A")>leng/2 else  "Danik"  if x.count("A")<leng/2  else "Friendship" )