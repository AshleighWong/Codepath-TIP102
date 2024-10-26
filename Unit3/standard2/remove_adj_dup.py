def remove_duplicate_shows(schedule):
    stack = [schedule[0]]
    for i in range(1, len(schedule)):
        char = schedule[i]
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)
    

print(remove_duplicate_shows("abbaca")) 
print(remove_duplicate_shows("azxxzy")) 