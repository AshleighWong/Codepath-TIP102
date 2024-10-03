
def reverse_comments_queue(comments):
    stack = []
    while comments:
        stack.append(comments[-1])
        comments.pop()
    return stack

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))