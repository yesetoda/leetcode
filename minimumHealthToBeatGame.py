damage = [3,3,3]
armor = 0
mx = max(damage)
hp_lost = 0
for i in damage:
    if i!=mx:
        hp_lost+=i
    else:
        hp_lost+=max(0,(i-armor))

print(hp_lost+1)