from typing import List

def is_increasing(numbers):
    if len(numbers) == 1:
        return True
    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i+1]:
            return False
    return True

def is_decreasing(numbers):
    if len(numbers) == 1:
        return True
    for i in range(len(numbers) - 1):
        if numbers[i] <= numbers[i+1]:
            return False
    return True

class Solution:
    def goodDaysToRobBank( security: List[int], times: int) -> List[int]:
        if times == 0:
            return [i for i in range(len(security))]
        out = []
        for i in range(times, len(security) - times):
            if not is_increasing(security[i-times:i]):
                if not is_decreasing(security[i+1:i+1+times]):
                    out.append(i)
        return out
    print(goodDaysToRobBank([5,3,3,3,5,6,2], 2))