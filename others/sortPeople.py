class Solution:
    def sortPeople(names: list[str], heights: list[int]) -> list[str]:
        ind = heights[::]
        ind.sort(reverse=True)
        out = []
        for i in ind:
            out.append(names[heights.index(i)])
        return out
    names = ["Mary","John","Emma"]
    heights = [180,165,170]
    print(sortPeople(names , heights))