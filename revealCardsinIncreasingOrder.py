class Solution:
    def deckRevealedIncreasing(deck: list[int]) -> list[int]:
        deck.sort()
        print(deck)
        out = [None for i in range(len(deck))]
        x = 1
        for i in range(len(deck)):
            if i<len(deck)/2:
                out[2*i] = deck[i]
            else:
                print(x)
                if out[x]==None:
                    out[x] = deck[i]
                    x+=4
                else:
                    x+=1
                    out[x] = deck[i]
                    x+=4
                x %=len(deck)
                
            print(out)
        print(out)
        
    print(deckRevealedIncreasing(deck = [17,13,11,2,3,5,7]))
        