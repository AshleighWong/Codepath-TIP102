
def is_valid_post_format(posts):
    tags = {')': '(', ']': '[', '}': '{'}
    stack = []
    for tag in posts:
        if tag in tags.values():
            stack.append(tag)
        elif tag in tags.keys():
            if not stack or stack[-1] != tags[tag]:
                return False
    return True

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))