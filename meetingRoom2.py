import heapq

def minMeetingRooms(intervals):
    # Sort the intervals based on start times
    intervals.sort(key=lambda x: x[0])
    
    # Use a min-heap to keep track of the end times of the meetings
    min_heap = []
    
    # Add the first meeting's end time to the min-heap
    heapq.heappush(min_heap, intervals[0][1])
    # Iterate through the remaining meetings
    for interval in intervals[1:]:
        print(min_heap)
        # Check if the earliest end time in the min-heap is less than or equal to the start time of the current meeting
        if min_heap[0] <= interval[0]:
            # A room is available, so remove the earliest end time from the min-heap
            heapq.heappop(min_heap)
        # Add the end time of the current meeting to the min-heap
        heapq.heappush(min_heap, interval[1])
    
    # The maximum size of the min-heap represents the minimum number of rooms required
    return len(min_heap)

# Example usage
intervals = [[0, 30], [5, 10], [15, 20]]
print(minMeetingRooms(intervals))  # Output: 2
    