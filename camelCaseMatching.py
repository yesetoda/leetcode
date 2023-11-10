class Solution:
    def camelMatch(queries: list[str], pattern: str) -> list[bool]:
        out = []
        for i in queries:
            found = False
            for j in set(pattern):
                if i.count(j)<pattern.count(j) or len([k for k in i if k.isupper()])>len([k for k in pattern if k.isupper()]):
                    out.append(False)
                    found = True
                    break
            if not found:
                out.append(True)
        return out
            