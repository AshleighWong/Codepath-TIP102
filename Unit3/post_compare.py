def post_compare(draft1, draft2):
    return cleaned(draft1) == cleaned(draft2)

def cleaned(draft):
    stack = []
    for char in draft:
        if char != '#':
            stack.append(char)
        elif stack and char == '#':
            stack.pop()
    return ''.join(stack)
        

print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 
'''
True
True
False
'''
