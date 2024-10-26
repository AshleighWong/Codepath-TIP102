from collections import deque

def time_required_to_stream(movies, k):
    queue = deque()
    for i in range(len(movies)):
        queue.append((i, movies[i]))
    seconds = 0
    
    while queue:
        person, remaining = queue.popleft()
        seconds +=1
        
        if remaining > 1:
            queue.append((person, remaining-1))
        if person == k and remaining == 1:
            return seconds



print(time_required_to_stream([2, 3, 2], 2)) 
print(time_required_to_stream([5, 1, 1, 1], 0)) 