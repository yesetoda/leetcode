def meeting_room(times):
    times.sort()
    for i in range(1,len(times)):
        if times[i][0] <=times[i-1][1]:
            return False
    return True
print(meeting_room( [[7,10],[2,4]]))