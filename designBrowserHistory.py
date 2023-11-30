class BrowserHistory:

    def __init__(self, homepage: str):
        self.ptr = 0
        self.leng = 1
        self.stack = [homepage]
        

    def visit(self, url: str) -> None:
        self.stack = self.stack[:self.ptr+1]
        self.stack.append(url)
        self.ptr+=1
        self.leng = len(self.stack)
        
    def back(self, steps: int) -> str:
        self.ptr =self.ptr-steps
        self.ptr = self.ptr if self.ptr>=0 and self.ptr<self.leng else 0 if self.ptr<0 else self.leng-1
        return self.stack[self.ptr]
        

    def forward(self, steps: int) -> str:
        self.ptr =self.ptr+steps
        self.ptr = self.ptr if self.ptr>=0 and self.ptr<self.leng else 0 if self.ptr<0 else self.leng-1
        return self.stack[self.ptr]


# Your BrowserHistory object will be instantiated and called as such:
print(obj := BrowserHistory("leetcode"))
print(obj.visit("google"))
print(obj.visit("facebook"))
print(obj.visit("youtube"))
print(param_2 := obj.back(1))
print(param_2 := obj.back(1))
print(param_3 := obj.forward(1))
print(obj.visit("linkedin"))
print(param_3 := obj.forward(2))
print(param_2 := obj.back(2))
print(param_2 := obj.back(7))




