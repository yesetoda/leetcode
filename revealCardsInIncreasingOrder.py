# class Solution:
#     def deckRevealedIncreasing( deck: list[int]) -> list[int]:
#         deck.sort()
#         deck = [deck[i] if i%2==0 else deck[len(deck)-1+i] for i in range(len(deck))]
#         out = []
#         while deck:
#             out.append(deck.pop(0))
#             if deck:
#                 deck.append(deck.pop(0))
#         return out
#     print(deckRevealedIncreasing(deck = [17,13,11,2,3,5,7]))

def srt(deck):
    deck.sort()
    d = []
    j = 0
    k = 0
    print(deck)
    for i in range(len(deck)):
        if i%2==0:
            # d.append(deck[k])
            print("i",k)
            k+=1
        else:
            ind = len(deck)//2+1+j
            print("ind",ind)
            # d.append(deck[ind] )
            j+=1
        # print(d)
    return d
print(srt([17,13,11,2,3,5,7]))