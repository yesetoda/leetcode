# # from collections import Counter
# # class FreqStack:
# #     def __init__(self):
# #         self.stack = []
# #         self.freq = Counter()
# #         self.ind = 0

# #     def push(self, val: int) -> None:
# #         self.stack.append(val)
        
# #         if val not in self.freq:
# #             self.freq[val] = [1,[self.ind]]
# #         else:
# #             self.freq[val][0] += 1
# #             self.freq[val][1].append(self.ind)
# #         self.ind+=1
# #     def pop(self) -> int:
# #         print(self.stack)
# #         print(self.freq)
# #         print(self.ind)
# #         self.ind-=1
# #         print("this is the most common elemenr",self.freq.most_common())
# #         # most_freq = [i for i in self.freq.most_common()]
# #         indx  =self.freq.most_common()[0][1][1][-1]
# #         print("this is the index",indx)
# #         val = self.stack.pop(indx)
# #         # if val in self.freq:
# #         self.freq[val][0] -= 1
# #         print("before",self.freq.most_common()[0][1][1])
# #         self.freq.most_common()[0][1][1].pop()
# #         print("after",self.freq.most_common()[0][1][1])
# #         if self.freq[val][0] == 0:
# #             del self.freq[val]
# #         return val
        
# from collections import defaultdict

# class FreqStack:
#     def __init__(self):
#         self.stack = []
#         self.freq = defaultdict(list)
#         self.ind = 0

#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         self.freq[val].append(self.ind)
#         self.ind += 1

#     def pop(self) -> int:
#         max_freq = max(self.freq.values())
#         max_freq_elements = [elem for elem, indices in self.freq.items() if len(indices) == max_freq]
#         max_freq_elements.sort(reverse=True)
#         val = max_freq_elements[0]
#         index_to_remove = self.freq[val].pop()
#         self.stack.pop(index_to_remove)
#         if not self.freq[val]:
#             del self.freq[val]
#         return val


# # Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(5)
# obj.push(7)
# obj.push(5)
# obj.push(7)
# obj.push(5)
# print(obj.pop())  # Output: 5
# print(obj.pop())  # Output: 7
# print(obj.pop())  # Output: 5
# print(obj.pop())  # Output: 7


# # # Your FreqStack object will be instantiated and called as such:
# # obj = FreqStack()
# # obj.push(5)
# # obj.push(7)
# # obj.push(5)
# # obj.push(7)
# # obj.push(5)
# # obj.pop()
# # obj.pop()
# # obj.pop()
# # param_2 = obj.pop()

a = {1:[1,5],2:[0,0,4]}
a = dict(sorted(a.items(), key=lambda x: (-len(x[1]), -max(x[1]))))
print(a)
print(max(a.values(),key =len))