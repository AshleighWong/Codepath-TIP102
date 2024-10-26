def clean_post(post):
    stack = []
    for char in post:
        if char.islower():
            stack.append(char)
        else:
            if stack and char.lower() == stack[-1]:
                stack.pop()
    
    return ''.join(stack)

print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 