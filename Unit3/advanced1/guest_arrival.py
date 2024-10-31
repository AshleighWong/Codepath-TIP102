def arrange_guest_arrival_order(arrival_pattern):
    stack = []
    guest_order = []
    
    for i in range(len(arrival_pattern) +1):
        stack.append(str(i+1))
        
        if i == len(arrival_pattern) or arrival_pattern[i] == 'I':
            while stack:
                guest_order.append(stack.pop())
    
    return ''.join(guest_order)
    
    
print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))
print(arrange_guest_arrival_order("DDDIDIII"))  