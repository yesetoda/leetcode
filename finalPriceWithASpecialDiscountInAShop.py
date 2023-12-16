class Solution:
    def finalPrices( prices: list[int]) -> list[int]:
        out = []
        for i in range(len(prices)):
            found = False
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    found = True
                    out.append(prices[i]-prices[j])
                    break
            if not found:
                out.append(prices[i])
        return out
        