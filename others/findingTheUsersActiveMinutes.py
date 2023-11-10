class Solution:
    def findingUsersActiveMinutes( logs: list[list[int]], k: int) -> list[int]:
        leng = len(logs)
        log = {}
        out =[0 for i in range(k)]
        for i  in range(leng):
            if logs[i][0] not in log:
                log[logs[i][0]] = {logs[i][1],}
            else:
                if logs[i][1] in log[logs[i][0]]:
                    pass
                else:
                    log[logs[i][0]].add(logs[i][1])
        for els in log.values():
            out[len(els)-1]+=1
        return out
    
    print(findingUsersActiveMinutes(logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5))
    
class Solution:
    def findingUsersActiveMinutes2( logs: list[list[int]], k: int) -> list[int]:
        log = {}
        max_uam = 0
        for i in range(len(logs)):
            user_id, minute = logs[i]
            if user_id not in log:
                log[user_id] = {minute}
            else:
                log[user_id].add(minute)
            max_uam = max(max_uam, len(log[user_id]))
        
        out = [0] * (max_uam + 1)
        for els in log.values():
            out[len(els)] += 1
        
        return out[1:k+1]
    print(findingUsersActiveMinutes2(logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5))
