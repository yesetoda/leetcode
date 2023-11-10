class Solution:
    def defangIPaddr(address: str) -> str:
        return address.replace("." ,"[.]")
    address = "1.1.1.1"
    print(defangIPaddr(address))