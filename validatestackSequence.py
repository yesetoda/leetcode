class Solution:
    def validateStackSequences( pushed: list[int], popped: list[int]) -> bool:
        pushed = pushed[::-1]
        stack =[]
        for i in popped:
            while i not in stack:
                if pushed:
                    stack.append(pushed.pop())
                else:
                    return False
            else:
                if stack:
                    stack.pop()
                else:
                    return False
        return True
    print(validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1]))