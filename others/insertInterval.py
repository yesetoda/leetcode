class Solution:
    # def insert1( intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    #     out = []
    #     x = set(newInterval)
    #     for i in intervals:
    #         if newInterval[0]<=i[0] and newInterval[1]>=i[0] or newInterval[0]<=i[1] and newInterval[1]>=i[1]:
    #             x.add(i[0])
    #             x.add(i[1])
    #         else:
    #             out.append(i)
    #     out.append([min(x),max(x)])
    #     out.sort()
    #     return out
    def insert1( intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        out = []
        merged = False
        for interval in intervals:
            if interval[1] < newInterval[0]:
                out.append(interval)
                print("if")
            elif interval[0] > newInterval[1]:
                print("elif")
                if not merged:
                    out.append(newInterval)
                    merged = True
                out.append(interval)
            else:
                print("else")
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
            print(out)
        if not merged:
            out.append(newInterval)
        return out
    print(insert1(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))

    def insert1( intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        out = []
        merged = False
        for interval in intervals:
            if interval[1] < newInterval[0]:
                out.append(interval)
            elif interval[0] > newInterval[1]:
                if not merged:
                    out.append(newInterval)
                    merged = True
                out.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        if not merged:
            out.append(newInterval)
        return out