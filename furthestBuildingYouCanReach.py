class Solution:
    def furthestBuilding( heights: list[int], bricks: int, ladders: int) -> int:
        difs = []
        for i in range(1,len(heights)):
            difs.append(abs(heights[i]-heights[i-1]))
        uselad = sorted(difs,reverse=True)[:ladders+1]
        cnt = 0
        for i in range(1,len(heights)):
            print(heights[i-1],heights[i])
            if heights[i-1]>=heights[i]:
                cnt+=1
                print("no need ",heights[i-1],heights[i])
            else:
                ht = abs(heights[i]-heights[i-1])
                if ht <=uselad[-1]  or  bricks>= ht :
                    print("diff",ht,"bricks left",bricks)
                    if bricks>0:
                        bricks-= ht
                        cnt+=1
                    print(bricks,"brick ",heights[i-1],heights[i])
                elif ladders>0:
                    ladders-=1
                    cnt+=1
                    # print(ladders,"ladder ",heights[i-1],heights[i])
                elif heights[i]>heights[i-1] and ladders==0 and bricks<ht:
                    # print("i cannot go anymmore")
                    break
        return cnt
    print(furthestBuilding(heights =[1,5,1,2,3,4,10000], bricks = 4, ladders = 1))