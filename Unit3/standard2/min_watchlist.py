def min_remaining_watchlist(watchlist):
    stack = [watchlist[0]]
    
    for i in range(1, len(watchlist)):
        char = watchlist[i]
        if char == 'B' and stack[-1] == 'A':
                stack.pop()
        elif char == 'D' and stack[-1] == 'C':
                stack.pop()
        else:
            stack.append(char)
    return len(stack)

print(min_remaining_watchlist("ABFCACDB")) 
print(min_remaining_watchlist("ACBBD")) 