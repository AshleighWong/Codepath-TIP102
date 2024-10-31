from collections import deque

def reveal_attendee_list_in_order(attendees):
    sorted_attendees = sorted(attendees)
    n = len(attendees)
    queue = deque(range(n))
    result = [0] * n
    for number in sorted_attendees:
        index = queue.popleft()
        result[index] = number
        if queue:
            queue.append(queue.popleft())
    return result


print(reveal_attendee_list_in_order([17,13,11,2,3,5,7]))
print(reveal_attendee_list_in_order([1,1000]))       